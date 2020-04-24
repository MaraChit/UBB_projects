#pragma once
#include "Problem.h"
#include "User.h"
#include <vector>
#include "Subject.h"
class Repo: public Subject
{
private:
	std::vector<Problem> problems;
	std::vector<User> users;

public:
	Repo();
	std::vector<Problem> returnProblems() { return this->problems; }
	std::vector<User> returnUsers() { return this->users; }

	//input: string name, string status, string reporter, string solver
	//output: none
	// adds a new issue in the vector of issues
	void addProblem(std::string t, std::string s, std::string re, std::string so)
	{
		this->problems.push_back(Problem(t, s, re, so));
		this->notify();
	}

	//input: string text_of_the_issue
	//outpu:none
	//function removes from the vector of issues the selected issue,given by its text
	void removeProblem(std::string text)
	{
		int i;
		for (i = 0; i < problems.size(); i++)
		{
			if (problems[i].getText() == text)
				this->problems.erase(problems.begin() + i);
		}
		this->notify();

	}

	//input: string text_of_the_issue, string name_of_solver
	//output:none
	//function updates the issue given by its text, modifying its status to "close" and adding the name of the solver
	void updateProblem(std::string text, std::string name)
	{
		int i;
		for(i=0;i<problems.size();i++)
			if (problems[i].getText() == text)
			{
				problems[i].setStatus("close");
				problems[i].setSolver(name);
			}
		this->notify();
	}
	void addUser(std::string name, std::string type)
	{
		this->users.push_back(User(name, type));
	}
	~Repo();
};

