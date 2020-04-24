class Nod:
    def __init__(self, e):
        self.e = e
        self.next = None
    
class Lista:
    def __init__(self):
        self.head = None

    def empty(self):
        return self.head is None



'''
crearea unei liste din valori citite pana la 0
'''
def creareLista():
    lista = Lista()
    lista.head = creareLista_rec()
    return lista



def creareLista_rec():
    x = int(input("x="))
    if x == 0:
        return None
    else:
        nod = Nod(x)
        nod.next = creareLista_rec()
        return nod
    
'''
tiparirea elementelor unei liste
'''
def tipar(lista):
    tipar_rec(lista.head)
    
def tipar_rec(nod):
    if nod != None:
        print (nod.e)
        tipar_rec(nod.next)
        

'''


Pb1. a) listToSet(l1 l2 ... ln, list)=  | 0 , l is empty (n=0)
                                        | listToSet(l2 l3 ... ln, l1 U list) , occur(l2 l3...ln, l1)=0
                                        | listToSet(l2 ...ln, list) , otherwise

        occur(l1 l2 ... ln, el) = | 0, n=0
                                  | 1+occur(l2 l3 ... ln, el), l1=el
                                  | occur(l2....ln, el), otherwise



 '''


def occur(node,el):
    if node is None:
        return 0
    elif node.e == el:
        return 1+occur(node.next, el)
    else:
        return occur(node.next, el)


def listToSet(node, set):
    if node is None:
        return 0
    elif set.head is None:
        set.head = Nod(node.e)
        return listToSet(node.next, set)
    elif occur(set.head, node.e) == 0:
        newNode= Nod(node.e)
        newNode.next = set.head
        set.head = newNode
        return listToSet(node.next, set)
    else:
        return listToSet(node.next, set)


'''
Pb 1. b) union(l1 l2 ...ln, L1 L2 ... Lm) = | l1 l2 ... ln , m=0
                                            | L1 L2 ... Lm , n=0
                                            | l1 U union (l2 ... ln, L1 L2 ... Lm), occur(L1 L2 ... Lm, l1) = 0
                                            | union(l2 ... ln, L1 L2 ... Lm) , otherwise
'''

def union(node, lista2):
    if lista2.head is None:
         print(node.e)
         #print("BLA")
         while(node != None):
             node=node.next
             print(node.e)
             #print("BJHWDJFIO")
    elif node is None:
        newNode=lista2.head
        while(newNode is not None):
            print(newNode.e)
            newNode=newNode.next
    elif occur(lista2.head, node.e) == 0:
        print (node.e)
        #print ("UGH")
        return union(node.next, lista2)
    else:
        #print("prst")
        union(node.next, lista2)

def main():
    list = creareLista()
    set1 = Lista()
    lista2 = creareLista()
    #tipar(list)
    '''
    listToSet(list.head, set1)
    nod=set1.head
    while nod != None:
        print(nod.e)
        nod=nod.next

    '''
    union(list.head, lista2)
main()
    
    
    
    
    