//
// Created by Ioana on 16.04.2019.
//

#include "SortedMap.h"
#include<iostream>

SortedMap::SortedMap(Relation r)
{
    this->relation=r;
    this->head= nullptr;
    this->tail= nullptr;
    this->length=0;

}

TValue SortedMap::search(TKey c) const
{
    TValue v=NULL_TVALUE;
    dllNode* curent=this->head;
    while (curent!= nullptr)
    {
        if (curent->getElement().first==c)
        {
            v=curent->getElement().second;
            return v;
        }
        curent=curent->getNext();
    }

    return  v;

}

TValue SortedMap::add(TKey c, TValue v)
{
    this->length++;
    dllNode* current=this->head;
    if (current!= nullptr)
    while(this->relation(current->getElement().first,c) && current!=this->tail &&current->getElement().first!=c)
    {
        current=current->getNext();
    }

    if (current== nullptr)
    {
        dllNode* new_node=new dllNode(std::pair <TKey,TValue > (c,v), nullptr, nullptr);
        this->tail=new_node;
        this->head=new_node;
        return NULL_TVALUE;
    }

    if (c==current->getElement().first)
    {
        TValue old=current->getElement().second;
        current->setElement(std::pair <TKey,TValue > (c,v));
        this->length--;
        return old;
    }else
    {
        dllNode* new_node=new dllNode(std::pair <TKey,TValue > (c,v), nullptr, nullptr );
        if(current==this->head && !this->relation(current->getElement().first,c))
        {
            new_node->setNext(this->head);
            this->head->setPrev(new_node);
            this->head=new_node;
            return NULL_TVALUE;
        }

        if (current==this->tail && this->relation(current->getElement().first,c))
        {
            new_node->setPrev(this->tail);
            this->tail->setNext(new_node);
            this->tail=new_node;
            return NULL_TVALUE;

        }else
        {
            dllNode* x=current->getPrev();
            new_node->setNext(current);
            current->setPrev(new_node);
            //x->setNext(new_node);
            new_node->setPrev(x);
            x->setNext(new_node);
            return NULL_TVALUE;
        }
    }
}

int SortedMap::size() const
{
    return this->length;
}

bool SortedMap::isEmpty() const
{
    if (this->length==0)
        return true;

    return  false;
}

SortedMap::~SortedMap(){}
/*{
    dllNode* current=this->head;
    while(current!=tail)
    {
        current=current->getNext();
        delete(current->getPrev());

    }

    delete(this->tail);
}
*/
TValue SortedMap::remove(TKey c)
{
    if (this->length!=0) {
        dllNode *current = this->head;
        if (current->getElement().first == c) {
            TValue old = current->getElement().second;
            //dllNode *cur = current->getPrev();
            //cur->setNext(current->getNext());
            this->head=current->getNext();
            delete (current);
            this->length--;
            return old;
        }
        while (current != this->tail) {
            if (current->getElement().first == c) {
                TValue old = current->getElement().second;
                dllNode *cur = current->getPrev();
                cur->setNext(current->getNext());
                delete (current);
                this->length--;
                return old;
            }

            current = current->getNext();
        }
        current = this->tail;
        if (current->getElement().first == c) {
            TValue old = current->getElement().second;
            dllNode *cur = current->getPrev();
            cur->setNext(current->getNext());
            delete (current);
            this->length--;
            return old;
        }
    }
    return NULL_TVALUE;


}

int SortedMap::addIfNotPresent(SortedMap& sm)
{
    int size=sm.size();
    dllNode* current;
    dllNode* current2;
    current=sm.head;
    int found,counter=0;
    while(current!=sm.tail)
    {   //int k=current->getElement().first;
        found=0;
        current2=this->head;
        while(current2!=this->tail)
        {
            if (current->getElement()==current2->getElement()) {
                found = 1;
                break;
            }


        }
        if(found==0)
        {
            this->add(current->getElement().first,current->getElement().second);
            counter++;
        }


    }

    return counter;
}

SMIterator SortedMap::iterator() const
{
    return SMIterator(*this);
}