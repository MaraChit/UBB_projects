//
// Created by Ioana on 16.04.2019.
//

#ifndef DLL_SORTED_MAP_DLLNODE_H
#define DLL_SORTED_MAP_DLLNODE_H

#include <utility>

typedef int TKey;
typedef int TValue;
typedef std::pair <TKey,TValue >TElem;

class dllNode {

private:
    TElem elem;
    dllNode* next;
    dllNode* prev;

public:
    dllNode(TElem element=std::pair <TKey,TValue > (0,0),dllNode* new_prev= nullptr, dllNode* new_next=nullptr)
    {
        this->elem=element;
        this->next=new_next;
        this->prev=new_prev;
    }

    ~dllNode(){}

    TElem getElement()
    {
        return this->elem;
    }

    void setElement(TElem NEW)
    {
        this->elem=NEW;
    }

    dllNode* getPrev()
    {
        return this->prev;
    }

    void setPrev(dllNode* new_prev)
    {
        this->prev=new_prev;
    }
    dllNode* getNext()
    {
        return this->next;
    }

    void setNext(dllNode* new_next)
    {
        this->next=new_next;
    }

    bool operator==(const dllNode &x)const
    {
        return this->next==x.next && this->prev==x.prev && this->elem==x.elem;
    }

    bool operator!=(const dllNode &x)const
    {
        return !(x==*this);
    }
};


#endif //DLL_SORTED_MAP_DLLNODE_H
