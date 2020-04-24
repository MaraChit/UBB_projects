#pragma once
#include <string>
class Idea
{
private:
	int status, act;
	std::string proposer;
	std::string text;

public:
	Idea(int _status, std::string _text, int _act, std::string _proposer) : status(_status), text(_text), act(_act), proposer(_proposer) {}
	int getStatus()
	{
		return this->status;
	}
	void setStatus(int newStatus)
	{
		this->status = newStatus;
	}

	std::string getProposer()
	{
		return this->proposer;
	}
	void setProposer(std::string newProposer)
	{
		this->proposer = newProposer;
	}
	std::string getText()
	{
		return this->text;
	}
	void setText(std::string newText)
	{
		this->text = newText;
	}
	int getAct()
	{
		return this->act;
	}

	~Idea() {}
};

