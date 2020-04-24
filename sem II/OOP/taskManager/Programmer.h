#pragma once
#include <string>
class Programmer
{
private:
	int id;
	std::string name;
public:
	Programmer(int _id, std::string _name):id(_id),name(_name){}

	int getId()
	{
		return this->id;
	}

	std::string getName()
	{
		return this->name;
	}

	~Programmer(){}
};

