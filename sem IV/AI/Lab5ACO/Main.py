from Controller import Controller
from Problem import Problem
from UI import UI


def main():
    problem = Problem()
    controller = Controller()
    ui = UI(controller)
    
    problem.loadProblem ()
    controller.loadParameters(problem)
    ui.run()


main()