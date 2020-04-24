//
// Created by Ioana on 07.04.2019.
//

#ifndef TRENCHCOATS_TRENCHCOATREPO_H
#define TRENCHCOATS_TRENCHCOATREPO_H


#include "TrenchCoat.h"
#include <vector>


class repository_exception :public std::runtime_error
{
public:
	repository_exception(std::string error) :std::runtime_error(("repositoryException: " + error + '\n')) {}

};


class TrenchCoatRepo {
private:
	//DynamicArray<TrenchCoat> trench_coat;
	std::vector<TrenchCoat> trench_coat;
	std::string file;
	int number_of_trench_coats;

public:
	TrenchCoatRepo()
	{
		this->number_of_trench_coats = 0;
	}

	~TrenchCoatRepo()
	{
		//delete this->trench_coat;
	}

	void addTrench(int price, string name, string photo, string size);
	std::vector<TrenchCoat> listTrench();
	virtual void updateTrench(int price, string name, string photo, string size);
	void deleteTrench(string name);
	void setFileLocation(std::string& filename);
	//void -it reads from the file
	void readFromFile();
	//void - it saves to the file
	void saveFile();
	std::vector<TrenchCoat> getTrench()
	{
		return this->trench_coat;
	}
	int getNumberOfTrenches()
	{
		return this->number_of_trench_coats;
	}
};


#endif //TRENCHCOATS_TRENCHCOATREPO_H
