#pragma once
#include <string>
class Task
{
	std::string description;
	int id, status;
public:
	Task(int _id, int _status, std::string _description): id(_id),status(_status),description(_description){}
	std::string getDescription()
	{
		return this->description;
	}
	std::string getStatus()
	{
		std::string option[] = {"open", "in progress", "closed"};
		return option[status];
		
	}
	int getIdTask()
	{
		return this->id;
	}

	void setStatus(int statusNew)
	{
		this->status = statusNew;
	}

	void setIdTask(int newId)
	{
		this->id = newId;
	}
	~Task(){}
};

