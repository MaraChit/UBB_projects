from Grammar import Grammar
from scanner import Scanner


class Parser:
    def __init__(self, g):
        # grammar for the parser
        self.grammar = g
        # dictionary of the first for each non terminal
        self.firstDict = {}
        # dictionary of the follow for each non terminal
        self.followDict = {}
        # parsing table
        self.parsingTable = {}
        # dictionary with key, value pairs: key-index, value-the associated production
        self.numberedDictionary = {}

    def addToFirst(self, key, value):
        if key not in self.firstDict.keys():
            self.firstDict[key] = []
        self.firstDict[key].append(value)

    def addToFollow(self, key, value):
        if key not in self.followDict.keys():
            self.followDict[key] = []
        self.followDict[key].append(value)

    def ifExistInProductions(self, key, value):
        productions = self.grammar.getProductionsForNonTerminal(key)
        for prod in productions:
            for elem in prod:
                if elem == value:
                    return True
        return False

    def first(self):
        productions = self.grammar.getProductions()
        dict = {}
        count = 0
        for key in productions:
            # complete intermediary dict
            value = []
            for i in productions[key]:
                # add terminals to firstDict and nonTerminals to intermediary dict
                if i[0] in self.grammar.getTerminals():
                    self.addToFirst(key, i[0])
                else:
                    value.append(i[0])
                    count += 1
            dict[key] = value

        # for each nonTerminal in dict substitute with the value of it from firstDict
        while count >= 0:
            for key in dict:
                for i in dict[key]:
                    if i in self.firstDict.keys():
                        for elem in self.firstDict[i]:
                            self.addToFirst(key, elem)
                        count = count - 1
                    else:
                        continue

        # remove duplicates
        for elem in self.firstDict:
            l = list(dict.fromkeys(self.firstDict[elem]))
            self.firstDict[elem] = l

    def follow(self):
        productions = self.grammar.getProductions()
        dict = {}
        count = 0
        # create empty list in the intermediary dict for each nonTerminal(key)
        for elem in self.grammar.getNonTerminals():
            dict[elem] = []

        self.addToFollow(self.grammar.getStartingSymbol(), 'eps')

        for prod in productions:
            for i in range(0, len(productions[prod][0])):
                nonTerminal = productions[prod][0][i]
                if nonTerminal in self.grammar.getNonTerminals():
                    # if current non terminal S and A->BS => add A to follow(S) in dict
                    if i == len(productions[prod][0]) - 1:
                        dict[nonTerminal].append(prod)
                        count += 1
                    else:
                        # if current=B and A->B terminal, Follow(B).append(terminal)
                        if productions[prod][0][i + 1] in self.grammar.getTerminals():
                            self.addToFollow(nonTerminal, productions[prod][0][i + 1])
                        # if current=B and A->BX, Follow(B).append(first(x))
                        else:
                            for k in self.firstDict[productions[prod][0][i + 1]]:
                                self.addToFollow(nonTerminal, k)
                            # current=B and A->BX and X EVER goes to eps => add A to follow(S) in dict
                            if self.ifExistInProductions(productions[prod][0][i + 1], 'eps'):
                                dict[nonTerminal].append(prod)
                                count += 1
        # for each nonTerminal in dict substitute with the value of it from followDict
        while count != 0:
            for key in dict:
                for i in dict[key]:
                    if key == i:
                        count -= 1
                    elif i in self.followDict.keys():
                        for elem in self.followDict[i]:
                            self.addToFollow(key, elem)
                        count = count - 1
                    else:
                        continue
                if count == 0:
                    break

        for prod in self.grammar.getNonTerminals():
            if prod not in self.followDict.keys():
                self.followDict[prod] = []

        # remove duplicates
        for elem in self.followDict:
            l = list(dict.fromkeys(self.followDict[elem]))
            self.followDict[elem] = l

        # (S,+):[['B', 'A'],0]
        # {0: ['S', ['B', 'A']],
        # 1: ['A', ['#', 'B', 'A']],
        # 2: ['A', ['eps']],
        # 3: ['B', ['D', 'C']],
        # 4: ['C', ['*', 'D', 'C']],
        # 5: ['C', ['eps']],
        # 6: ['D', ['(', 'S', ')']],
        # 7: ['D', ['a']]}

    def addNumbers(self):
        i = 0
        for key in self.grammar.getProductions():
            for elem in self.grammar.getProductionsForNonTerminal(key):
                self.numberedDictionary[i] = [key, elem]
                i += 1

    def returnNumber(self, key, value):
        list2 = [key, value]
        for a in self.numberedDictionary:
            if self.numberedDictionary[a] == list2:
                return a

    def fillParsingTable(self):
        self.first()
        self.follow()
        self.addNumbers()
        productions = self.grammar.getProductions()
        for nonterminal in self.grammar.getNonTerminals():
            for terminal in self.grammar.getTerminals():
                key = (nonterminal, terminal)
                self.parsingTable[key] = []
        for prod in productions:
            for t in productions[prod]:
                if t[0] == 'eps':
                    list1 = self.followDict[prod]
                    for i in list1:
                        index = self.returnNumber(prod, [t[0]])
                        self.parsingTable[(prod, i)].append([t[0]])
                        self.parsingTable[(prod, i)].append(index)
                elif t[0] in self.grammar.getTerminals():
                    index = self.returnNumber(prod, t)
                    self.parsingTable[(prod, t[0])].append(t)
                    self.parsingTable[(prod, t[0])].append(index)
                elif t[0] in self.grammar.getNonTerminals():
                    list1 = self.firstDict[t[0]]
                    for i in list1:
                        index = self.returnNumber(prod, t)
                        self.parsingTable[(prod, i)].append(t)
                        self.parsingTable[(prod, i)].append(index)

    def parseSequence(self, sequenceList):
        self.fillParsingTable()
        sequenceList.append('eps')
        workingList = [self.grammar.getStartingSymbol(), 'eps']
        resultList = []
        result = ''
        ok = True
        while ok:
            if sequenceList[0] != workingList[0] and workingList[0] in self.grammar.getNonTerminals():
                lista = self.parsingTable[(workingList[0], sequenceList[0])]
                # print(list)
                if lista[0] == ['eps']:
                    workingList.pop(0)
                    resultList.append(lista[1])
                else:
                    resultList.append(lista[1])
                    workingList.pop(0)
                    lista[0].reverse()
                    workingList.reverse()
                    for i in lista[0]:
                        workingList.append(i)
                    workingList.reverse()
                    lista[0].reverse()
            elif sequenceList[0] == workingList[0] and sequenceList[0] != 'eps':
                sequenceList.pop(0)
                workingList.pop(0)
            elif sequenceList[0] == 'eps' and workingList[0] == 'eps':
                ok = False
                result = 'accepted'
            else:
                ok = False
                result = 'error'

        # print(sequenceList)
        # print(workingList)
        if result == 'accepted':
            return resultList
        else:
            return 'Not accepted'

    def showResult(self, sequence):
        result = self.parseSequence(sequence)
        productions = ""
        for elem in result:
            rhs = ""
            for rhs1 in self.numberedDictionary[elem][1]:
                rhs += rhs1
            productions = productions + self.numberedDictionary[elem][0] + "->" + rhs + "\n"
        return productions

    # {0: ['S', ['B', 'A']],
    # 1: ['A', ['#', 'B', 'A']],
    # 2: ['A', ['eps']],
    # 3: ['B', ['D', 'C']],
    # 4: ['C', ['*', 'D', 'C']],
    # 5: ['C', ['eps']],
    # 6: ['D', ['(', 'S', ')']],
    # 7: ['D', ['a']]}

    # [0, 3, 7, 4, 6, 0, 3, 7, 5, 1, 3, 7, 5, 2, 5, 2]
    # [[s],[b,a],[d,c,a],[a,c,a],[a,*,...]
    def derivationString(self, sequence):
        #sequence = self.parseSequence(seq)
        result = []
        result.append([self.grammar.startingSymbol])
        poz = 0
        index = 0
        while index < len(sequence):
            newList = []
            rhs = self.numberedDictionary[sequence[index]][1]
            if poz != 0:
                for i in range(0, poz):
                    newList.append(result[index][i])
            while result[index][poz] in self.grammar.getTerminals():
                newList.append(result[index][poz])
                poz += 1

            for elem1 in rhs:
                newList.append(elem1)

            for i in range(poz + 1, len(result[index])):
                newList.append(result[index][i])
            index += 1
            result.append(newList)
        return result

    def derivString(self, seq):
        result = self.parseSequence(seq)
        string = ""
        rhs = ""
        for rhs1 in self.numberedDictionary[0][1]:
            rhs += rhs1
        string = string + self.numberedDictionary[0][0] + "->" + rhs
        for elem in result:
            prod = self.numberedDictionary[elem][1]
            for i in prod:
                poz = 0
                if i in self.grammar.getNonTerminals():
                    prod2 = self.numberedDictionary[elem + 1][1]
                    rhs = ""
                    for rhs1 in prod2:
                        rhs += rhs1
                    string = string + "->" + rhs
                    for t in prod[poz:]:
                        string += t

                else:
                    string = string + i
                    for t in prod[poz:]:
                        string += t
                poz += 1
        return string


if __name__ == '__main__':
    grammar1 = Grammar("g1.txt")
    parser1 = Parser(grammar1)
    string = 'a * ( a # a )'
    sequence1 = string.split(" ")
    se1 = string.split(" ")
    print("Grammar 1:")
    finish=parser1.parseSequence(se1)
    print(finish)
    #print(parser1.showResult(se1))
    print(parser1.derivationString(finish))
    print(' ')

    scanner2 = Scanner("pb1.txt")
    scanner2.scan()
    sequence2 = []
    pif = scanner2.programInternalForm
    #print(pif)
    for elem in pif:
        sequence2.append(pif[elem][0])

    grammar2 = Grammar("g2.txt")
    parser2 = Parser(grammar2)

    parser2.fillParsingTable()
    '''
    for elem in parser2.parsingTable:
        print(elem, "has", parser2.parsingTable[elem])
        print()
        '''
    print('Grammar 2:')
    finish2 = parser2.parseSequence(sequence2)
    print(finish2)
    print(parser2.derivationString(finish2))
    
