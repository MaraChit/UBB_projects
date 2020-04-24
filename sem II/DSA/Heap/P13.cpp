#include "P13.h"
#include <algorithm>
#include <iostream>

void removeLast(vector<TElem>& elements, Relation r, int k) {
	FourHeap* heap = new FourHeap{ r };
	for (auto element : elements) {
		heap->push(element);
	}
	int size=k, pos=0;
	for (int i=0;i<k; i++) {
		TElem elem = heap->pop();
		for (int j = 0; j < elements.size(); j++) {
			if (elements[j] == elem)
			{
				pos = j;
				elements.erase(elements.begin() + pos);
				j = elements.size();
			}		
		}
	}
}