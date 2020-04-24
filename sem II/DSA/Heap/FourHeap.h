
#pragma once
#include <utility>
#include <iostream>
#include <exception>

using namespace std;

typedef int TElem;


#pragma once

typedef int TElem;

typedef bool(*Relation)(TElem p1, TElem p2);


class FourHeap
{
private:
	int capacity = 20;
	TElem* listOfElements = new TElem[this->capacity];
	int size = 0;
	Relation relation;

	//function bubble up
	void bubbleUp(int pos);

	//function bubble down
	void bubbleDown(int p);

	//resize for dynamic array
	void resize();

public:
	//implicit constructor
	FourHeap(Relation r);

	//adds an element 
	void push(TElem e);

	//removes and returns the element 
	//throws exception 
	TElem pop();

	//destructor
	~FourHeap();
};

