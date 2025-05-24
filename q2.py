from dataclasses import dataclass

@dataclass
class Node:
    """Implements a (singly) linked-list node 

    For a Node n:
        n.data holds an integer value
        n.next refers to the next Node in the linked list, or None

    You must not modify this code.
    """
    data: int
    next: 'Node' = None

@dataclass
class LinkedList:
    """Implements a (singly) linked-list 

    For a LinkedList ll:
        ll.head refers to a Node that is the head of the linked list, or None
        ll.size is the size of the linked list

    You must not modify this code.
    """
    head: Node = None
    size: int = 0

@dataclass
class LinkedListWithTail:
    """Implements a (singly) linked-list 

    For a LinkedList ll:
        ll.head refers to a Node that is the head of the linked list, or None
        ll.tail refers to a Node that is the tail of the linked list, or None
        ll.size is the size of the linked list

    You must not modify this code.
    """
    head: Node = None
    tail: Node = None
    size: int = 0


def show(linked_list):
 	#nodeBeingChecked has to be initialised at the linked-list head 
 nodeBeingChecked = linked_list.head
 #couldn't use for loop, as sample data is missing linkedlist size, so used while LOOP instead
 while nodeBeingChecked != None :
 	#each line printed part
  print(nodeBeingChecked.data)
  #basically acts as an iterative loop, updating the nodeBeingChecked by +1
  nodeBeingChecked = nodeBeingChecked.next
 

def cat(linked_list_a, linked_list_b):
 	#the edge cases (as if head is None, then there is no linked-list)
 if linked_list_a.head == None:
 	return linked_list_b
 	
 if linked_list_b.head == None:
 	return linked_list_a
 	
 concatenatedNode = linked_list_a.head
 #similiar to last question, it essentially iterates through linked_list_a until it reaches the tail, 
 #could be a quicker way with O(1) if given linkedlistA.tail, but we're not so O(n) for going through iteratively
 while concatenatedNode.next != None:
  	concatenatedNode = concatenatedNode.next
  	#once reached linklistA.tail iteratively,
  	#pretty easy last bit of just connecting tail of linkedlistA to the head of linkedlistB, and then return to definiton of function
 concatenatedNode.next = linked_list_b.head
 combinedLinkedList = linked_list_a
 return(combinedLinkedList)

def smart_cat(linked_list_a, linked_list_b):
 	#same edge case check for previous question concatenation
 if linked_list_a.head == None:
 	return linked_list_b
 	
 if linked_list_b.head == None:
 	return linked_list_a
 	
 	#alot simplier with defining linkedlistA tail as the head of linkedlistB (now this has time complexity O(1))
 concatenatedNodeII = linked_list_a.tail
 concatenatedNodeII.next = linked_list_b.head
 #redefined new variable incase returns the original linked_list_a
 combinedlistII = linked_list_a
 return(combinedlistII)
 

def make_queue():
	# create the nodes and give them data (example given on coursework question outline)
 N1 = Node(data=4)
 N2 = Node(data=9)
 N3 = Node(data=18)
 N4 = Node(data=3)
 N5 = Node(data=21)
 
 #introduce link stucture (middle nodes repetitive, but N5 is tail therefore .next = None/NULL)
 #
 N1.next = N2
 N2.next = N3
 N3.next = N4
 N4.next = N5
 N5.next = None
 #another attribute given to linkedlistwithtail as shown in question example
 linked_list_with_tail = LinkedListWithTail(head=N1, tail=N5, size=5)
 return(linked_list_with_tail)

def enqueue(ll_queue, value):
	#set up new new node (newN) and have the value of the second variable inputted
 newN = Node(data=value)
 # edge case if linkedlist is empty
 if ll_queue.head == None:
  ll_queue.tail = newN
  ll_queue.head = newN
  # anti-edge case (just enqueing to end), basically variable reassignment
 if ll_queue.head != None:
  ll_queue.tail.next = newN
  ll_queue.tail = newN	
  newN.next = None
  #update the size of the linkedlist manually
 ll_queue.size = ll_queue.size + 1 
 return(ll_queue)

def convert_to_array_queue(ll_queue):
	#initliase empty array of size 10, set makeshift iterative variable j = 0, and set queue head to a nodeBeingChecked to #tidy up code with less double dotting
 A = [""]*10
 nodeBeingChecked = ll_queue.head
 j = 0
 # if linkedlist is not empty and index is strictly less than 10
 while nodeBeingChecked != None and j<= 9:
 	# blank position in array is given linkedlist data
		A[j] = nodeBeingChecked.data
		# updating of j and nodeBeingChecked(for while to act like for loop)
		j = j+1
		nodeBeingChecked = nodeBeingChecked.next
		#only parts after nodes containing data are given None, be restricting the range
 for i in range(j,10):
   A[i] = None
 f = 0
 r = j-1
 LLtuple = (A,r,f)
 return(LLtuple)


