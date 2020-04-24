#include "Repo.h"
#include <fstream>

void Repo::readData()
{

	std::ifstream gin("tasks.txt");
	std::string description;
	int status, _id;
	std::string rand;
	int count = 0;
	std::getline(gin, rand, '#');
	count++;
	while (rand != "")
	{
		if (count == 1)
			_id = stoi(rand);

		if (count == 2)
		{
			status = stoi(rand);
			if (status == 0)
				_id = -1;
		}

		if (count == 3)
		{
			description = rand;
			count = 0;
			this->addTask(_id, status, description);
			std::getline(gin, rand);
		}

		std::getline(gin, rand, '#');
		count++;

	}

}

void Repo::saveData()
{
	std::ofstream gout("tasks.txt");
	for (auto i : this->tasks)
		gout << i.getIdTask()<< " " << i.getStatus()<< " " << i.getDescription() << "\n";

}

Repo::Repo()
{
	this->readData();
}


Repo::~Repo()
{
	this->saveData();
}
