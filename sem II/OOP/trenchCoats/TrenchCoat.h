//
// Created by Ioana on 07.04.2019.
//

#ifndef TRENCHCOATS_TRENCHCOAT_H
#define TRENCHCOATS_TRENCHCOAT_H

#include <string>
#include <vector>

using namespace std;

class TrenchCoat {
private:
	string size;
	int price;
	string name;
	string photo;

public:

	//trench& operator=(trench& otherTrench);
	//trench read write operators overload
	friend std::istream& operator>>(std::istream& is, TrenchCoat& trenchRead);
	friend std::ostream& operator<<(std::ostream& os, TrenchCoat trenchWrite);

	TrenchCoat(string name_trench, string size_trench, string photo_trench, int price_trench)
	{
		this->name = name_trench;
		this->price = price_trench;
		this->size = size_trench;
		this->photo = photo_trench;
	}

	TrenchCoat()
	{
		this->name = "";
		this->price = 0;
		this->size = "";
		this->photo = "";
	}

	~TrenchCoat() {}

	string getName()
	{
		return this->name;
	}

	void setName(string newName)
	{
		this->name = newName;
	}

	int getPrice()
	{
		return this->price;
	}

	void setPrice(int newPrice)
	{
		this->price = newPrice;
	}

	string getSize()
	{
		return this->size;
	}

	void setSize(string newSize)
	{
		this->size = newSize;
	}

	string getPhoto()
	{
		return this->photo;
	}

	void setPhoto(string newPhoto)
	{
		this->photo = newPhoto;
	}

};

vector<string> tokenize(string str, char delimiter);
#endif //TRENCHCOATS_TRENCHCOAT_H
