#include "screenWritter.h"
#include <vector>
#include <qmessagebox.h>

bool cmp(Idea a, Idea b)
{
	return a.getStatus() < b.getStatus();
}
void screenWritter::afisare()
{
	std::vector<Idea>v=repo.returnIdeas();
	std::sort(v.begin() + 0, v.end(), cmp);
	std::string stat;
	for (auto i : v)
	{
		if (i.getStatus() == 1)
			stat = "accepted";
		else
			stat = "proposed";
		std::string print = stat + ", " + i.getText() + ", " + std::to_string(i.getAct()) + ", " + i.getProposer();
		new QListWidgetItem (print.c_str(), this->ui.listWidget);
	}
}

void screenWritter::handleAdd()
{
	std::string name = ui.lineEdit->text().toStdString();
	std::string act = ui.lineEdit_2->text().toStdString();
	int ok = 1;
	if (name == "" || act == "")
	{
		QMessageBox q;
		q.critical(0, "ERROR", "Complete them all!");
	}
	else
	{


		if (act != "1" && act != "2" && act != "3")
		{
			QMessageBox q2;
			q2.critical(0, "ERROR", "Not an existing act");
		}
		else {

			std::vector<Idea> v = repo.returnIdeas();
			for (auto i : v)
			{
				if (i.getAct() == stoi(act))
					if (i.getText() == name)
					{
						ok = 0;
					}
			}
		}
	}
	if (ok == 0)
	{
		
		QMessageBox q3;
		q3.critical(0, "Error", "Already exists");
	}
	else
	{
		repo.addIdea(0, name, stoi(act), writter.getName());
		this->ui.listWidget->clear();
		this->afisare();
	}
}
void screenWritter::handleRevise()
{
	int nr = this->ui.listWidget->currentIndex().row();
	std::vector<Idea> v = repo.returnIdeas();
	if (writter.getRank() == "senior")
	{
		if (v[nr].getStatus() == 0)
			repo.updateIdea(1, v[nr].getText(), nr);
	}
	this->ui.listWidget->clear();
	this->afisare();
	

}

void screenWritter::handleDevelop()
{
	std::vector<Idea>v = repo.returnIdeas();
	std::vector<Idea>accept;
	for (auto i : v)
	{
		if (i.getProposer() == writter.getName())
			if (i.getStatus() == 1)
				accept.push_back(i);

	}
	std::string stat;
	stat = "accepted";
	this->ui.listWidget->clear();
	for (auto i : accept)
	{
		std::string print = stat + ", " + i.getText() + ", " + std::to_string(i.getAct()) + ", " + i.getProposer();
		new QListWidgetItem(print.c_str(), this->ui.listWidget);
	}
}

void screenWritter::handleSave()
{

}
screenWritter::screenWritter(Repo& repos, Writter w, QWidget *parent)
	: QMainWindow(parent), repo(repos),writter(w)
{
	ui.setupUi(this);
	this->afisare();
	connect(ui.addButton, SIGNAL(clicked()), this, SLOT(handleAdd()));
	connect(ui.reviseButton, SIGNAL(clicked()), this, SLOT(handleRevise()));
	connect(ui.developButton, SIGNAL(clicked()), this, SLOT(handleDevelop()));
	connect(ui.saveButton, SIGNAL(clicked()), this, SLOT(handleSave()));
}
