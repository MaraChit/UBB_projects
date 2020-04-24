#include "SortedBagIterator.h"
#include <iostream>

//th(size)
SortedBagIterator::SortedBagIterator(const SortedBag &bag) : bag{bag}
{
	stack = new TComp[bag.bagSize];
	stackSize = 0;
	current = 0;
	initStack(bag.root);
}

//th(size)
void SortedBagIterator::initStack(int node)
{
	if (node != -1)
	{
		initStack(bag.elems[node].left);
		this->stack[this->stackSize++] = this->bag.elems[node].info;
		initStack(bag.elems[node].right);
	}
}

//th(1)
void SortedBagIterator::first()
{
	current = 0;
}

//th(1)
void SortedBagIterator::next()
{
	if (!valid())
		throw std::exception();
	current++;
}

//th(1)
bool SortedBagIterator::valid() const
{
	if (current < bag.bagSize)
		return true;
	return false;
}


TComp SortedBagIterator::getCurrent() const
{
	if (!valid())
		throw std::exception();

	return stack[current];
}

SortedBagIterator::~SortedBagIterator()
{
	delete[]stack;
}
