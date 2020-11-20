"""
Grammar file will be constructed as follows:
line 1: non-terminals separated by space
line 2: terminals separated by space
line 3: starting symbol
line 4+: productions on each line following this rule:
            non-terminal separated by space from symbols
            and the symbols separated by "+"
            ex: S a+b+S
"""


class Grammar:
    def __init__(self, filename):
        self.file = filename
        self.nonTerminals = None
        self.terminals = None
        self.productions = {}
        self.startingSymbol = None
        self.readGrammar()

    def readGrammar(self):
        with open(self.file) as f:
            # get the set of  non-terminal symbols
            line = f.readline()
            self.nonTerminals = line[0:-1].split(" ")

            # get the set of terminal symbols
            line = f.readline()
            self.terminals = line[0:-1].split(" ")

            # get the starting symbol
            line = f.readline()
            start = line[0:-1].split(" ")
            self.startingSymbol = start[0]

            # get the finite set of productions
            line = f.readline()
            while line:
                production = line[0:-1].split(" ")
                # print(production)
                if production[0] not in self.productions.keys():
                    self.productions[production[0]] = []
                splitList = production[1].split("+")
                self.productions[production[0]].append(splitList)

                line = f.readline()

    def getTerminals(self):
        return self.terminals

    def getNonTerminals(self):
        return self.nonTerminals

    def getStartingSymbol(self):
        return self.startingSymbol

    def getProductions(self):
        return self.productions

    def getProductionsForNonTerminal(self, key):
        return self.productions[key]

    def printProductionsForNonTerminal(self, key):
        productionString = ""
        productionString = productionString + key + " -> "
        size = 0
        for p in self.productions[key]:
            size += 1
            for elem in p:
                productionString = productionString + elem + " "
            if size == len(self.productions[key]):
                productionString = productionString + "\n"
            else:
                productionString = productionString + " | "
        return productionString

    def printProductions(self):
        productionString = ""
        for prod in self.productions.keys():
            productionString = productionString + prod + " -> "
            size = 0
            for p in self.productions[prod]:
                size += 1
                for elem in p:
                    productionString = productionString + elem + " "
                if size == len(self.productions[prod]):
                    productionString = productionString + "\n"
                else:
                    productionString = productionString + " | "
        return productionString


def printOptions():
    print("")
    print("1.Print terminals")
    print("2.Print non terminals")
    print("3.Print starting symbol")
    print("4.Print transitions")
    print("5.Print production for a non terminal")
    print("0.Exit")
    print("")


if __name__ == '__main__':
    grammar = Grammar("g2.txt")
    while True:
        try:
            printOptions()
            command = int(input(">>"))
            if command == 1:
                print(grammar.getTerminals())
            elif command == 2:
                print(grammar.getNonTerminals())
            elif command == 3:
                print(grammar.getStartingSymbol())
            elif command == 4:
                print(grammar.printProductions())
            elif command == 5:
                nonterm = input("Specify nonterminal: ")
                print(grammar.printProductionsForNonTerminal(nonterm))
            elif command == 0:
                break
            else:
                print("Invalid option!!!!!")

        except Exception as e:
            print(e)
            print("Something went wrong!")
