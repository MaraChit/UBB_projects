//
// Created by Ioana on 17.05.2019.
//

#include "user_repo.h"
#include <iostream>
#include <fstream>
using namespace std;

bool user_repo::addTrench(TrenchCoat &newTrench) {
	this->storage.push_back(newTrench);
	this->saveFile();
	return true;
}

void user_repo::saveFile()
{
	//cout<<1<<endl;
	if (this->filelocation.size() > 2) {

		//cout<<2<<endl;

		std::size_t found = this->filelocation.find(".html", this->filelocation.size() - 5);
		if (found != std::string::npos)
			this->saveHTML();
		else
		{
			std::ofstream file;
			file.open(this->filelocation, std::ios::out);
			for (int index = 0; index < this->storage.size(); index++)
				file << this->storage[index];

			file.close();
		}
	}
}

void user_repo::saveHTML()
{
	std::ofstream file;
	//cout<<this->filelocation<<" "<<this->storage.size();
	file.open(this->filelocation, std::ios_base::out);
	file << "<!DOCTYPE html>\n<html>\n<head>\n<title>Trenches</title>\n</head>\n<body>\n<table border=\"1\">\n";
	file << "<tr>\n<td>Name</td>\n"
		"<td>Size</td>\n"
		"<td>Price</td>\n"
		"<td>Photo</td>\n"
		"</tr>\n";
	for (auto& trench : this->storage) {
		file << "tr\n" << "<td>" << trench.getName() << "</td>\n"
			<< "<td>" << trench.getSize() << "</td>\n"
			<< "<td>" << trench.getPrice() << "</td>\n"
			<< "<td><a href=" << '"' << trench.getPhoto() << '"' << ">Link</a></td>\n" << "</tr>\n";
	}
	file << "</tr>\n"
		"</table>\n"
		"</body>\n"
		"</html>";
	file.close();
}