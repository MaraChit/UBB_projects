#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_codeReview.h"
#include "Repo.h"
#include "Observer.h"

class codeReview : public QMainWindow, public Observer
{
	Q_OBJECT

public:
	codeReview(Repo& repos, Programmer p, QWidget *parent = Q_NULLPTR);
	void afisare();
	void update() override
	{
		this->afisare();
	}

private:
	Ui::codeReviewClass ui;
		Repo& repo;
	Programmer programmer;

private slots:
	void handleAdd();
	void handleSELECT();
	void handleRevise();
};
