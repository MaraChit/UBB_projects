#include "QtGuiApplication1.h"
#include <QtWidgets/QApplication>
#include "guiMenu.h"
#include <fstream>
#include "controller.h"
int main(int argc, char *argv[])
{
	QApplication a(argc, argv);

	//QtGuiApplication1 w;
	//w.show();
	TrenchCoatRepo trenchRepository;
	user_repo trenchBuyerRepo;
	controller control(&trenchRepository);

	std::ifstream filein{ "path.txt" };
	std::string pathRepo;
	std::string pathUser;
	filein >> pathRepo >> pathUser;
	if (strcmp(pathRepo.c_str(), "memory") != 0)
	{
		control.setFileLocation(pathRepo);
		control.readFromFile();
	}
	if (strcmp(pathUser.c_str(), "memory") != 0)
		trenchBuyerRepo.setFileLocation(pathUser);

	guiMenu GUI(control,trenchBuyerRepo);
	GUI.show();


	return a.exec();
}
