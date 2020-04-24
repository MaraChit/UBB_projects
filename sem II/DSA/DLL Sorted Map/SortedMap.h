//
// Created by Ioana on 16.04.2019.
//

#ifndef DLL_SORTED_MAP_SORTEDMAP_H
#define DLL_SORTED_MAP_SORTEDMAP_H

#include "dllNode.h"
#include <utility>
#include "SMIterator.h"

#define NULL_TVALUE -1

typedef  bool(*Relation)(TKey,TKey);

typedef int TKey;
typedef int TValue;
typedef std::pair <TKey,TValue >TElem;
class SMIterator;
class SortedMap {
    friend class SMIterator;
private:

    Relation relation;
    dllNode* head;
    dllNode* tail;
    int length;
    //representation of SortedMap



public:



    // implicit constructor

    SortedMap(Relation r);



    // adds a pair (key,value) to the map

    //if the key already exists in the map, then the value associated to the key is replaced by the new value and the old value is returned

    //if the key does not exist, a new pair is added and the value null is returned

    //best case theta(1)
    //worst case theta(n)
    //average case theta(n)

    TValue add(TKey c, TValue v);



    //searches for the key and returns the value associated with the key if the map contains the key or null: NULL_TELEM otherwise
    //best case theta(1)
    //worst case theta(n)
    //average case theta(n)
    TValue search(TKey c) const;





    //removes a key from the map and returns the value associated with the key if the key existed or null: NULL_TELEM otherwise
    //best case theta(1)
    //worst case theta(n)
    //average case theta(n)
    TValue remove(TKey c);



    //returns the number of pairs (key,value) from the map

    int size() const; //theta(1)



    //checks whether the map is empty or not

    bool isEmpty() const; //theta(1)



    // return the iterator for the map

    // the iterator will return the keys following the order given by the relation

    SMIterator iterator() const;



    // destructor

    ~SortedMap();

    //ADDS all pairs from sm, whose key is not in the SortedMap
    //returns the number of added pairs
    //best case (n)
    //worst case 0(n)
    //average case 0(n)
    int addIfNotPresent(SortedMap& sm);


};


#endif //DLL_SORTED_MAP_SORTEDMAP_H
