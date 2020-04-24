//
// Created by Ioana on 07.04.2019.
//

#include "TrenchCoatRepo.h"
#include "iostream"
#include <fstream>

void TrenchCoatRepo::addTrench(int price, string name, string photo, string size)
{
	this->trench_coat.push_back(TrenchCoat(name, size, photo, price));
	this->number_of_trench_coats += 1;
}

void TrenchCoatRepo::updateTrench(int price, string name, string photo, string size)
{
	int i;//ok=0;
	//for (i = 0; i < this->number_of_trench_coats; i++)
	for(i=0;i<this->trench_coat.size();i++)
		//if (this->trench_coat.getElement(i).getName()==name)
		if (this->trench_coat[i].getName() == name)
		{
			/*  this->trench_coat.getElement(i).setSize(size);
			  this->trench_coat.getElement(i).setPhoto(photo);//
			  this->trench_coat.getElement(i).setPrice(price);*/

			this->trench_coat[i].setSize(size);
			this->trench_coat[i].setPhoto(photo);//
			this->trench_coat[i].setPrice(price);
			//ok=1;
		}

	//if(ok==0)
		//throw repository_exception("It can not be updated. Trench coat does not exist");
}

void TrenchCoatRepo::deleteTrench(string name) {
	/*int i;
	for (i=0;i<this->number_of_trench_coats;i++)
		if(this->trench_coat[i].getName()==name) {
			this->trench_coat.removeElement(i);
			this->number_of_trench_coats--;
			break;
		}*/
		//int ok=0;
	for (auto it = this->trench_coat.begin(); it != this->trench_coat.end(); it++)
		if (name == (*it).getName()) {
			this->trench_coat.erase(it);
			this->number_of_trench_coats--;
			//ok=1;
			break;
		}

	/*if (ok==0)
		throw repository_exception("Can't delete trench coat; it doesn't exist.");
*/
}

std::vector<TrenchCoat> TrenchCoatRepo::listTrench()
{
	return this->trench_coat;

}

void TrenchCoatRepo::setFileLocation(std::string & filename)
{
	this->file = filename;
}
void TrenchCoatRepo::readFromFile()
{
	ifstream filein{ this->file };

	TrenchCoat newTrench;
	//cout<<1;
	while (filein >> newTrench)
	{
		this->trench_coat.push_back(newTrench);
		//cout<<newTrench.getPhoto();
	}
	//cout<<2;
	filein.close();

}
void TrenchCoatRepo::saveFile()
{
	ofstream fileout{ this->file };

	for (auto& Trench : this->trench_coat)
	{
		fileout << Trench;
	}

	fileout.close();
}




