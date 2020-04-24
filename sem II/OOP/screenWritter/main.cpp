#include "screenWritter.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	Repo r;
	
	std::vector<Writter> vector = r.returnWritters();
	for (auto i : vector)
	{
		screenWritter* w= new screenWritter(r,i);
		//QString::fromStdString(i.getName());
		w->setWindowTitle(i.getName().c_str());
		w->show();
	}

	return a.exec();
}
