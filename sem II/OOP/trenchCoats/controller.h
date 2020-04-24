//
// Created by Ioana on 07.04.2019.
//

#ifndef TRENCHCOATS_CONTROLLER_H
#define TRENCHCOATS_CONTROLLER_H


//#include "DynamicArray.h"
#include "TrenchCoatRepo.h"
#include "user_repo.h"
#include "UndoRedo.h"


class Validator
{

public:
	void check_name(string name);
	void check_size(string size);
	void check_price(int price);
};



class controller_exception :public std::runtime_error
{
public:
	controller_exception(std::string error) :std::runtime_error(("controller_exception" + error + '\n')) {}
};




class controller {

private:
	TrenchCoatRepo* trench_repo_controller;
	//user_repo userRepo_controller;
	std::vector<UndoAction*> undoActions;
	std::vector<RedoAction*> redoActions;
	//std::vector<UndoAction*> redoActions;

public:
	controller(TrenchCoatRepo* new_trench_coat_repo_controller)
	{
		this->trench_repo_controller = new_trench_coat_repo_controller;
	}

	~controller() {}

	void addTrenchController(string& size, string& photo, string& name, int price);
	std::vector<TrenchCoat> listTrenchController();
	void updateTrenchController(string& size, string& photo, string& name, int price);
	void deleteTrenchController(string& name);
	//input a string with the path to the filename
	//it calls the same function from the repo
	void setFileLocation(std::string& filename);
	//calls the function from repo which reads from the file
	void readFromFile();

	/*void setMyListLocation(std::string& filename)
	{
		this->userRepo_controller.setFileLocation(filename);
	}*/

	void undo();
	void redo();
};


#endif //TRENCHCOATS_CONTROLLER_H
