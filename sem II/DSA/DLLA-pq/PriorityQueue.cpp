//
// Created by Ioana on 06.05.2019.
//

#include "PriorityQueue.h"
#include<iostream>
using namespace std;

#define NULLVAL -1


PriorityQueue::PriorityQueue(Relation r)
{
    // Creates a new empty priority queue
    // Pre: r is a relation over the priorities, r: TPriority x TPriority
    // Post: PriorityQueue_dlla is an empty priority queue
    // O(n)

    priority=r;
    PriorityQueue_dlla.capacity=10000;
    PriorityQueue_dlla.size=0; //pq is empty
    PriorityQueue_dlla.head= NULLVAL;
    PriorityQueue_dlla.tail=NULLVAL;
    PriorityQueue_dlla.FirstEmpty=0; //first empty poz is the first poz
    PriorityQueue_dlla.elements = new Element[10000];
    PriorityQueue_dlla.prev= new int[10000];
    PriorityQueue_dlla.next= new int[10000];

    for (int i=0;i<PriorityQueue_dlla.capacity; i++)
    {
        PriorityQueue_dlla.prev[i]=i-1;
        PriorityQueue_dlla.next[i]=i+1;
    }

    PriorityQueue_dlla.prev[0]=NULLVAL;
    PriorityQueue_dlla.next[PriorityQueue_dlla.capacity-1]=NULLVAL;

}

void PriorityQueue::push(TElem e, TPriority p) {
    // Pushes a new element to the priority queue
    // Pre: TElem e, TPriority p
    // Post: Element (e, p)
    // Best case: Theta(1)
    // Worst case: Theta(size)
    // Average case: O(size)
    Element* pair = new Element(e, p);

    if(isEmpty())           // if the queue is empty
        insertEmpty(pair);
    else
    {
        int previous_position = -1;
        int current_position = PriorityQueue_dlla.head;
        bool cond = true;
        while(cond)                     // search for position where to insert the element
        {
            if(current_position == -1)
                cond = false;
            else
            {
                TPriority current_element = PriorityQueue_dlla.elements[current_position].second;
                if(priority(current_element, p))        // compare using priority relation
                {
                    previous_position = current_position;
                    current_position = PriorityQueue_dlla.next[current_position];
                }
                else
                    cond = false;
            }
        }
        if(previous_position == -1) // if the element we add has the highest priority
          //if(PriorityQueue_dlla.prev[current_position]==-1)
            insertFirst(pair);
        else
            insertPosition(pair, previous_position);//PriorityQueue_dlla.prev[current_position]); // add the element to the first empty position
    }
    PriorityQueue_dlla.size += 1;

}

Element PriorityQueue::top() const
{
    // Returns from the priority queue the element with the highest priority and its priority
    // Pre: PriorityQueue_dlla priority queue
    // Post: PriorityQueue_dlla priority queue,
    //       el contains the element with the highest priority from the priority queue and its priority
    // Throws: exception if the priority queue is empty
    // Theta(1)
    if(isEmpty())
        throw std::runtime_error("Empty Queue");

    int pos = PriorityQueue_dlla.head;
    Element el = PriorityQueue_dlla.elements[pos];

    return el;
}

Element PriorityQueue::pop()
{
    // Pops and returns the element with the highest priority from the priority queue
    // Pre: PriorityQueue_dlla priority queue
    // Post: PriorityQueue_dlla' priority queue,
    //       el contains the element with the highest priority from the priority queue and its priority
    // Throws: exception if the priority queue is empty
    // Theta(1)
    if(isEmpty())
        throw std::runtime_error("Empty Queue");

    int pos = PriorityQueue_dlla.head;
    Element el = PriorityQueue_dlla.elements[pos];

    PriorityQueue_dlla.head = PriorityQueue_dlla.next[pos];
    PriorityQueue_dlla.prev[pos]=NULLVAL;

    PriorityQueue_dlla.next[pos] = PriorityQueue_dlla.FirstEmpty;
    PriorityQueue_dlla.FirstEmpty = pos;

    PriorityQueue_dlla.size -= 1;

    return el;
}
bool PriorityQueue::isEmpty() const
{
    // Checks if the priority queue is empty
    // Pre: PriorityQueue_dlla priority queue
    // Post: true, if PriorityQueue_dlla has no elements
    //       false, otherwise
    // Theta(1)
    if(PriorityQueue_dlla.size == 0)
        return true;
    return false;
}

