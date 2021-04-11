class node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkedList:
    def __init__(self):
        self.head=None

    def print_LL(self):
        if self.head==None:
            print("Linked List is empty")
        else:
            n=self.head
            while n!=None:
                print(n.data)
                n=n.ref

    def add_begin(self,data):
        new_node=node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=node(data)
        if self.head==None:
            print("Linked List is empty")
            self.head=new_node
        else:                    #if linked list is not empty we need to go to the last node
            n=self.head
            while n.ref!=None:     #this should take us to the last node
                n=n.ref             
            n.ref=new_node 

    #inserting after a given node
    def add_after_node(self,data,x):   #x is the given node   
        #first step should be to find x
        n=self.head
        while n!=None:
            if n.data == x:
                break
            else:
                n=n.ref #going to the next node
        if n==None:
            print("Given Node not present in Linked list")
        else:
            new_node=node(data)
            new_node.ref=n.ref
            n.ref=new_node
                   
LL1=linkedList()
LL1.add_begin(100)
LL1.add_begin(200)
LL1.add_end(10)
LL1.add_after_node(150,200)
LL1.print_LL()
