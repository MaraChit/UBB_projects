from Controller import Controller


class UI:
    def __init__(self,c: Controller):
        self._controller = c

    def run(self):
        (fit, sol) = self._controller.runAlg()
        print("Solution:")
        for line in sol:
            print(line)
        print("Fitness is: ", fit)
        self._controller.runValidationTest()