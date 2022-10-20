class Node:
 
    
    def __init__(self, data):
        """
        Constructor to initialize the node object
        """
        self.data = data
        self.next = None
 
class LinkedList:
 
    
    def __init__(self):
        """
        Function to initialize head

        """
        self.head = None
 
    
    def append(self, new_data):
        """
        Function to insert a new node at the beginning
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    
    def deleteNode(self, key):
        """
        Given a reference to the head of a list and a key,
        delete the first occurrence of key in linked list
        
        """
         
       
        temp = self.head
 
        
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
 
        
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        
        if(temp == None):
            return
 
        
        prev.next = temp.next
 
        temp = None
 
 
    
    def printList(self):
        """
        Utility function to print the linked LinkedList
        """


        temp = self.head
        while(temp):
            print (" %d" %(temp.data)),
            temp = temp.next
 
if __name__ == "__main__":


    llist = LinkedList()
    llist.append(9)
    llist.append(1)
    llist.append(5)
    llist.append(4)
    
    print ("Created Linked List: ")
    llist.printList()
    x=int(input("pls enter the node you want to delete "))
    llist.deleteNode(x)
    print (f"Linked List after Deletion of {x}")
    llist.printList()