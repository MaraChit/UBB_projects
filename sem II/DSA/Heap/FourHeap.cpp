
#include "FourHeap.h"

// Theta(1)
FourHeap::FourHeap(Relation r) {
	this->relation = r;
}

// Theta(n)
void FourHeap::resize() {
	this->capacity *= 2;
	TElem* aux = new TElem[this->capacity];
	for (int i = 0; i < this->size; i++) {
		aux[i] = this->listOfElements[i];
	}
	delete[] this->listOfElements;
	this->listOfElements = aux;
}

// O(log4n)
void FourHeap::bubbleUp(int position) {
	int poz = position; 
	TElem elem = this->listOfElements[poz];
	int parent = (poz-1) / 4;
	while (poz > 0 && !this->relation(elem, this->listOfElements[parent])) {
		auto aux = this->listOfElements[poz];
		this->listOfElements[poz] = this->listOfElements[parent];
		this->listOfElements[parent]=aux;
		poz = parent;
		parent = (poz-1) / 4;
	}
	this->listOfElements[poz] = elem;
}

// O(log4n)
void FourHeap::push(TElem e) {

	if (this->size == this->capacity)
		this->resize();
	
	this->size++;
	this->listOfElements[this->size-1] = e;
	bubbleUp(size-1);
}



// O(log4n)
void FourHeap::bubbleDown(int p) {
	int poz = p;
	TElem elem = this->listOfElements[poz];
	while (poz < this->size - 1) {
		int maxChild = -1;
		if (poz * 4 + 1 < this->size) {
			maxChild = poz * 4 + 1;
		}
		if (poz * 4 + 2 < this->size && !this->relation(this->listOfElements[poz * 4 + 2], this->listOfElements[maxChild])) {
			maxChild = poz * 4 + 2;
		}
		if (poz * 4 + 3 < this->size && !this->relation(this->listOfElements[poz * 4 + 3], this->listOfElements[maxChild])) {
			maxChild = poz * 4 + 3;
		}
		if (poz * 4 + 4 < this->size && !this->relation(this->listOfElements[poz * 4 + 4], this->listOfElements[maxChild])) {
			maxChild = poz * 4 + 4;
		}
		if (maxChild != -1 && !this->relation(this->listOfElements[maxChild], elem)) {
			TElem aux = this->listOfElements[poz];
			this->listOfElements[poz] = this->listOfElements[maxChild];
			this->listOfElements[maxChild] = aux;
			poz = maxChild; 
		}
		else {
			poz = this->size-1;
		}
	}
}


// O(log4n)
TElem FourHeap::pop() {
	if (this->size <= 0) {
		throw std::exception();
	}
	auto deletedElem = this->listOfElements[0];
	this->listOfElements[0] = this->listOfElements[this->size - 1];
	this->size--;
	bubbleDown(0);
	return deletedElem;
}

// Theta(1)
FourHeap::~FourHeap() { 
	delete[] this->listOfElements;
}
