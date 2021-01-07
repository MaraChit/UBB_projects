from Grammar import Grammar


class Parser:
    def __init__(self, g):
        self.grammar = g
        self.firstDict = {}
        self.followDict = {}
        self.parsingTable = {}

    def addToFirst(self, key, value):
        if key not in self.firstDict.keys():
            self.firstDict[key] = []
        self.firstDict[key].append(value)

    def addToFollow(self, key, value):
        if key not in self.followDict.keys():
            self.followDict[key] = []
        self.followDict[key].append(value)

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

    def ifExistInProductions(self, key, value):
        productions = self.grammar.getProductionsForNonTerminal(key)
        for prod in productions:
            for elem in prod:
                if elem == value:
                    return True
        return False

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
                    # if current nonterminal S and A->BS => add A to follow(S) in dict
                    if i == len(productions[prod][0]) - 1:
                        dict[nonTerminal].append(prod)
                        count += 1
                    else:
                        # if current=B and A->B terminal, Follow(B).append(terminal)
                        if productions[prod][0][i + 1] in self.grammar.getTerminals():
                            self.addToFollow(nonTerminal,productions[prod][0][i+1])
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

        # remove duplicates
        for elem in self.followDict:
            l = list(dict.fromkeys(self.followDict[elem]))
            self.followDict[elem] = l


if __name__ == '__main__':
    grammar = Grammar("g3.txt")
    parser = Parser(grammar)
    parser.first()
    parser.follow()

    print("First")
    print(parser.firstDict)
    # print(len(parser.firstDict))

    print("Follow")
    print(parser.followDict)
