class Bag:

    # creates a new, empty Bag
    def __init__(self):
        self.__elem=[]
        self.__frecv=[]


    # adds a new element to the Bag
    def add(self, e):
        if e in self.__elem:
            for i in range(0,len(self.__elem)):
                if self.__elem[i]==e:
                    self.__frecv[i]+=1
                    return
        else:
            self.__elem.append(e)
            self.__frecv.append(1)

            """
            theta(n) or theta(1)
            """

    # removes one occurrence of an element from a Bag
    # returns True if an element was actually removed (the Bag contained the element e), or False if nothing was removed
    def remove(self, e):
        if e in self.__elem:
            index=self.__elem.index(e)  #gets the index of element e
            if self.__frecv[index]==1:
                self.__elem.pop(index)
                self.__frecv.pop(index)
            else:
                self.__frecv[index]-=1
            return True

        return False
        """
        theta(1)
        """

    # searches for an element e in the Bag
    # returns True if the Bag contains the element, False otherwise
    def search(self, e):
        if e in self.__elem:
            return True
        return False
        """
        theta(1)
        """

    # counts and returns the number of times the element e appears in the bag
    def nrOccurrences(self, e):
        if e in self.__elem:
            i=self.__elem.index(e);
            return self.__frecv[i]
        return 0
        """
        theta(1)
        """


    # returns the size of the Bag (the number of elements)
    def size(self):
        nrEl=0
        for i in range (0, len(self.__frecv)):
            nrEl+=self.__frecv[i]
        return nrEl
        """
        theta(n)
        """


    # returns True if the Bag is empty, False otherwise
    def isEmpty(self):
        if len(self.__elem)==0:
            return True
        return False
        """
        theta(1)
        """

    # returns a BagIterator for the Bag
    def iterator(self):
        return BagIterator(self)
        """
        theta(1)
        """


class BagIterator:

    #creates an iterator for the Bag b, set to the first element of the bag, or invalid if the Bag is empty
    def __init__(self, b):
        self.__bag =b
        self.__index=0
        self.__currentFrecv=0


    # returns True if the iterator is valid
    def valid(self):
        if self.__index<len(self.__bag._Bag__elem):
            return True
        return False
        """
        theta(1)
        """

    # returns the current element from the iterator.
    # throws ValueError if the iterator is not valid
    def getCurrent(self):
        if not self.valid():
            raise ValueError
        else:
            return self.__bag._Bag__elem[self.__index]
        """
        theta(1)
        """

    # moves the iterator to the next element
    #throws ValueError if the iterator is not valid
    def next(self):
        if not self.valid():
            raise ValueError
        else:
            el=self.getCurrent()
            self.__currentFrecv+=1
            if self.__currentFrecv==self.__bag.nrOccurrences(el):
                self.__currentFrecv=0
                self.__index+=1
        """
        theta(1)
        """


    # sets the iterator to the first element from the Bag
    def first(self):
        self.__index=0
        self.__currentFrecv=0
        """
        theta(1)
        """
