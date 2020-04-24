#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_issueTracker.h"
#include "Repo.h"
#include "Observer.h"

class issueTracker : public QMainWindow, public Observer
{
	Q_OBJECT

public:
	issueTracker(Repo& r, User u, QWidget *parent = Q_NULLPTR);
	void afisare();
	void update() override
	{
		this->afisare();
	}

private:
	Ui::issueTrackerClass ui;
	Repo& repo;
	User user;

private slots:
	void handleAdd();
	void handleRemove();
	void handleSelect(QListWidgetItem* h);
	void handleResolve();
};
