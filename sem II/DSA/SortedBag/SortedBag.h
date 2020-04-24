#pragma once
#include "SortedBagIterator.h"


const int NULL_TComp  = -99999999;

typedef int TComp;
typedef TComp TElem;
typedef bool(*Relation)(TComp, TComp);

class SortedBagIterator;

struct Node
{
	TComp info;
	int left;
	int right;
};

class SortedBag {

	friend class SortedBagIterator;

private:
	/*representation of SortedBag*/
	Relation rel;
	Node *elems;
	int firstFree;
	int root;
	int capacity;
	int bagSize;
	void resize();

	//Theta(size)
    //returns the index of max value from left subtree
	int maxOfLeft(int node);

public:

	//constructor
	SortedBag(Relation r);

	//Theta(size)
	//returns the index of the parent
	int getParent(int index);

	//adds an element to the sorted bag
    //BC Theta(1)
    //WC Theta(size)
    //AC Theta|(size)
	void add(TComp e);

	//removes one occurrence of an element from a sorted bag
	//returns true if an element was removed, false otherwise (if e was not part of the sorted bag)

	//BC:Theta(1)
	//WC:Tetha(size)
	//WC:Tetha(size)
	bool remove(TComp e);

	
	//checks if an element appears is the sorted bag
	//BC Theta(1)
	//WC Theta(size)
	//AC Theta|(size)
	bool search(TComp e) const;

	//returns the number of occurrences for an element in the sorted bag
    //Theta(size)
	int nrOccurrences(TComp e) const;

	//returns the number of elements from the sorted bag
    //Theta(1)
	int size() const;

	//returns an iterator for this sorted bag
    //Theta(1)
	SortedBagIterator iterator() const;

	//checks if the sorted bag is empty
	//Theta(1)
	bool isEmpty() const;

	//void show();

	//BC: Theta(1)
	//WC: Theta(nr)
	//AC: Theta(nr)
	void addOccurrences(int nr, TComp elem);

	//destructor
	~SortedBag();

};