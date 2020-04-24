//
// Created by Ioana on 07.04.2019.
//

#include "controller.h"
#include <iostream>

void controller::undo() {
	undoActions.back()->executeUndo();
	undoActions.pop_back();
}

void controller::redo() {
	redoActions.back()->executeRedo();
	//redoActions.back()->executeUndo;
	redoActions.pop_back();
}

void controller::addTrenchController(string& size, string& photo, string& name, int price) {

	this->trench_repo_controller->addTrench(price, name, photo, size);
	this->trench_repo_controller->saveFile();
	TrenchCoat trench(name, size, photo, price);
	UndoAdd* undo = new UndoAdd(trench_repo_controller, trench);
	undoActions.push_back(undo);
	RedoAdd* redo = new RedoAdd(trench_repo_controller, trench);
	redoActions.push_back(redo);
}

void controller::updateTrenchController(string &size, string &photo, string &name, int price) {

	TrenchCoat undoTrench;
	std::vector<TrenchCoat> trench_list;
	trench_list = this->trench_repo_controller->getTrench();
	for (auto& trench : trench_list)
	{
		if (trench.getName() == name)
			undoTrench = trench;
	}

	this->trench_repo_controller->updateTrench(price, name, photo, size);
	this->trench_repo_controller->saveFile();
	
	TrenchCoat trenchCoat(undoTrench.getName(), undoTrench.getSize(), undoTrench.getPhoto(), undoTrench.getPrice());
	UndoUpdate* undo = new UndoUpdate(trench_repo_controller, trenchCoat);
	undoActions.push_back(undo);

	TrenchCoat redoTrench(name, size, photo, price);
	RedoUpdate* redo = new RedoUpdate(trench_repo_controller, redoTrench);
	redoActions.push_back(redo);
}

void controller::deleteTrenchController(string &name) {

	std::vector<TrenchCoat> trench_list;
	trench_list = this->trench_repo_controller->getTrench();
	TrenchCoat undoTrench;
	for (auto& trench : trench_list)
	{
		if (trench.getName() == name)
			undoTrench = trench;
		//{
			//UndoRemove* undo = new UndoRemove(trench_repo_controller, trench);
			//undoActions.push_back(undo);
		//}
	}
	
	this->trench_repo_controller->deleteTrench(name);
	this->trench_repo_controller->saveFile();

	UndoRemove* undo = new UndoRemove(trench_repo_controller, undoTrench);
	undoActions.push_back(undo);
	RedoRemove* redo = new RedoRemove(trench_repo_controller, undoTrench);
	redoActions.push_back(redo);

}

std::vector<TrenchCoat> controller::listTrenchController()
{
	std::vector<TrenchCoat> trench_coat_list;
	trench_coat_list = this->trench_repo_controller->listTrench();
	return trench_coat_list;
	//return this->trench_repo_controller->listTrench();
}

void controller::setFileLocation(std::string& filename)
{
	//std::cout<<filename;
	this->trench_repo_controller->setFileLocation(filename);
}

void controller::readFromFile()
{
	this->trench_repo_controller->readFromFile();
}

/*void Validator::check_name(string name)
{
	if (name.size()<3)
		throw controller_exception("Names must be longer than 3 leters");

	std::string::const_iterator nameValidator=name.begin();
	if((*nameValidator)<'A' || (*nameValidator)>'Z')
		throw controller_exception ("Names must start with uppercase");
}

void Validator::check_size(string size) {
	if ((size!="XL")&&(size!="L")&&(size!="M")&&(size!="S")&&(size!="XS"))
		throw controller_exception("Not a valid size");
}

void Validator::check_price(int price) {
	if (price<0)
		throw controller_exception("price must be a number greater than 0!");
}
*/