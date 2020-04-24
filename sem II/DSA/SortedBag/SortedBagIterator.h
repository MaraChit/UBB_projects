#pragma once
#include "SortedBag.h"
typedef int TComp;
typedef TComp TElem;
typedef bool(*Relation)(TComp, TComp);

class SortedBag;

class SortedBagIterator
{
	friend class SortedBag;
private:
	const SortedBag &bag;
	int current;
	TComp *stack;
	int stackSize;
	SortedBagIterator(const SortedBag &bag);
	void initStack(int node);
public:
	//sets the iterator to the first element of the container
	void first();

	//moves the iterator to the next element
	//throws exception if the iterator is not valid
	void next();

	//checks if the iterator is valid
	bool valid() const;

	//returns the value of the current element from the iterator
	// throws exception if the iterator is not valid
	TComp getCurrent() const;

	~SortedBagIterator();
};

