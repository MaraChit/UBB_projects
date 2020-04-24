#pragma once
#include<string>

class User
{
private:
	std::string name;
	std::string type;

public:
	User(std::string n, std::string t):name(n),type(t){}
	std::string getName() { return this->name; }
	std::string getType() { return this->type; }
	~User(){}
};

