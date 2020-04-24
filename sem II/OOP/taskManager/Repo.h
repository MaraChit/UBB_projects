#pragma once
#include "Programmer.h"
#include <vector>
#include "Task.h"
#include "Subject.h"

class Repo: public Subject
{
private:
	//std::vector<Programmer> programmers;
	std::vector<Task> tasks;

public:
	Repo();
	~Repo();
	void readData();
	void saveData();
	void addTask(int id, int status, std::string description)
	{
		this->tasks.push_back(Task(id, status, description));
		this->notify();
	}
	void removeTask(int poz)
	{
		this->tasks.erase(tasks.begin() + poz);
		this->notify();
	}
	std::vector<Task> returnTasks()
	{
		return this->tasks;
	}
	void seteazaProstii(int poz, int status, int id)
	{
		this->tasks[poz].setIdTask(id);
		this->tasks[poz].setStatus(status);
		this->notify();
	}



};

