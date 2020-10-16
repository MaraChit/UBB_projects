class SymbolTable:
    def __init__(self, size):
        #define the hashtable to be used for the symbol table
        self.elems = [None] * size
        self.size = size

    def __str__(self):
        st = ""
        for symbol in self.elems:
            st += str(symbol) + "\n"
        return st

    def hash(self, elem):
        #define a hash function
        return elem % self.size

    def linear_probing(self, elem, i):
        return (self.hash(elem) + i) % self.size

    def ascii_code(self, elem):
        sum = 0
        for i in range(0,len(elem)):
            sum = sum + ord(elem[i])
        return sum

    def add(self, elem):
        #adding a new element in the symbol table
        if isinstance(elem, str):
            key = self.ascii_code(elem)
        else:
            key = elem

        i = 0
        poz = self.linear_probing(key, i)
        while i < self.size and self.elems[poz] is not None:
            i = i+1
            poz = self.linear_probing(key, i)
        if poz != self.size:
            self.elems[poz] = [key, elem]

    def search(self, elem):
        #searching for an element in a symbol table
        if isinstance(elem, str):
            key = self.ascii_code(elem)
        else:
            key = elem
        i = 0
        poz = self.linear_probing(key, i)
        while i < self.size:
            if self.elems[poz] is None or self.elems[poz][1] != elem:
                i = i+1
                poz = self.linear_probing(key, i)
            else:
                return True

        return False

def test():
    st = SymbolTable(5)

    st.add(17)
    st.add(6)
    st.add(1)
    st.add("ana")

    print("Symbol table: \n")
    print(st)

    print("checking for value '17':")
    print(st.search(17))
    print("checking for value '3':")
    print(st.search(3))
    print("checking for value 'ana':")
    print(st.search('ana'))

test()