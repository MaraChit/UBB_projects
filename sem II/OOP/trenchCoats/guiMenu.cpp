#include "guiMenu.h"

guiMenu::guiMenu(controller control,user_repo repo_user, QWidget *parent): QWidget(parent),controllerTrench(control),repoUser(repo_user)
{
	//layout
	this->mainLayout = new QVBoxLayout();
	this->setLayout(this->mainLayout);

	//buttons
	this->modeA = new QPushButton("Mode Administrator", this);
	this->mainLayout->addWidget(this->modeA);
	connect(this->modeA, SIGNAL(clicked()), this, SLOT(handleA()));

	this->modeB = new QPushButton("Mode Buyer", this);
	this->mainLayout->addWidget(this->modeB);
	connect(this->modeB, SIGNAL(clicked()), this, SLOT(handleB()));	

}

void guiMenu::handleA()
{
	this->gui_administrator = new guiAdministrator(this->controllerTrench);
	this->gui_administrator->show();
}

void guiMenu::handleB()
{
	this->guy_buyer = new guiBuyer(this->controllerTrench,repoUser);
	this->guy_buyer->show();
}


 


guiMenu::~guiMenu(){}


