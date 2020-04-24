#include "codeReview.h"
#include <vector>
#include <qmessagebox.h>

bool cmp(Code a, Code b)
{
	return a.getName() < b.getName();
}
void codeReview::afisare()
{
	ui.listWidget->clear();
	std::string x;
	std::vector<Code> v = repo.returnCode();
	sort(v.begin(), v.end(), cmp);
	for (auto i : v)
	{
		if (i.getStatus() == 0)
		{
			x = "not_revised";
		}
		else
			x = "revised";
		
			//ui.listWidget.
		std::string print = i.getName() + " " + x + " " + i.getCreator() + " " + i.getReviewer();
		QListWidgetItem* p=new QListWidgetItem(print.c_str(), this->ui.listWidget);
		if (i.colour == 1) p->setBackgroundColor(Qt::green);
	}

}

void codeReview::handleAdd()
{
	std::string code;
	int ok = 1;
	std::vector < Code >v = repo.returnCode();
	code = ui.lineEdit->text().toStdString();
	if (code == "")
	{
		QMessageBox q;
		q.critical(0, "ERROR", "Complete!");
		ok = 2;
	}
	else
	{
		for (auto i : v)
		{
			if (i.getName() == code)
				ok = 0;
		}
	}
	if (ok==0)
	{
		QMessageBox q2;
		q2.critical(0, "ERROR", "Exists");
	}
	else
	{
		if (ok == 1)
		{
			repo.addCode(code, 0, programmer.getName(), "none");
			ui.listWidget->clear();
			this->afisare();
		}
	}

}
	
void codeReview::handleSELECT()
{
	int nr = ui.listWidget->currentIndex().row();
	std::vector<Code> v = repo.returnCode();
	sort(v.begin(), v.end(), cmp);
	if (v[nr].getCreator() == programmer.getName() || v[nr].getStatus() == 1)
		ui.revisButton->setDisabled(true);
	else
		ui.revisButton->setEnabled(true);
}

void codeReview::handleRevise()
{
	std::vector<Code> v = repo.returnCode();
	sort(v.begin(), v.end(), cmp);
	int nr = ui.listWidget->currentIndex().row();
	repo.updateCode(programmer.getName(), 1, v[nr].getName());
	//ui.listWidget->currentItem()->setBackgroundColor(Qt::green);
	//ui.listWidget->currentRow()->setBackgroundColor(QColor(Qt::green));
	
	ui.listWidget->clear();
	this->afisare();
	programmer.setRevised(programmer.getRevised() + 1);
	std::string done = "Done: " + std::to_string(programmer.getRevised());
	std::string total = "Left: " + std::to_string(programmer.getTotal() - programmer.getRevised());
	ui.labelDone->setText(done.c_str());
	ui.labelLeft->setText(total.c_str());
	if (programmer.getRevised() == programmer.getTotal())
	{
		QMessageBox o;
		o.information(0,"good job","CONGRATULATIONS!");
	}

	
}



codeReview::codeReview(Repo& repos, Programmer p, QWidget *parent)
	: QMainWindow(parent),repo(repos),programmer(p)
{
	ui.setupUi(this);
	this->afisare();
	//ui.labelDone.setText(programmer.getTotal().c_str());
	std::string lable = "DONE: " + std::to_string(programmer.getRevised());
	ui.labelDone->setText(lable.c_str());
	lable = "Left: " + std::to_string(programmer.getTotal() - programmer.getRevised());
	ui.labelLeft->setText(lable.c_str());
	connect(ui.addButton, SIGNAL(clicked()), this, SLOT(handleAdd()));
	//connect(ui.selectButton, SIGNAL(clicked()), this, SLOT(handleSELECT));
	connect(ui.selectButton, SIGNAL(clicked()), this, SLOT(handleSELECT()));
	connect(ui.revisButton, SIGNAL(clicked()), this, SLOT(handleRevise()));

}

