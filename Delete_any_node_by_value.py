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

    def add_before_node(self,data,x):
        #check is linked list is empty
        if self.head==None:
            print("Linked List is empty")
            return
        #check if the given node is the first node 
        if self.head.data==x:
            new_node=node(data)
            new_node.ref=self.head
            self.head=new_node
            return 
        #if new node to be added somewhere in between
        #find x and then find the previous node
        n=self.head
        while n.ref!=None:
            if n.ref.data==x:   #here n is the prev node
                break
            else:
                n=n.ref
        if n==None:
            print("Given Node is not present in Linked List")
        else:
            #now that we found the prev node to the given node we can add after prev node
            new_node=node(data)
            new_node.ref=n.ref
            n.ref=new_node
    
    def insert_empty(self,data):
        if self.head==None:
            new_node=node(data)
            new_node.ref=None
        else:
            print("Linked List is empty")

    def del_begin(self):
        if self.head==None:
            print("Linked List is empty so we cannot delete nodes")
        else:
            n=self.head
            self.head=n.ref    #just make self.head point to next node 

    def del_end(self):    #in this just make the ref of the pre-last node as null
        if self.head==None:
            print("Linked List is empty so cannot delete node")
        elif self.head.ref==None:  #if linked list has only 1 element
            self.head=None
        else:
            n=self.head
            while n.ref.ref!=None:
                n=n.ref
            n.ref=None

    def del_node_by_value(self,x):
        if self.head==None:
            print("Linked List is empty so cant delete node")
        elif self.head.data==x:    #this is if given node is first node
            self.head=self.head.ref
        else:
            n=self.head
            while n.ref!=None:
                if n.ref.data==x:    #n is the prev node   #go to the prev node to the given node and change the reference
                    break
                else:
                    n=n.ref
            if n.ref==None:
                print("Given Node not found in Linked List")
            else:
                n.ref=n.ref.ref


LL1=linkedList()
LL1.add_begin(100)
LL1.add_begin(200)
LL1.add_end(10)
LL1.add_after_node(150,200)
LL1.add_before_node(90,100)
LL1.del_begin()
LL1.del_end()   
LL1.del_node_by_value(150)
LL1.print_LL()