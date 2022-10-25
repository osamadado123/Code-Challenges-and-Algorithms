class Node:
    
	def __init__(self, new_data):
		self.data = new_data
		self.next = None
class LinkedList:

	def __init__(self):
		self.head = None

	
	def append(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def deleteNode(self, n):
		first = self.head
		second = self.head
		for i in range(n):
			
			
			if(second.next == None):
				
				
				if(i == n - 1):
					self.head = self.head.next
				return self.head
			second = second.next
		
		while(second.next != None):
			second = second.next
			first = first.next
		
		first.next = first.next.next
	
	def printList(self):
                x=[]
                tmp_head = self.head
                while(tmp_head != None):
                    print(tmp_head.data, end = ' ')
                    x.append(tmp_head.data)
                    tmp_head = tmp_head.next
                return x

llist = LinkedList()
llist.append(5)
llist.append(4)
llist.append(3)
llist.append(2)
llist.append(1)
print("Created Linked list is:")
llist.printList()
llist.deleteNode(2)
print("\nLinked List after Deletion is:")
llist.printList()