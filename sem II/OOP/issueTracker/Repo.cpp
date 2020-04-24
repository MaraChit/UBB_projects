#include "Repo.h"
#include <fstream>


Repo::Repo()
{
	std::ifstream fin("issues.txt");
	std::string text, status, reporter, solver, rand;
	getline(fin, rand, '#');
	int count = 0;
	count++;
	while (rand != "")
	{
		if (count == 1)
			text = rand;
		if (count == 2)
			status = rand;
		if (count == 3)
			reporter = rand;
		if (count == 4)
		{
			solver = rand;
			count = 0;
			this->addProblem(text, status, reporter, solver);
			getline(fin, rand);
		}

		getline(fin, rand, '#');
		count++;
	}

	std::ifstream gin("users.txt");
	std::string name, type, r;
	int cnt = 0;
	getline(gin, r, '#');
	cnt++;
	while (r != "")
	{
		if (cnt == 1)
			name = r;
		if (cnt == 2)
		{
			type = r;
			cnt = 0;
			this->addUser(name, type);
			getline(gin, r);
		}

		getline(gin, r, '#');
		cnt++;
	}
}


Repo::~Repo()
{
}
