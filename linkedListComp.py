class Node:
    def __init__(self, linf, lsup, k=None, n=None):
        self.inf = linf
        self.sup = lsup
        self.k = k
        self.next_node = n
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, n):
        self.next_node = n
    
    def get_inf(self):
        return self.inf

    def get_sup(self):
        return self.sup

    def get_k(self):
        return self.k
    
    def set_inf(self, d):
        self.inf = d

    def set_sup(self, d):
        self.sup = d
    
    def set_k(self, k):
        self.k = k

    def ___repr___(self):
        s = '{},{},{}'.format(self.inf, self.sup, self.k)
        return s

#Linked List
class LinkedList:
    def __init__(self, r=None):
        self.root = r
        if(self.root != None):
            self.size = 1
        else:
            self.size = 0
    
    def get_size(self):
        return self.size
    
    def add(self, s, i, k=None):
        new_node = Node(s, i ,k)
        if self.root is None:
            self.root = new_node
        else:
            self.root.next_node = new_node
            new_node.next_node = None
        self.size += 1

    def printList(self):
        current = self.root

        while current is not None:
            i = [current.inf, current.sup, current.k]
            print(i, end=" -> ")
            current = current.get_next()
        print('\n')

#Finds the nth last node
def nth_last_node(ll:LinkedList, n):
    nth = None
    t = ll.root
    count = 1

    while t is not None:
        t = t.get_next()
        count += 1

        if count >= n+1:
            if nth is None:
                nth = ll.root
            else:
                nth = nth.get_next()
    
    return [nth.get_inf, nth.get_sup]
