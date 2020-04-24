#include "Map.h"
#include "MapIterator.h"
#include <iostream>


Map::Map()
{
    this->maxSize = 10;
    this->numberOfElements = 0;
    this->elements = new node*[this->maxSize];
    for (int i = 0; i < this->maxSize; i++)
        this->elements[i] = nullptr;
}


Map::~Map()
{
    // :)))))))
    //try this

    for(int i=0;i<numberOfElements;i++){


       delete this->elements[i];

    }
    delete[] elements;
}


void Map::resize()
{
    double loadFactor = this->numberOfElements / this->maxSize;
    if (loadFactor <= 0.7)
        return;
    this->maxSize *= 2;

    node** newArray = new node*[this->maxSize];
    for (int i = 0; i < this->maxSize; i++) {
        newArray[i] = nullptr;
    }

    for (int i = 0; i < this->maxSize / 2; i++) {
        node* current = this->elements[i];

        while (current != nullptr) {
            int pos = this->hash(current->data.first);
            node* tempNode = new node;
            tempNode->data.second = current->data.second;
            tempNode->data.first = current->data.first;
            tempNode->next = newArray[pos];
            newArray[pos] = tempNode;
            current = current->next;
        }
    }

    for (int i = 0; i < this->maxSize / 2; i++) {
        node* current = this->elements[i];
        while (current != nullptr) {
            node* copy = current->next;
            delete current;
            current = copy;
        }
    }
    delete[] this->elements;
    this->elements = newArray;

}

TValue Map::add(TKey c, TValue v) {
    TValue ret;

    this->resize();
    int pos = this->hash(c);
    node *current = this->elements[pos];

   // node *temp = new node;

    if ((current != nullptr)&&(current->data.first!=c)) {
        node *temp = new node;
        temp->data.first = c;
        temp->data.second = v;
        temp->next = current;

        this->elements[pos] = temp;
        this->numberOfElements++;
        return NULL_TVALUE;
    }else
    {
        if(current!= nullptr && current->data.first==c) {
            ret = current->data.second;
            current->data.second = v;
            return ret;
        }
    }


    node *temp = new node;
    temp->data.first = c;
    temp->data.second = v;
    temp->next = nullptr;
    this->elements[pos] = temp;
    this->numberOfElements++;
    return NULL_TVALUE;



}

TValue Map::search(TKey c) const
{
    int pos = this->hash(c);
    node* current = this->elements[pos];
    while (current != nullptr)
    {
        if (current->data.first == c)
        {
            return current->data.first;
        }
        current = current->next;
    }
    return NULL_TVALUE;
}

int Map::size()const
{
    return this->numberOfElements;
}

bool Map::isEmpty()const
{
    if (this->numberOfElements == 0)
        return true;

    return false;
}

TValue Map::remove(TKey c)
{
    int pos = this->hash(c);
    TValue v;
    node* current = this->elements[pos];
    node* prev = nullptr;
    while (current != nullptr)
    {
        if (current->data.first == c)
        {
                if (prev != nullptr)

                    prev->next = current->next;
                else
                    this->elements[pos] = current->next;

                v=current->data.second;

                delete current;
                this->numberOfElements--;
                return v;
        }
        prev = current;
        current = current->next;
    }
    return NULL_TVALUE;
}

MapIterator Map::iterator() const
{
    MapIterator s(*this);
    return s;
}
