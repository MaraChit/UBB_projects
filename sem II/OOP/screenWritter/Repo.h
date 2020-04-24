#pragma once
#include <vector>
#include "Idea.h"
#include "Writter.h"
class Repo
{
private:
	std::vector<Idea> ideeas;
	std::vector<Writter> writters;
public:
	Repo();
	std::vector<Idea> returnIdeas()
	{
		return this->ideeas;
	}

	std::vector<Writter> returnWritters()
	{
		return this->writters;
	}

	void readData();
	void addIdea(int status, std::string text, int act, std::string proposer);
	void updateIdea(int news, std::string newText,int poz)
	{
		this->ideeas[poz].setStatus(news);
		this->ideeas[poz].setText(newText);
		
	}
	~Repo();
};

