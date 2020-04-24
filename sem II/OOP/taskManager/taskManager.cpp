#include "taskManager.h"
#include <vector>
#include<qmessagebox.h>

bool cmp(Task a, Task b)
{
	return a.getStatus() > b.getStatus();
}

void taskManager::afisare()
{
	this->ui.TaskListWidget->clear();
	std::vector<Task> tasks = repo.returnTasks();
	std::sort(tasks.begin() + 0, tasks.begin() + tasks.size(), cmp);

	for (auto t : tasks)
	{
		std::string print;
		print = std::to_string(t.getIdTask()) + " " + t.getStatus() + " " + t.getDescription();
		new QListWidgetItem(print.c_str(), this->ui.TaskListWidget);

	}
}
void taskManager::handleAdd()
{
	std::string description = ui.descriptionLineEdit->text().toStdString();
	this->repo.addTask(-1, 0, description);
	this->afisare();
}

void taskManager::handleRemove()
{
	int nr = this->ui.TaskListWidget->currentIndex().row();
	this->repo.removeTask(nr);
	this->afisare();
}

void taskManager::handleStart()
{
	int nr = this->ui.TaskListWidget->currentIndex().row();
	std::vector<Task>vectorul = repo.returnTasks();
	if (vectorul[nr].getStatus() == "open")
	{
		this->repo.seteazaProstii(nr, 1, programmer.getId());
		this->afisare();
		// std::string print = std::to_string(vectorul[nr].getIdTask()) + " " + vectorul[nr].getStatus() + " " + vectorul[nr].getDescription() + " " + programmer.getName();
		//new QListWidgetItem(print.c_str(), this->ui.TaskListWidget);
	}
	else
	{
		QMessageBox q;
		q.critical(0, "ESTI PROST", "nu merge asa");
	}

}

void taskManager::handleDone()
{
	int nr = this->ui.TaskListWidget->currentIndex().row();
	std::vector<Task>v = repo.returnTasks();
	if (v[nr].getStatus() == "in progress" && v[nr].getIdTask()==programmer.getId())
	{
		this->repo.seteazaProstii(nr, 2, v[nr].getIdTask());
		this->afisare();
	}
	else
	{
		QMessageBox Q;
		Q.critical(0, "MNIU", "n-AI VOIE");
	}
	
}


taskManager::taskManager(Repo& repos, Programmer& p, QWidget *parent)
	: QMainWindow(parent),repo(repos),programmer(p)
{
	ui.setupUi(this);
	this->afisare();
	connect(ui.AddButton, SIGNAL(clicked()), this, SLOT(handleAdd()));
	connect(ui.removeButton, SIGNAL(clicked()), this, SLOT(handleRemove()));
	connect(ui.STARTButton, SIGNAL(clicked()), this, SLOT(handleStart()));
	connect(ui.doneButton, SIGNAL(clicked()), this, SLOT(handleDone()));
	//connect(this->ui.AddButton, SIGNAL(clicked()), this, SLOT(this->handleAdd()));
}
