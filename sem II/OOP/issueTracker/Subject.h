#pragma once
#include "Observer.h"
#include <vector>
class Subject
{
private:
	std::vector<Observer*>obs;
public:
	Subject(){}
	void addObserver(Observer* o)
	{
		obs.push_back(o);
	}
	void notify()
	{
		for (auto i : obs)
			i->update();
	}
	~Subject(){}
};

