#include "MapIterator.h"
#include <exception>


MapIterator::MapIterator(const Map& container):c(container)
{
    this->current = nullptr;
    this->currentPoz = 0;
    this->first();
}


MapIterator::~MapIterator()
{
}

//sets the iterator to the first element of the container

void MapIterator::first()
{
    this->current = nullptr;
    this->currentPoz = 0;
    //int i;
    while (this->c.elements[this->currentPoz] == nullptr&&currentPoz < this->c.maxSize-1)
    {
        this->currentPoz++;
    }
    this->current = this->c.elements[this->currentPoz];
}



//moves the iterator to the next element

//throws exception if the iterator is not valid

void MapIterator::next()
{
    if (!this->valid())
        throw std::exception();//"UPS! Iterator not valid!");
    if (current->next != nullptr) { current = current->next; return; }
    this->currentPoz++;
    while (this->c.elements[this->currentPoz]==nullptr&&currentPoz<this->c.maxSize-1)
    {
        this->currentPoz++;
    }
    this->current = this->c.elements[this->currentPoz];
}



//checks if the iterator is valid

bool MapIterator::valid() const
{
    return this->current != nullptr;
}



//returns the value of the current element from the iterator

// throws exception if the iterator is not valid

TElem MapIterator::getCurrent() const
{
    if(this->valid())
        return this->current->data;
    throw std::exception();//"UPS! Iterator not valid!");
}