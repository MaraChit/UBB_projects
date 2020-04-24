//
// Created by Ioana on 07.04.2019.
//

#include "TrenchCoat.h"
#include <sstream>

/*
   Tokenizes a string.
   Input:	str - the string to be tokenized.
		   delimiter - char - the delimiter used for tokenization
   Output: a vector of strings, containing the tokens

	*/
vector<string> tokenize(string str, char delimiter)
{
	vector <string> result;
	stringstream ss(str);
	string token;
	while (getline(ss, token, delimiter))
		result.push_back(token);

	return result;
}

std::istream& operator>>(std::istream& is, TrenchCoat& s)
{
	string line;
	getline(is, line);

	vector<string> tokens = tokenize(line, ',');
	if (tokens.size() != 4)
		return is;

	s.setName(tokens[0]);
	s.setSize(tokens[1]);
	s.setPrice(stoi(tokens[2]));
	s.setPhoto(tokens[3]);

	return is;
}

std::ostream& operator<<(std::ostream & os, TrenchCoat s)//const movie
{
	os << s.getName() << "," << s.getSize() << "," << s.getPrice() << "," << s.getPhoto() << "\n";
	return os;
}




