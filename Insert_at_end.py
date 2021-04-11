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
                
                    



LL1=linkedList()
LL1.add_begin(100)
LL1.add_begin(200)
LL1.add_end(10)
LL1.print_LL()