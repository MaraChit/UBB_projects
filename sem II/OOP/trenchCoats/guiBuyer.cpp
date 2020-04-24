#include "guiBuyer.h"
#include "guiAdministrator.h"


guiBuyer::guiBuyer(controller control,user_repo trench_for_user, QWidget *parent):QWidget(parent), trenchCoatBuyerRepo(trench_for_user), controllerTrench(control)
{
	//layout
	this->mainLayout = new QGridLayout();
	this->setLayout(this->mainLayout);

	//buttons 
	this->next = new QPushButton("Next", this);
	this->mainLayout->addWidget(this->next, 1, 1);
	connect(this->next, SIGNAL(clicked()), this, SLOT(handleNext()));

	this->save = new QPushButton("Save", this);
	this->mainLayout->addWidget(this->save, 1, 2);
	connect(this->save, SIGNAL(clicked()), this, SLOT(handleSave()));

	this->mylist = new QPushButton("Mylist", this);
	this->mainLayout->addWidget(this->mylist, 1, 3);
	connect(this->mylist, SIGNAL(clicked()), this, SLOT(handleMylist()));

	this->list = new QPushButton("List", this);
	this->mainLayout->addWidget(this->list, 2, 2);
	connect(this->list, SIGNAL(clicked()), this, SLOT(handleList()));

	this->sizeInput = new QLineEdit;
	this->sizeLabel = new QLabel;
	this->sizeLabel->setText("&Size");
	this->sizeLabel->setBuddy(this->sizeInput);
	this->mainLayout->addWidget(this->sizeLabel, 3, 1);
	this->mainLayout->addWidget(this->sizeInput, 3, 2, 1, 2);

	this->priceInput = new QLineEdit;
	this->priceLabel = new QLabel;
	this->priceLabel->setText("&Price");
	this->priceLabel->setBuddy(this->priceInput);
	this->mainLayout->addWidget(this->priceLabel, 4, 1);
	this->mainLayout->addWidget(this->priceInput, 4, 2, 1, 2);

	this->saveInput = new QLineEdit;
	this->saveLabel = new QLabel;
	this->saveLabel->setText("&Trench name to save: ");
	this->saveLabel->setBuddy(this->saveInput);
	this->mainLayout->addWidget(this->saveLabel, 5, 1, 1, 2);
	this->mainLayout->addWidget(this->saveInput, 5, 3);

	this->nextLabel = new QLabel;
	this->nextLabel->setText("Next");
	this->mainLayout->addWidget(this->nextLabel, 6, 1);

	//listwidget
	this->trenchList = new QListWidget();
	this->mainLayout->addWidget(this->trenchList, 1, 4, 6, 3);

	this->trenchCounter = 0;
}


guiBuyer::~guiBuyer()
{
}

void guiBuyer::handleNext(){

	std::vector<TrenchCoat> buyerTrenches = this->controllerTrench.listTrenchController();
		if (buyerTrenches.size() > 0)
		{
			string toPrint = buyerTrenches[trenchCounter].getName() + ", " + buyerTrenches[trenchCounter].getSize() + ", " + to_string(buyerTrenches[trenchCounter].getPrice()) + ", " + buyerTrenches[trenchCounter].getPhoto();
			this->nextLabel->setText(toPrint.c_str());
			this->trenchCounter++;
			if (this->trenchCounter == buyerTrenches.size())
				this->trenchCounter = 0;
		}
		else
		{
			this->nextLabel->setText("No trench coats available");
		}

}

void guiBuyer::handleSave() {

	std::string name = this->saveInput->text().toUtf8().constData();
	std::vector<TrenchCoat> trenches = this->controllerTrench.listTrenchController();
	for (auto it = trenches.begin(); it != trenches.end(); it++)
		if (name == (*it).getName()) {
			trenchCoatBuyerRepo.addTrench(*it);
			
			break;
		}
	this->handleMylist();
	this->clear();

}
void guiBuyer::handleMylist() {
	
	this->trenchList->clear();
	new QListWidgetItem("Mylist", this->trenchList);
	std::vector<TrenchCoat> trenchesToList = trenchCoatBuyerRepo.getTrench();
	for (auto trench : trenchesToList)
	{
		std::string toPrint = trench.getName() + ", " + trench.getSize() + ", " + to_string(trench.getPrice()) + ", " + trench.getPhoto();
		new QListWidgetItem(toPrint.c_str(), this->trenchList);
		this->clear();

	}
}
void guiBuyer::handleList() {

	this->trenchList->clear();
	new QListWidgetItem("List", this->trenchList);
	std::string size = this->sizeInput->text().toUtf8().constData();
	//std::string price = this->priceInput->text().toUtf8().constData();
	int price = stoi(this->priceInput->text().toUtf8().constData());
	std::vector<TrenchCoat> trenchToList = controllerTrench.listTrenchController();
	for (auto trench : trenchToList)
	{
		if (trench.getSize() == size && trench.getPrice() < price)
		{
			std::string toPrint = trench.getName() + ", " + trench.getSize() + ", " + to_string(trench.getPrice()) + ", " + trench.getPhoto();
			new QListWidgetItem(toPrint.c_str(), this->trenchList);
			this->clear(); 
		}

	}
}

void guiBuyer::clear()
{
	this->sizeInput->clear();
	this->priceInput->clear();
	this->saveInput->clear();
}
