#pragma once
#include <string>
class Code
{
private:
	std::string name;
	int status;
	std::string creator;
	std::string reviewer;

public:
	Code(std::string _name,int _status, std::string _creator, std::string _reviwer):name(_name),status(_status),creator(_creator),reviewer(_reviwer){}
	int colour = 0;
	std::string getName()
	{
		return this->name;
	}
	std::string getCreator()
	{
		return this->creator;
	}
	std::string getReviewer()
	{
		return this->reviewer;
	}
	int getStatus()
	{
		return this->status;
	}
	void setStatus(int newStatus)
	{
		this->status = newStatus;
	}
	void setReviewer(std::string x)
	{
		this->reviewer = x;
	}
	~Code(){}
};

