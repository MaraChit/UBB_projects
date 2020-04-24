
#include "SortedBag.h"
#include <iostream>

//th(1)
SortedBag::SortedBag(Relation r) : rel{r}
{
	this->root = -1;
	this->firstFree = 0;
	this->capacity = 10;
	this->bagSize = 0;
	this->elems = new Node[this->capacity];
}


int SortedBag::getParent(int index)
{
	int i = 0, k = 0;
	int current;
	int *stack = new int[this->bagSize];
	stack[i++] = this->root;
	while (k <i)
	{
		current = stack[k];
		k++;
		if (this->elems[current].left == index || this->elems[current].right == index)
		{
			delete[]stack;
			return current;
		}
		if (this->elems[current].left != -1)
			stack[i++] = this->elems[current].left;
		if (this->elems[current].right != -1)
			stack[i++] = this->elems[current].right;
	}
}

//th(size)
void SortedBag::resize()
{
	Node *newElems = new Node[this->capacity * 2];
	for (int i = 0; i < this->capacity; i++)
	{
		newElems[i].info = this->elems[i].info;
		newElems[i].left = this->elems[i].left;
		newElems[i].right = this->elems[i].right;
	}
	this->firstFree = this->capacity;
	this->capacity *= 2;
	delete[]this->elems;
	this->elems = newElems;
}


int SortedBag::maxOfLeft(int node)
{

	int current = this->elems[node].left;
	int max = this->elems[current].info;
	int idxMax = current;
	int *stack = new int[this->bagSize];
	int i = 0;
	int k = 0;
	if (this->elems[current].left != -1)
		stack[i++] = this->elems[current].left;
	if (this->elems[current].right != -1)
		stack[i++] = this->elems[current].right;

	while (k < i)
	{
		current = stack[k++];
		if (this->elems[current].info >= max && current != -1)
		{
			idxMax = current;
			max = this->elems[current].info;
		}
		if (this->elems[current].left != -1)
			stack[i++] = this->elems[current].left;
		if (this->elems[current].right != -1)
			stack[i++] = this->elems[current].right;
	}
	delete[]stack;

	return idxMax;
}


void SortedBag::add(TComp e)
{
	this->elems[firstFree].info = e;
	this->elems[firstFree].left = -1;
	this->elems[firstFree].right = -1;
	if (this->root == -1)
	{
		this->root = 0;
	}
	else
	{
		int current = this->root;
		int parent;
		while (current != -1)
		{
			parent = current;
			if (this->rel(e, this->elems[current].info))
				current = this->elems[current].left;
			else current = this->elems[current].right;
		}
		if (this->rel(e, this->elems[parent].info))
			this->elems[parent].left = firstFree;
		else
			this->elems[parent].right = firstFree;
	}
	firstFree++;
	if (firstFree >= this->capacity)
		resize();
	this->bagSize++;
}

bool SortedBag::remove(TComp e)
{
	int current = this->root;
	if (this->root == -1)
		return false;
	if (this->elems[current].info == e)
	{
		if (this->elems[current].left == -1)
			this->root = this->elems[current].right;
		else if (this->elems[current].right == -1)
			this->root = this->elems[current].left;
		else
		{
			int index = this->maxOfLeft(current);
			int parent = this->getParent(index);
			if (this->elems[parent].left == index)
				this->elems[parent].left = -1;
			else this->elems[parent].right = -1;
			this->elems[current].info = this->elems[index].info;
		}
		this->bagSize--;
		return true;
	}
	int *stack = new int[this->bagSize];
	int i = 0;
	int k = 0;
	if (this->elems[current].left != -1)
		stack[i++] = this->elems[current].left;
	if (this->elems[current].right != -1)
		stack[i++] = this->elems[current].right;
	while (k < i)
	{
		current = stack[k];
		k++;
		if (this->elems[current].info == e)
		{
			int parent = getParent(current);
			if (this->elems[current].left == -1)
			{
				if (this->elems[parent].left == current)
					this->elems[parent].left = this->elems[current].right;
				else this->elems[parent].right = this->elems[current].right;
			}
			else if (this->elems[current].right == -1)
			{
				if (this->elems[parent].left == current)
					this->elems[parent].left = this->elems[current].left;
				else this->elems[parent].right = this->elems[current].left;
			}
			else
			{
				int index = this->maxOfLeft(current);
				int parent = this->getParent(index);
				if (this->elems[parent].left == index)
					this->elems[parent].left = -1;
				else this->elems[parent].right = -1;
				this->elems[current].info = this->elems[index].info;

			}
			delete[]stack;
			this->bagSize--;
			return true;
		}
		if (this->elems[current].left != -1)
			stack[i++] = this->elems[current].left;
		if (this->elems[current].right != -1)
			stack[i++] = this->elems[current].right;
	}
	delete[]stack;
	return false;
}


