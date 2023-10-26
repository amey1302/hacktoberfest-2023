# Node class 

class Node: 

	# Constructor to initialize the node object 
	def __init__(self, data): 
		self.data = data 
		self.next = None

class LinkedList: 
	# Function to initialize head 
	def __init__(self): 
		self.head = None

	#Function to reverse a LL
	def reverse(self): 
		prev = None
		current = self.head 
		while(current is not None): 
			next = current.next
			current.next = prev 
			prev = current 
			current = next
		self.head = prev 

	# Function to insert a new node at the beg
	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	# function to print the LinkedList 
	def printList(self): 
		temp = self.head 
		while(temp): 
			print (temp.data,end=" ") 
			temp = temp.next


# Driver program to test above functions 
ll = LinkedList() 
ll.push(40) 
ll.push(90) 
ll.push(12) 
ll.push(89) 
ll.push(78) 
print ("-----Original Linked List--------") 
ll.printList() 
ll.reverse() 
print ("\n-----Reversed Linked List-----------") 
ll.printList() 

