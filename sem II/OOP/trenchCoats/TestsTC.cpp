//
// Created by Ioana on 07.04.2019.
//

#include "TestsTC.h"
#include <assert.h>
#include<iostream>
#include "TrenchCoatRepo.h"
#include "TrenchCoat.h"
#include "controller.h"

/*void testDynamicArray()
{
	DynamicArray<int> v(1);
	v.addElement(3);
	v.addElement(2);
	assert(v.getElement(1)==2);
	assert(v.getSize()==2);
	v.setElement(1,5);
	assert(v.getElement(1)==5);
	v.removeElement(0);
	assert(v.getSize()==1);
	assert(v.getElement(0)==5);

}*/

void testAddController()
{
	TrenchCoatRepo repository;
	controller control(&repository);
	std::string name = "name";
	std::string size = "size";
	std::string photo = "photo";
	control.addTrenchController(size, photo, name, 100);
	std::vector<TrenchCoat> m = control.listTrenchController();
	assert(m.size() == 1);
	assert(m.size() != 0);

}

void testDeleteController()
{
	TrenchCoatRepo repository;
	controller control(&repository);
	std::string name = "name";
	std::string size = "size";
	std::string photo = "photo";
	control.addTrenchController(size, photo, name, 100);
	std::vector<TrenchCoat> m = control.listTrenchController();
	assert(m.size() == 1);
	control.deleteTrenchController(name);
	m = control.listTrenchController();
	//std::cout<<m.size();
	assert(m.size() == 0);
	assert(m.size() != 1);
}

void testUpdateController()
{
	TrenchCoatRepo repository;
	controller control(&repository);
	std::string name = "name";
	std::string size = "size";
	std::string photo = "photo";
	control.addTrenchController(size, photo, name, 100);
	std::vector<TrenchCoat> m = control.listTrenchController();
	assert(m.size() == 1);
	//std::string name2 = "name2";
	std::string size2 = "size2";
	std::string photo2 = "photo2";
	control.updateTrenchController(size2, photo2, name, 200);
	m = control.listTrenchController();
	assert(m[0].getName() == "name");
	assert(m[0].getSize() == "size2");
	assert(m[0].getPrice() == 200);
	assert(m[0].getPhoto() == "photo2");

}

void testReadingController()
{
	TrenchCoatRepo repository;
	controller control(&repository);
	std::string name = "name";
	std::string size = "size";
	std::string photo = "photo";
	std::string filelocation = "file.txt";
	control.setFileLocation(filelocation);
	control.addTrenchController(size, photo, name, 200);
	//std::cout<<repository.getNumberOfTrenches();
	TrenchCoatRepo repository2;
	controller control2(&repository2);
	control2.setFileLocation(filelocation);
	control2.readFromFile();
	//std::cout<<repository2.getNumberOfTrenches();
	std::vector<TrenchCoat> v = control2.listTrenchController();
	assert(v.size() != 0);

}



void testAddRepo()
{
	TrenchCoatRepo repository;
	std::string name = "name";
	std::string size = "size";
	std::string photo = "photo";
	repository.addTrench(200, name, photo, size);
	assert(repository.getNumberOfTrenches() == 1);
}

void testDeleteRepo()
{
	TrenchCoatRepo repository;
	std::string name = "name";
	std::string size = "size";
	std::string photo = "photo";
	repository.addTrench(200, name, photo, size);
	assert(repository.getNumberOfTrenches() == 1);
	repository.deleteTrench(name);
	assert(repository.getNumberOfTrenches() != 1);
	assert(repository.getNumberOfTrenches() == 0);
}

void testUpdateRepo()
{
	TrenchCoatRepo repository;
	std::string name = "name";
	std::string size = "size";
	std::string photo = "photo";
	repository.addTrench(200, name, photo, size);
	assert(repository.getNumberOfTrenches() == 1);
	std::string size2 = "size2";
	std::string photo2 = "photo2";
	repository.updateTrench(300, name, photo2, size2);
	assert(repository.getTrench()[0].getName() == "name");
	assert(repository.getTrench()[0].getPrice() == 300);
	assert(repository.getTrench()[0].getPhoto() == "photo2");
	assert(repository.getTrench()[0].getSize() == "size2");

}

void testTokenize()
{
	std::string title = "title,price,size,photo";
	assert(tokenize(title, ',').size() == 4);
}

void testReading()
{
	TrenchCoatRepo repository;
	std::string name = "name";
	std::string size = "size";
	std::string photo = "photo";
	std::string filelocation = "file.txt";
	repository.setFileLocation(filelocation);
	repository.addTrench(200, name, photo, size);
	assert(repository.getNumberOfTrenches() == 1);
	repository.saveFile();
	//std::cout<<repository.getNumberOfTrenches();
	TrenchCoatRepo repository2;
	repository2.setFileLocation(filelocation);
	repository2.readFromFile();
	//std::cout<<repository2.getNumberOfTrenches();
	//assert(repository2.getNumberOfTrenches()>0);
	std::vector<TrenchCoat> v = repository2.listTrench();
	assert(v.size() > 0);


}

void TestAll()
{
	testAddController();
	testDeleteController();
	testUpdateController();
	testAddRepo();
	testDeleteRepo();
	testUpdateRepo();
	testTokenize();
	testReading();
	testReadingController();
	//testDynamicArray();
}