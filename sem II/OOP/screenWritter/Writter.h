#pragma once
#include <string>
class Writter
{
private:
	std::string name;
	std::string rank;
public:
	Writter(std::string _name, std::string _rank) :name(_name), rank(_rank) {}
	std::string getName()
	{
		return this->name;
	}
	std::string getRank()
	{
		return this->rank;
	}

	~Writter() {}
};

