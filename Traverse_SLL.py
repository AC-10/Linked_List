#Linked  list is not stored in a contiguos manner
#LL has 2 major benefits over array
#Dont need to pre allocate space
#Insertion is easier
#Singly Linked List has data and address of next node
'''1st step is to create a individual node'''
class node:
    def __init__(self,data):       #no reference to next node argument becoz we r creating individual nodes
        self.data=data
        self.ref=None

'''node1=node(10)'''      #10|None will be present in the node

class linkedList:
    def __init__(self):
        self.head=None       #head is the starting node so if head is None then LinkedList is empty
    
    #traversing the linked list and printing data present in node
    def print_LL(self):
        if self.head==None:               #before traversing the linked list check is linked list is empty
            print("Linked List is empty")
        else:
            n=self.head
            if n!=None:             #i.e till we have reached the last node dont stop
                print(n.data)       #print the data in the node
                n=n.ref             
                
LL1=linkedList()
LL1.print_LL()
        