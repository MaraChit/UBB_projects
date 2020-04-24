//
// Created by Ioana on 17.04.2019.
//

#ifndef DLL_SORTED_MAP_SMITERATOR_H
#define DLL_SORTED_MAP_SMITERATOR_H

#include "SortedMap.h"
#include <exception>
#include <stdexcept>
class SortedMap;
class SMIterator {

    friend class SortedMap;

private:
    const SortedMap& sm;
    dllNode* currentElem;
public:
    //Constructor receives a reference of the container.
    //after creation the iterator will refer to the first element of the container, or it will be invalid if the container is empty
    SMIterator(const SortedMap& sm);
    //sets the iterator to the first element of the container
    void first(); //theta(1)
    //moves the iterator to the next element
    //throws exception if the iterator is not valid
    void next(); //theta(1)
    //checks if the iterator is valid
    bool valid() const; //theta(1)
    //returns the value of the current element from the iterator
    // throws exception if the iterator is not valid
    TElem getCurrent() const; //theta(1)
    ~SMIterator();

};


#endif //DLL_SORTED_MAP_SMITERATOR_H
