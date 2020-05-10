from controller import Controller
from repository import Repository

def main():
    
    repository = Repository()
    controller = Controller(repository)
    controller.runAlg()
    
main()