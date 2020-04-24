#include "taskManager.h"
#include <QtWidgets/QApplication>
#include "Repo.h"
#include <fstream>
#include <vector>

int main(int argc, char *argv[])
{
	Repo repo;
	std::ifstream fin("programmers.txt");
	std::string name;
	int id;
	std::vector<Programmer> programmers;
	while (fin >> id && fin >> name)
	{
		Programmer newProgrammer(id, name);
		programmers.push_back(newProgrammer);

	}
	
	
	QApplication a(argc, argv);
	
	for (auto p : programmers)
	{
		taskManager* task = new taskManager(repo,p);
		//taskManager w(repo,p);
		task->setWindowTitle(QString::fromStdString(p.getName()));
		task->show();
		repo.addObs(task);
	}
		
	return a.exec();
}
