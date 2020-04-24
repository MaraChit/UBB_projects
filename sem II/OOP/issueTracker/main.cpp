#include "issueTracker.h"
#include <QtWidgets/QApplication>

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	Repo r;
	std::vector<User> vector = r.returnUsers();
	for (auto i : vector)
	{
		issueTracker* w = new issueTracker(r, i);
		r.addObserver(w);
		std::string s = i.getName() + "-" + i.getType();
		w->setWindowTitle(s.c_str());
		w->show();
	}
	return a.exec();
}