PriorityQueue::~PriorityQueue()
{
    //cout<<"fvg";
    delete[] PriorityQueue_dlla.elements;
    delete[] PriorityQueue_dlla.next;
    //delete[] PriorityQueue_dlla.prev;
}


int PriorityQueue::getSize()
{
    // Returns the size of the queue
    // Theta(1)
    return PriorityQueue_dlla.size;
}


void PriorityQueue::insertEmpty(Element *pair)
{
    // Adds an Element to the empty priority queue
    // Pre: PriorityQueue_dlla priority queue, Element pair
    // Post: PriorityQueue_dlla' priority queue,
    // Theta(1)
    int pos = PriorityQueue_dlla.FirstEmpty;
    PriorityQueue_dlla.FirstEmpty = PriorityQueue_dlla.next[pos];

    PriorityQueue_dlla.elements[pos].first = pair->first;
    PriorityQueue_dlla.elements[pos].second = pair->second;
    PriorityQueue_dlla.next[pos] = NULLVAL;
    PriorityQueue_dlla.prev[pos]=NULLVAL;
    PriorityQueue_dlla.head = pos;
    PriorityQueue_dlla.tail=pos;
}

void PriorityQueue::insertFirst(Element *pair)
{
    // Adds an Element to the top of the priority queue
    // Pre: PriorityQueue_dlla priority queue, Element pair
    // Post: PriorityQueue_dlla' priority queue,
    // Theta(1)
    int pos = PriorityQueue_dlla.FirstEmpty;
    PriorityQueue_dlla.FirstEmpty = PriorityQueue_dlla.next[pos];

    PriorityQueue_dlla.elements[pos].first = pair->first;
    PriorityQueue_dlla.elements[pos].second = pair->second;

    PriorityQueue_dlla.next[pos] = PriorityQueue_dlla.head;
    PriorityQueue_dlla.prev[PriorityQueue_dlla.head]=pos;
    PriorityQueue_dlla.prev[pos]=NULLVAL;
    PriorityQueue_dlla.head = pos;
}

void PriorityQueue::insertPosition(Element *pair, int previous_position)
{
    // Adds an Element to the priority queue on first empty position
    // Pre: PriorityQueue_dlla priority queue, Element pair
    // Post: PriorityQueue_dlla' priority queue
    // Theta(1)
    int pos = PriorityQueue_dlla.FirstEmpty;
    PriorityQueue_dlla.FirstEmpty = PriorityQueue_dlla.next[pos];

    PriorityQueue_dlla.elements[pos].first = pair->first;
    PriorityQueue_dlla.elements[pos].second = pair->second;

    PriorityQueue_dlla.next[pos] = PriorityQueue_dlla.next[previous_position];
    PriorityQueue_dlla.prev[pos]=previous_position;
    PriorityQueue_dlla.prev[PriorityQueue_dlla.next[previous_position]]=pos;
    PriorityQueue_dlla.next[previous_position] = pos;

    if(PriorityQueue_dlla.tail==previous_position)
    {
        PriorityQueue_dlla.tail=pos;
    }

}

void PriorityQueue::display()
{
    int i;
    std::cout<<PriorityQueue_dlla.head<<" "<<PriorityQueue_dlla.tail<<endl;
    for(i=0;i<PriorityQueue_dlla.size;i++)
    {
        std::cout<<PriorityQueue_dlla.next[i];
        std::cout<<" ";
        std::cout<<PriorityQueue_dlla.prev[i];
        std::cout<<" ";
        std::cout<<PriorityQueue_dlla.elements[i].first<<" "<<PriorityQueue_dlla.elements[i].second;
        std::cout<<endl;
    }
}


bool PriorityQueue::search(TElem elem) const
{
    // BC: Theta(1)
    // WC: Theta(size)
    // AC: Theta(size)
    int next = PriorityQueue_dlla.head;   // first element
    int size = PriorityQueue_dlla.size;    // number of elements
    while (size)              // iterate through all elements
    {
        if(PriorityQueue_dlla.elements[next].first == elem)   // if element was found
            return true;    // return true
        next = PriorityQueue_dlla.next[next]; // go to next element
        size--;
    }
    return false;   // return false if el was not found
}
