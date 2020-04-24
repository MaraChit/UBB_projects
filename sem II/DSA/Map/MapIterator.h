#pragma once
#include "Map.h"
typedef int TKey;

typedef int TValue;



#include <utility>

typedef std::pair<TKey, TValue> TElem;

//unidirectional iterator for a container
class Map;
class MapIterator {
    friend class Map;
private:

    //Constructor receives a reference of the container.

    //after creation the iterator will refer to the first element of the container, or it will be invalid if the container is empty

    MapIterator(const Map& container);



    //contains a reference of the container it iterates over

    const Map& c;



    /* representation specific for the iterator*/

    node* current;
    int currentPoz;
public:



    //sets the iterator to the first element of the container
    //BC theta (1)
    //WC theta(n)
    //AC O(n)
    void first();
    ~MapIterator();


    //moves the iterator to the next element

    //throws exception if the iterator is not valid
    //BC theta (1)
    //WC theta(n)
    //AC O(n)
    void next();



    //checks if the iterator is valid
    //theta(1)
    bool valid() const;



    //returns the value of the current element from the iterator

    // throws exception if the iterator is not valid
    //theta(1)
    TElem getCurrent() const;



};


