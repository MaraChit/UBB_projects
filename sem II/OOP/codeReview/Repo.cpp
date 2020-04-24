#include "Repo.h"
#include <fstream>

void Repo::readDate()
{
	std::ifstream fin("codes.txt");
	int status;
	std::string name, creator, reviewer, rand;
	getline(fin, rand, '#');
	int count = 0;
	count++;
	while (rand != "")
	{
		if (count == 1)
			name = rand;
		if (count == 2)
			status = stoi(rand);
		if (count == 3)
			creator = rand;
		if (count == 4)
		{
			count = 0;
			reviewer = rand;
			this->addCode(name, status, creator, reviewer);
			getline(fin, rand);
			//this->addCode(name, status, creator, reviewer);
		}

		getline(fin, rand, '#');
		count++;

	}
		std::ifstream gin("programmers.txt");
		int total, revised;
		std::string name2, r;
		/*int cnt = 0;
		getline(gin, r, '#');
		cnt++;
		while (r != "")
		{
			if (cnt == 1)
				name2 = r;
			if (cnt == 2)
				total = stoi(r);
			if (cnt == 3)
			{
				revised = stoi(r);
				cnt = 0;
				this->addProgrammer(name2, total, revised);
				getline(gin, r);
			}

			getline(gin, r, '#');
			cnt++;

		}*/
		while (gin >> name2 && gin >> total && gin >> revised)
		{
			this->addProgrammer(name2, total, revised);
		}

	


}

Repo::Repo()
{
	this->readDate();
}


Repo::~Repo()
{
}
