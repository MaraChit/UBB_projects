#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_screenWritter.h"
#include "Repo.h"

class screenWritter : public QMainWindow
{
	Q_OBJECT

public:
	screenWritter(Repo& repos, Writter w,QWidget *parent = Q_NULLPTR);
	void afisare();

private:
	Ui::screenWritterClass ui;
	Repo& repo;
	Writter writter;



private slots:
	void handleAdd();
	void handleRevise();
	void handleDevelop();
	void handleSave();

};
