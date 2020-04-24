#pragma once
#include <string>
class Problem
{
private:
	std::string text;
	std::string reporter;
	std::string solver;
	std::string status;
public:
	Problem(std::string _text, std::string s, std::string re, std::string so):text(_text),status(s), reporter(re),solver(so)  {}
	
	std::string getText(){ return this->text; }
	std::string getStatus() { return this->status; }
	std::string getReporter() { return this->reporter; }
	std::string getSolver() { return this->solver; }

	void setSolver(std::string s) { this->solver = s; }
	void setStatus(std::string s) { this->status = s; }


	~Problem(){}
};

