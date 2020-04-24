#pragma once
#include <qwidget.h>
#include <qpushbutton.h>
#include <qboxlayout.h>
#include <qlineedit.h>
#include <qlabel.h>
#include <qlistwidget.h>
#include "controller.h"

class guiBuyer: public QWidget
{
	Q_OBJECT
public:
	guiBuyer(controller control, user_repo trench_for_user, QWidget *parent=0);
	~guiBuyer();

private:
	controller controllerTrench;
	user_repo trenchCoatBuyerRepo;

	QPushButton *next;
	QPushButton *save;
	QPushButton *mylist;
	QPushButton *list;

	QLabel *nextLabel;
	QLabel *sizeLabel;
	QLabel *priceLabel;
	QLabel *saveLabel;

	QLineEdit *sizeInput;
	QLineEdit *priceInput;
	QLineEdit *saveInput;
	
	QGridLayout *mainLayout;
	QListWidget *trenchList;

	void clear();

	int trenchCounter = 0;

private slots:
	void handleNext();
	void handleSave();
	void handleMylist();
	void handleList();
};