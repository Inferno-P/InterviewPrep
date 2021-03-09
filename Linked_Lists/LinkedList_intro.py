## Create a Linked List Structure


class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beg(self, data):
        newNode = Node(data, self.head) # Create a new Node and point it to the HEAD value
        newNode.next = self.head
        self.head = newNode
    
    def insert_at_end(self, data):
        
        
        if self.head is None: 
            #List is empty
            newNode = Node(data,self.head)
            self.head = newNode
            return
        
        # Go to the end
        itrNode = self.head
        while itrNode.next != None:
            itrNode = itrNode.next
            #stops ar the second last node.
            
        newNode = Node(data,None)
        itrNode.next = newNode 
        
        
    def print(self):
                
        if self.head is None:
            print("Linked Lst is empty!")
            return 
        
        node = self.head
        LL_string = ""
        while node != None:
            LL_string = LL_string + str(node.data)+" --> "
            node = node.next
        print("HEAD--> "+LL_string+"Null") 
    
    def insert_values(self, data_list):
        self.head = None
        for val in data_list:
            self.insert_at_end(val)
            
    def length(self):
        
        if self.head is None:
            return 0
        itr = self.head
        ctr=0
        while itr != None:
            itr = itr.next
            ctr+=1
        return ctr
        
    def remove_at(self, idx):
        if self.length() < idx+1:
            print("Linked List not long enough. idx exceeds bounds.")
            return
        if idx == 0:
            self.head = self.head.next
            return
        
        ctr = 0 
        itr = self.head
        
        while ctr < idx-1:
            itr = itr.next
            print(ctr)
            ctr+=1
            
        print(ctr)
        temp = itr.next 
        itr.next = temp.next
    
    def insert_at(self, idx,data):
        if self.length() < idx:
            print("Invalid index")
            return
        if idx ==0:
            self.insert_at_beg(data)
        
        ctr=0
        itr=self.head   
        while ctr < idx -1:
            itr=itr.next
            ctr+=1
        newNode = Node(data, itr.next)
        itr.next=newNode 
        




if __name__== '__main__':
    LL = LinkedList()
    LL.insert_at_beg(5)
    LL.print()
    LL.insert_at_beg(10)
    LL.insert_at_beg(30)
    LL.insert_at_end(25)
    LL.insert_at_beg(45)
    LL.insert_at_end(46)
    LL.print()
    
    newLL = LinkedList()
    value_list = [10,20,30,40,50,70,90,100000,11]
    newLL.insert_values(value_list)
    newLL.print()
    l = newLL.length()
    print(l)
    newLL.remove_at(2)
    newLL.print()
    print(newLL.length())
    
    newLL.insert_at(3, 'adam')
    newLL.print()
    print(newLL.length())



