#pragma once
#include <string>
class Programmer
{
private:
	std::string name;
	int total, revised;
	
public:
	Programmer(std::string _name, int _total, int _revised):name(_name),total(_total),revised(_revised){}
	std::string getName()
	{
		return this->name;
	}
	int getTotal()
	{
		return this->total;
	}
	int getRevised()
	{
		return this->revised;
	}
	void setRevised(int x)
	{
		this->revised = x;
	}
	~Programmer(){}
};

