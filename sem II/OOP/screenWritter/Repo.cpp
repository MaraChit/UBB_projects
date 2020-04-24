#include "Repo.h"
#include <fstream>
#include <string>


void Repo::addIdea(int status, std::string text, int act, std::string proposer)
{
	this->ideeas.push_back(Idea(status, text, act, proposer));
}


void Repo::readData()
{
	std::ifstream fin("ideeas.txt");
	std::string rand;
	int status, act;
	std::string text, proposer;
	std::getline(fin, rand, '#');
	int count = 0;
	count++;
	while (rand != "")
	{
		if (count == 1)
			status = stoi(rand);
		if (count == 2)
			text = rand;
		if (count == 3)
			act = stoi(rand);
		if (count == 4)
		{
			count = 0;
			proposer = rand;
			getline(fin, rand);
			this->addIdea(status, text, act, proposer);

		}

		getline(fin, rand, '#');
		count++;

	}

	std::ifstream gin("writters.txt");
	std::string rank, name;
	while (gin >> rank && gin >> name)
	{
		this->writters.push_back(Writter(name, rank));
	}
}



Repo::Repo()
{
	this->readData();
}


Repo::~Repo()
{
}