bool SortedBag::search(TComp e) const
{
	if (this->root == -1)
		return false;
	int *stack = new int[this->bagSize];
	int i = 0;
	int k = 0;
	int parent = this->root;
	if (this->elems[parent].left != -1)
		stack[i++] = this->elems[parent].left;
	if (this->elems[parent].right != -1)
		stack[i++] = this->elems[parent].right;
	if (this->elems[parent].info == e)
		return true;

	while (k < i)
	{
		int current = stack[k];
		k++;
		if (this->elems[current].left != -1)
			stack[i++] = this->elems[current].left;
		if (this->elems[current].right != -1)
			stack[i++] = this->elems[current].right;
		if (this->elems[current].info == e)
		{
			delete[]stack;
			return true;
		}
	}
	delete[]stack;
	return false;
}


int SortedBag::nrOccurrences(TComp e) const
{
	if (this->root == -1)
		return 0;
	int nr = 0;
	int *stack = new int[this->bagSize];
	int i = 0;
	int k = 0;
	int parent = this->root;

	if (this->elems[parent].left != -1)
		stack[i++] = this->elems[parent].left;
	if (this->elems[parent].right != -1)
		stack[i++] = this->elems[parent].right;
	if (this->elems[parent].info == e)
		nr++;
	while (k < i)
	{
		int current = stack[k];
		k++;
		if (this->elems[current].left != -1)
			stack[i++] = this->elems[current].left;
		if (this->elems[current].right != -1)
			stack[i++] = this->elems[current].right;
		if (this->elems[current].info == e)
			nr++;
	}
	return nr;
}


int SortedBag::size() const
{
	return this->bagSize;
}


SortedBagIterator SortedBag::iterator() const
{
	return SortedBagIterator(*this);
}


bool SortedBag::isEmpty() const
{
	return (this->bagSize == 0);
}

/*void SortedBag::show()
{
	if (this->root == -1)
	{
		std::cout << "empty.\n";
		return;
	}
	int *stack = new int[this->bagSize];
	int i = 0;
	int k = 0;
	int parent = this->root;
	stack[i++] = this->root;
	while (k < i)
	{
		int current = stack[k];
		k++;
		if (this->elems[current].left != -1)
			stack[i++] = this->elems[current].left;
		if (this->elems[current].right != -1)
			stack[i++] = this->elems[current].right;
	}
	for (k = 0; k < i; k++)
	{
		std::cout << this->elems[stack[k]].info << " l: "<< this->elems[stack[k]].left<<" r:"<< this->elems[stack[k]].right<<" i:"<<stack[k]<<"\n";
	}
	std::cout << "\n";
}*/


SortedBag::~SortedBag()
{
	delete[] this->elems;
}


void SortedBag::addOccurrences(int nr, TComp elem) {

    if (nr<=0)
    {
        throw std::runtime_error("Nr of occurences is negative");
    }

    while(nr>0)
    {
        this->add(elem);
        nr--;
    }
}