#make the same singly linked list again
#step 1 : Create the individual Node having data but no ref to next node
class node:
    def __init__(self,data):
        self.data=data
        self.ref=None

#step 2: Create the empty linked list 
class linked_list:
    def __init__(self):
        self.head=None
    
    #traversing through the linked list
    def print_LL(self):
        if self.head==None:               #before traversing the linked list check is linked list is empty
            print("Linked List is empty")
        else:
            n=self.head
            while n!=None:             #i.e till we have reached the last node dont stop
                print(n.data)       #print the data in the node
                n=n.ref     

    def add_begin(self,data):
        new_node=node(data)        #create the new node with 100 as data
        new_node.ref=self.head    #since adding at begin we need to give the ref of node to past first node
        self.head=new_node        #now the head should point to the first node

LL1=linked_list()
LL1.add_begin(100)
LL1.add_begin(200)
LL1.print_LL()
            
    
