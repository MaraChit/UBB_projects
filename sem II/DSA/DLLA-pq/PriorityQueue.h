//
// Created by Ioana on 06.05.2019.
//

#ifndef DLLA_PRIORITYQ_PRIORITYQUEUE_H
#define DLLA_PRIORITYQ_PRIORITYQUEUE_H
#include<iostream>

typedef int TElem;

typedef int TPriority;



typedef std::pair<TElem, TPriority> Element;



typedef bool (*Relation)(TPriority p1, TPriority p2);

/*typedef struct DLLAnode {
    TElem info;
    int next;
    int prev;
}DLLAnode;*/

typedef struct DLLA {

    Element* elements;
    int* next;
    int* prev;
    int capacity;
    int head;
    int tail;
    int FirstEmpty;
    int size;

}DLLA;

class PriorityQueue {
private:

    //representation of PriorityQueue
    DLLA PriorityQueue_dlla;
    Relation priority;
    void reize();



public:

    //implicit constructor

    PriorityQueue(Relation r);



    //adds an element with priority to the queue

    void push(TElem e, TPriority p);



    //returns the element with the highest priority with respect to the order relation

    //throws exception if the queue is empty

    Element top()  const;



    //removes and returns the element with the highest priority

    //throws exception if the queue is empty

    Element pop();



    //checks if the queue is empty

    bool isEmpty() const;



    //destructor

    ~PriorityQueue();


    int getSize();
    void display();

    void insertEmpty(Element *pair);
    void insertFirst(Element *pair);
    void insertPosition(Element *pair, int previous_position);


    bool PriorityQueue::search(TElem elem) const;




};


#endif //DLLA_PRIORITYQ_PRIORITYQUEUE_H
