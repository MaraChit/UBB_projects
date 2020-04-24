#pragma once
#include <qwidget.h>
#include <qpushbutton.h>
#include <qboxlayout.h>
#include <qlabel.h>
#include <qlineedit.h>
#include <qlistwidget.h>
#include "controller.h"


class guiAdministrator :public QWidget
{
	Q_OBJECT

public:
	guiAdministrator(controller control, QWidget *parent=0);
	~guiAdministrator();

private:
	controller controllerTrench;

	QPushButton *add;
	QPushButton *deletee;
	QPushButton *update;
	QPushButton *list;
	QPushButton *undo;
	QPushButton *redo;

	QLineEdit *nameInput;
	QLineEdit *sizeInput;
	QLineEdit *priceInput;
	QLineEdit *photoInput;

	QLabel *name;
	QLabel *size;
	QLabel *price;
	QLabel *photo;

	QGridLayout *mainLayout;
	QListWidget *trenchList;

	void clear();

private slots:
	void handleAdd();
	void handleDelete();
	void handleUpdate();
	void handleList();
	void handleUndo();
	void handleRedo();

};

