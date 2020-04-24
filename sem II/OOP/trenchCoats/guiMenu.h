#pragma once
#include <qwidget.h>
#include <qpushbutton.h>
#include <qboxlayout.h>
#include "guiAdministrator.h"
#include "guiBuyer.h"
#include  "controller.h"


class guiMenu :public QWidget
{
	Q_OBJECT

public:
	guiMenu(controller control, user_repo repo_user, QWidget *parent=0);
	~guiMenu();

private:
	QPushButton *modeA;
	QPushButton *modeB;
	QVBoxLayout *mainLayout;
	guiAdministrator *gui_administrator;
	controller controllerTrench;
	user_repo repoUser;
	guiBuyer *guy_buyer;

private slots:
	void handleA();
	void handleB();

};

