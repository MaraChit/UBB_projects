//
// Created by Ioana on 17.05.2019.
//

#ifndef MARA_TES_USER_REPO_H
#define MARA_TES_USER_REPO_H


#include <vector>
#include "TrenchCoat.h"

class user_repo {
private:
	std::vector<TrenchCoat> storage;
	std::string filelocation = "";
	void saveFile();
	void saveHTML();

public:
	user_repo() {}

	bool addTrench(TrenchCoat& newTrench);
	void setFileLocation(std::string fileLocation)
	{
		this->filelocation = fileLocation;
	}
	std::vector<TrenchCoat> getTrench()
	{
		return this->storage;
	}

};


#endif //MARA_TES_USER_REPO_H
