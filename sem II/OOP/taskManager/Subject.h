#pragma once
#include<vector>
#include "Observer.h"

class Subject
{
private:
	std::vector<Observer*> observers;
public:
	Subject();

	void addObs(Observer* obs)
	{
		observers.push_back(obs);
	}

	void notify()
	{
		for (auto o : observers)
			o->update();
	}

	~Subject();
};

