#pragma once
#include "Observer.h"
#include <vector>
class Subject
{
private:
	std::vector<Observer*> observers;

public:
	Subject(){}
	void notify() {
		for (auto i : observers)
			i->update();
	}
	void addObserver(Observer* o) {
		observers.push_back(o);
	}
	~Subject() {}
};

