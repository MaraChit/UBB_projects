#include "codeReview.h"
#include <QtWidgets/QApplication>
#include <assert.h>
void testAdd()
{
	Repo rrr;
	assert(rrr.returnCode().size() == 3);
	std::string name = "name";
	std::string creator = "creator";
	std::string reviewr = "rev";
	rrr.addCode(name, 0, creator, reviewr);
	assert(rrr.returnCode().size() == 4);

}
int main(int argc, char *argv[])
{
	QApplication a(argc, argv);
	testAdd();
	Repo r;
	std::vector<Programmer> v = r.returnProgrammer();
	for (auto i : v)
	{
		codeReview* w = new codeReview(r,i);
		r.addObserver(w);
		w->setWindowTitle(i.getName().c_str());
		w->show();
	}
	return a.exec();
}
