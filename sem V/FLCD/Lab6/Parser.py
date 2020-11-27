from Grammar import Grammar


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

        self.addToFollow(grammar.getStartingSymbol(), 'eps')

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
        list = [key, value]
        for a in self.numberedDictionary:
            if self.numberedDictionary[a] == list:
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
                    list = self.followDict[prod]
                    for i in list:
                        index = self.returnNumber(prod, [t[0]])
                        self.parsingTable[(prod, i)].append([t[0]])
                        self.parsingTable[(prod, i)].append(index)
                elif t[0] in self.grammar.getTerminals():
                    index = self.returnNumber(prod, t)
                    self.parsingTable[(prod, t[0])].append(t)
                    self.parsingTable[(prod, t[0])].append(index)
                elif t[0] in self.grammar.getNonTerminals():
                    list = self.firstDict[t[0]]
                    for i in list:
                        index = self.returnNumber(prod, t)
                        self.parsingTable[(prod, i)].append(t)
                        self.parsingTable[(prod, i)].append(index)

    def sequenceToList(self, sequence):
        list = sequence.split(" ")
        return list

    def parseSequence(self, sequence):
        self.fillParsingTable()
        sequenceList = self.sequenceToList(sequence)
        sequenceList.append('eps')
        workingList = [self.grammar.getStartingSymbol(), 'eps']
        resultList = []

        result = ''

        ok = True
        while ok:
            if sequenceList[0] != workingList[0] and workingList[0] in self.grammar.getNonTerminals():
                list = self.parsingTable[(workingList[0], sequenceList[0])]
                if list[0] == ['eps']:
                    workingList.pop(0)
                    resultList.append(list[1])
                else:
                    resultList.append(list[1])
                    workingList.pop(0)
                    list[0].reverse()
                    workingList.reverse()
                    for i in list[0]:
                        workingList.append(i)
                    workingList.reverse()
                    list[0].reverse()
            elif sequenceList[0] == workingList[0] and sequenceList[0] != 'eps':
                sequenceList.pop(0)
                workingList.pop(0)
            elif sequenceList[0] == 'eps' and workingList[0] == 'eps':
                ok = False
                result = 'accepted'
            else:
                ok = False
                result = 'error'

        if result == 'accepted':
            return resultList
        else:
            return 'Not accepted'


if __name__ == '__main__':
    grammar = Grammar("g3.txt")
    parser = Parser(grammar)

    # print(parser.sequenceToList('( int ) + int'))
    parser.fillParsingTable()
    print(parser.parsingTable)

    print(parser.parseSequence('a * ( a # a )'))
    

    # parser.first()
    # parser.follow()
    #
    # print("First")
    # print(parser.firstDict)
    # # print(len(parser.firstDict))
    #
    # print("Follow")
    # print(parser.followDict)
