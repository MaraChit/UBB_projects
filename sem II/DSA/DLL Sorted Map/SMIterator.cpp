//
// Created by Ioana on 17.04.2019.
//

#include "SMIterator.h"

SMIterator::SMIterator(const SortedMap &new_sm) :sm{new_sm}
{
    //this->sm=new_sm;
    this->currentElem=new_sm.head;
}

void SMIterator::first()
{
    this->currentElem=this->sm.head;
}

bool SMIterator::valid() const
{
    if(this->currentElem != nullptr)
    {
        return true;
    }
    return false;
}

void SMIterator::next()
{
    if (this->valid())
    {
        this->currentElem=this->currentElem->getNext();
    }else
    {
        throw std::exception("Stop iteration\n");
    }
}

SMIterator::~SMIterator() {}

TElem SMIterator::getCurrent() const
{
    if(this->valid())
    {
        return this->currentElem->getElement();
    }else
    {
        throw std::exception("invalid element\n");
    }
}

