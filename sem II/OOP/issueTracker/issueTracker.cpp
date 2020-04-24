#include "issueTracker.h"
#include "qmessagebox.h"
bool cmp(Problem a, Problem b)
{
	if (a.getStatus() == b.getStatus())
		return a.getText() < b.getText();

	return a.getStatus() > b.getStatus();
}
void issueTracker::afisare()
{
	std::vector<Problem> problm = repo.returnProblems();
	ui.listWidget->clear();
	sort(problm.begin(), problm.end(), cmp);
	for (auto i : problm)
	{
		std::string print = i.getText() + ", " + i.getStatus() + ", " + i.getReporter() + ", " + i.getSolver();
		new QListWidgetItem(print.c_str(), ui.listWidget);
	}
}

void issueTracker::handleAdd()
{
	std::string text;
	int ok = 1;
	std::vector<Problem> p=repo.returnProblems();
	text = ui.lineEdit->text().toStdString();
	if (user.getType() == "tester")
	{
		if (text == "")
		{
			QMessageBox q;
			q.critical(0, "ERROR", "You must write the issue.");
			ok = 2;
		}
		else
		{
			for (auto i : p)
			{
				if (i.getText() == text)
				{
					ok = 0;
				}
				
			}
		}
	}
	else
	{
		ok = -1;
	}

	if (ok == 0)
	{
		QMessageBox k;
		k.critical(0, "ERROR", "Already exists");
	}
	if (ok == -1)
	{
		QMessageBox j;
		j.critical(0, "ERROR", "You are not a tester");
	}
	if (ok == 1)
		repo.addProblem(text, "open", user.getName(), "none");

	this->afisare();
}

void issueTracker::handleRemove()
{
	int nr = ui.listWidget->currentIndex().row();
	std::vector<Problem> v = repo.returnProblems();
	sort(v.begin(), v.end(), cmp);
	if (v[nr].getStatus() == "close")
	{
		repo.removeProblem(v[nr].getText());
	}
	this->afisare();
}

void issueTracker::handleSelect(QListWidgetItem* h)
{
	int nr = ui.listWidget->currentIndex().row();
	std::vector<Problem> p = repo.returnProblems();
	sort(p.begin(), p.end(), cmp);
	if (p[nr].getStatus() == "open" && user.getType() == "programmer")
		ui.resolveButton->setEnabled(true);
	else
		ui.resolveButton->setDisabled(true);
}
void issueTracker::handleResolve()
{
	int nr = ui.listWidget->currentIndex().row();
	std::vector<Problem> p = repo.returnProblems();
	sort(p.begin(), p.end(), cmp);
	repo.updateProblem(p[nr].getText(), user.getName());
	this->afisare();

}

issueTracker::issueTracker(Repo& r, User u, QWidget *parent)
	: QMainWindow(parent),repo(r),user(u)
{
	ui.setupUi(this);
	this->afisare();

	connect(ui.addButton, SIGNAL(clicked()), this, SLOT(handleAdd()));
	connect(ui.removeButton, SIGNAL(clicked()), this, SLOT(handleRemove()));
	connect(ui.listWidget, SIGNAL(itemClicked(QListWidgetItem*)), this, SLOT(handleSelect(QListWidgetItem*)));
	connect(ui.resolveButton, SIGNAL(clicked()), this, SLOT(handleResolve()));
}
