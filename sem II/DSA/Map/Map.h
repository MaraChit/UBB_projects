#pragma once
#include <vector>
#include <math.h>
#include <utility>


#define NULL_TVALUE -1

using namespace std;

typedef int TKey;
typedef int TValue;
typedef std::pair<TKey, TValue> TElem;


typedef struct node
{
    TElem data;
    node* next;
} node;

class MapIterator;


class Map {
    friend class MapIterator;

private:

    // representation of Map
    node** elements;
    int numberOfElements;
    int maxSize;

    //theta(n)
    void resize();

    //theta(1)
    int hash(TKey key) const { return abs(key) % this->maxSize; }


public:



    // implicit constructor
    //BC theta(1)
    //WC theta(n)
    //AC O(n)

    Map();



    // adds a pair (key,value) to the map

    //if the key already exists in the map, then the value associated to the key is replaced by the new value and the old value is returned

    //if the key does not exist, a new pair is added and the value null is returned

    TValue add(TKey c, TValue v);



    //searches for the key and returns the value associated with the key if the map contains the key or null: NULL_TVALUE otherwise

    TValue search(TKey c) const;



    //removes a key from the map and returns the value associated with the key if the key existed ot null: NULL_TVALUE otherwise

    TValue remove(TKey c);



    //returns the number of pairs (key,value) from the map

    int size() const;



    //checks whether the map is empty or not

    bool isEmpty() const;



    //returns an iterator for the map

    MapIterator iterator() const;



    // destructor

    ~Map();



};

