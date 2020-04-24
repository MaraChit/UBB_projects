#pragma once
#include <vector>
#include "Code.h"
#include "Programmer.h"
#include "Subject.h"

class Repo : public Subject
{
private:
	std::vector<Code>codes;
	std::vector<Programmer>programmers;
public:
	Repo();
	std::vector<Code>returnCode() { return this->codes;}
	std::vector<Programmer>returnProgrammer() { return this->programmers; }
	void readDate();
	void addCode(std::string name, int status, std::string c, std::string r)
	{
		this->codes.push_back(Code(name, status, c, r));
		this->notify();
	}
	void addProgrammer(std::string x, int total, int left)
	{
		this->programmers.push_back(Programmer(x, total, left));
		
	}
	void updateCode(std::string name, int status, std::string code)
	{
		for (auto& i : codes)
		{
			if (i.getName() == code)
			{
				i.setReviewer(name);
				i.setStatus(status);
				i.colour = 1;
			}
		}

		this->notify();
	}
	~Repo();
};

