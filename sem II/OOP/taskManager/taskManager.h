#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_taskManager.h"
#include "Repo.h"
#include "Observer.h"

class taskManager : public QMainWindow,public Observer
{
	Q_OBJECT

public:
	taskManager(Repo& repos,Programmer& p, QWidget *parent = Q_NULLPTR);
	

private:
	Ui::taskManagerClass ui;
	Repo& repo;
	Programmer programmer;
	void afisare();
	void update() override
	{
		this->afisare();
	}

private slots:
	void handleAdd();
	void handleRemove();
	void handleStart();
	void handleDone();

};
