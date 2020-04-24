#include "guiAdministrator.h"
#include <cstring>


guiAdministrator::guiAdministrator(controller control, QWidget *parent) :QWidget(parent),controllerTrench(control)
{
	//layout
	this->mainLayout = new QGridLayout();
	this->setLayout(this->mainLayout);
	
	//buttons
	this->add = new QPushButton("ADD", this);
	this->mainLayout->addWidget(this->add, 1, 1);
	connect(this->add, SIGNAL(clicked()), this, SLOT(handleAdd()));

	this->deletee = new QPushButton("DELETE", this);
	this->mainLayout->addWidget(this->deletee, 1, 2);
	connect(this->deletee, SIGNAL(clicked()), this, SLOT(handleDelete()));

	this->update = new QPushButton("UPDATE", this);
	this->mainLayout->addWidget(this->update, 1, 3);
	connect(this->update, SIGNAL(clicked()), this, SLOT(handleUpdate()));

	this->list = new QPushButton("LIST", this);
	this->mainLayout->addWidget(this->list, 3, 4);
	connect(this->list, SIGNAL(clicked()), this, SLOT(handleList()));

	this->undo = new QPushButton("UNDO", this);
	this->undo->setShortcut(QKeySequence("Ctrl+z"));
	this->mainLayout->addWidget(this->undo, 1, 4);
	connect(this->undo, SIGNAL(clicked()), this, SLOT(handleUndo()));

	this->redo = new QPushButton("REDO", this);
	this->redo->setShortcut(QKeySequence("Ctrl+y"));
	this->mainLayout->addWidget(this->redo, 5, 4);
	connect(this->redo, SIGNAL(clicked()), this, SLOT(handleRedo()));

	//labels && line edits
	this->name = new QLabel;
	this->nameInput = new QLineEdit;
	this->name->setText("&Name");
	this->name->setBuddy(this->nameInput);  
	this->mainLayout->addWidget(this->name, 2, 1);
	this->mainLayout->addWidget(this->nameInput, 2, 2, 1, 2);

	this->size = new QLabel;
	this->sizeInput = new QLineEdit;
	this->size->setText("&Size");
	this->size->setBuddy(this->sizeInput);
	this->mainLayout->addWidget(this->size, 3, 1);
	this->mainLayout->addWidget(this->sizeInput, 3, 2, 1, 2);

	this->price = new QLabel;
	this->priceInput = new QLineEdit;
	this->price->setText("&Price");
	this->price->setBuddy(this->priceInput);
	this->mainLayout->addWidget(this->price, 4, 1);
	this->mainLayout->addWidget(this->priceInput, 4, 2, 1, 2);

	this->photo = new QLabel;
	this->photoInput = new QLineEdit;
	this->photo->setText("&Photo");
	this->photo->setBuddy(this->photoInput);
	this->mainLayout->addWidget(this->photo, 5, 1);
	this->mainLayout->addWidget(this->photoInput, 5, 2, 1, 2);

	//list widget
	this->trenchList = new QListWidget();
	this->mainLayout->addWidget(this->trenchList, 1, 5, 5, 3);

}


guiAdministrator::~guiAdministrator()
{
}

void guiAdministrator::handleAdd()
{
	std::string name = this->nameInput->text().toUtf8().constData();
	std::string size = this->sizeInput->text().toUtf8().constData();
	std::string price = this->priceInput->text().toUtf8().constData();
	std::string photo = this->photoInput->text().toUtf8().constData();

	this->controllerTrench.addTrenchController(size, photo, name, stoi(price));
	this->clear();
}
void guiAdministrator::handleDelete()
{
	std::string name = this->nameInput->text().toUtf8().constData();
	this->controllerTrench.deleteTrenchController(name);
	this->clear();
}
void guiAdministrator::handleUpdate()
{
	std::string name = this->nameInput->text().toUtf8().constData();
	std::string size = this->sizeInput->text().toUtf8().constData();
	std::string price = this->priceInput->text().toUtf8().constData();
	std::string photo = this->photoInput->text().toUtf8().constData();
	
	this->controllerTrench.updateTrenchController(size, photo, name, stoi(price));
	this->clear();
}
void guiAdministrator::handleList()
{
	this->trenchList->clear();
	vector<TrenchCoat> trenches_for_print = this->controllerTrench.listTrenchController();
	for (auto trench : trenches_for_print)
	{
		string listTrench = trench.getName() + ", " + trench.getSize() + ", " + to_string(trench.getPrice()) + ", " + trench.getPhoto();
		new QListWidgetItem(listTrench.c_str(), this->trenchList);
		this->clear();
	}
}

void guiAdministrator::handleUndo() {

	this->controllerTrench.undo();
	this->handleList();
}

void guiAdministrator::handleRedo() {

	this->controllerTrench.redo();
	this->handleList();
}

void guiAdministrator::clear()
{
	this->nameInput->clear();
	this->sizeInput->clear();
	this->priceInput->clear();
	this->photoInput->clear();
}