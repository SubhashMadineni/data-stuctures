# -*- coding: utf-8 -*-
"""Graph Algos Implementation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V8XFXf8yCOThFsya3WT-YtOtDp6Dr4Yl
"""

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    
  # Method to add new node into LL at the end
  def atEnd(self, data):
    NewNode = Node(data)              #creating new box ie..Node

    if self.head is None:
      self.head = NewNode             #IF head is null insertion at lead happens
      return

    last_ele = self.head

    while( last_ele.next):
      last_ele = last_ele.next        #travesing till the last Box

    last_ele.next = NewNode           #Joining new box at the end of Last Box

  def printList(self):
    temp = self.head                  #capturing the head
    while temp is not None:           #traversing till the end

      print(temp.data)
      temp = temp.next


ll = LinkedList()

ll.atEnd(1)
ll.atEnd(2)
ll.atEnd(3)
ll.atEnd(4)
ll.atEnd(5)
ll.atEnd(6)
ll.atEnd(7)
ll.atEnd(8)
ll.atEnd(9)

ll.printList()

# Python program to find the longest substring with k unique 
# characters in a given string 
MAX_CHARS = 26

# This function calculates number of unique characters 
# using a associative array count[]. Returns true if 
# no. of characters are less than required else returns 
# false. 
def isValid(count, k): 
	val = 0
	for i in range(MAX_CHARS): 
		if count[i] > 0: 
			val += 1

	# Return true if k is greater than or equal to val 
	return (k >= val) 

# Finds the maximum substring with exactly k unique characters 
def kUniques(s, k): 
	u = 0 # number of unique characters 
	n = len(s) 

	# Associative array to store the count 
	count = [0] * MAX_CHARS 

	# Tranverse the string, fills the associative array 
	# count[] and count number of unique characters 
	for i in range(n): 
		if count[ord(s[i])-ord('a')] == 0: 
			u += 1
		count[ord(s[i])-ord('a')] += 1

	# If there are not enough unique characters, show 
	# an error message. 
	if u < k: 
		print ("Not enough unique characters") 
		return

	# Otherwise take a window with first element in it. 
	# start and end variables. 
	curr_start = 0
	curr_end = 0

	# Also initialize values for result longest window 
	max_window_size = 1
	max_window_start = 0

	# Initialize associative array count[] with zero 
	count = [0] * len(count) 

	count[ord(s[0])-ord('a')] += 1 # put the first character 

	# Start from the second character and add 
	# characters in window according to above 
	# explanation 
	for i in range(1,n): 

		# Add the character 's[i]' to current window 
		count[ord(s[i])-ord('a')] += 1
		curr_end+=1

		# If there are more than k unique characters in 
		# current window, remove from left side 
		while not isValid(count, k): 
			count[ord(s[curr_start])-ord('a')] -= 1
			curr_start += 1

		# Update the max window size if required 
		if curr_end-curr_start+1 > max_window_size: 
			max_window_size = curr_end-curr_start+1
			max_window_start = curr_start 

	print ("Max substring is : " + s[max_window_start:max_window_start + max_window_size] 
	+ " with length " + str(max_window_size)) 

# Driver function 
s = "aabacbebebe"
k = 3
kUniques(s, k) 

# This code is contributed by BHAVYA JAIN



def lengthOfLongestSubstring(self, s: str) -> int:
    charSet = set()
    l = 0
    r = 0
    res = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res,r-l+1)
    
    return res

# linked list cycle 2
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None or head.next == None : return
        slow = ListNode()
        fast = ListNode()
        slow.next = head
        fast.next = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast: break
                
        if not fast or not fast.next: return None
         
        while(head != slow):
            slow = slow.next
            head = head.next
            
        return slow

class ListNode:
    def __init__(self,data):
        self.val = data
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        temp = self.head
        for _ in range(index+1):
            temp = temp.next
        return temp.val
        

    def addAtHead(self, val: int) -> None:

        nn  = ListNode(val)
        nn.next = self.head.next
        self.head.next = nn
        self.length +=1
        
    def addAtTail(self, val: int) -> None:

        nn =ListNode(val)
        temp = self.head
        for _ in range(self.length) :
            temp = temp.next
        temp.next = nn
        self.length += 1
            

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index >= self.length:
            return -1
        nn = ListNode(val)
        temp = self.head
        for _ in range(index):
            temp = temp.next
        nn.next = temp.next
        temp.next = nn
        self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.length:
            return -1

        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.next = temp.next.next
        self.length -= 1
        

# ["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
# [[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]

#Bst Implementation

class Node:
  def __init__(self,value = None):
    self.value = value
    self.left = None
    self.right = None
    self.parent = None

class bst:
  def __init__(self):
    self.root = None 
  
  def insert(self,value):
    if self.root == None:
      self.root = Node(value)
    else:
      self._insert(value,self.root)
  def _insert(self,value,curr_node):
    if value < curr_node.value:
      if curr_node.left == None:
        curr_node.left = Node(value)
        curr_node.left.parent = curr_node   #parent
      else:
        self._insert(value,curr_node.left)


    elif value > curr_node.value:
      if curr_node.right == None:
        curr_node.right = Node(value)
        curr_node.right.parent = curr_node         #parent
      else:
        self._insert(value,curr_node.right)
    
    else:
      print("Value already in Tree")

  def height_tree(self):
    if self.root != None :
      return self._height(self.root,0)
    else: return 0
  def _height(self, curr_node, curr_height):
    if curr_node == None: return curr_height
    left_height = self._height(curr_node.left, curr_height +1)
    right_height = self._height(curr_node.right, curr_height +1)
    return max(left_height, right_height)

  #Returns the Node with specified input Value 
  def find(self,value):
    if self.root != None: return self._find(value,self.root)
    else: return None
  def _find(self, value, curr_node):
    if value == curr_node.value: return curr_node
    elif value < curr_node.value and curr_node.left != None: return self._find(value, curr_node.left)
    elif value > curr_node.value and curr_node.right != None: return self._find(value, curr_node.right)

  def delete_value(self,value):return self.delete_node(self.find(value))
  def delete_node(self, node):
    if node ==None or self.find(node.value) == None:
      print("Node to be deleted not found")
      return None
    #returns the node with min value in tree rooted at input node
    def min_value_node(n):
      current = n
      while current.left != None:
        currnt = current.left
      return current
    
    #return the number of childern for the specified node
    def num_childern(n):
      num_childern = 0
      if n.left != None: num_childern += 1
      if n.right != None: num_childern += 1
      return num_childern
    #get the parent of the node to be deleted
    node_parent = node.parent

    #get the number of childern of node to be deleted
    node_childern = num_childern(node)

    #(case1) Node has 0 childern---------------------------------------------------->1
    if node_childern == 0:
      #remove the referneceto the node from the parent
      if node_parent.left == node: node_parent.left = None
      else: node_parent.right = None

    #case 2 (node has a single child)------------------------------------------------->2
    if node_childern == 1:
      #get the single node child
      if node.left != None: child = node.left
      else: child = node.right

      #replace the node to be deleted with its child
      if node_parent.left == Node: node_parent.left = child
      else: node_parent.right = child

      child.parent = node.parent

    #case 3 (node has 2 childern)------------------------------------------------------>3
    if node_childern == 2:
      #get the inorder sucessor of the deleted node
      successor = min_value_node(node.right)

      # copy the inorder successor value into the node we wish to delete
      node.value = successor.value

      #delete the inorder successor of the node now that its value has been copied
      self.delete_node(successor)



  #returns true if given value exists in the tree
  def search(self, value):
    if self.root != None:
      return self._search(value,self.root)
    else:
      return False
  def _search(self, value, curr_node):
    if value == curr_node.value: return True
    elif value < curr_node.value and curr_node.left != None:
      return self._search(value,curr_node.left)
    elif value > curr_node.value and curr_node.right != None:
      return self._search(value,curr_node.right)
    return False
  def print_tree(self):
    if self.root != None:
      self._print_tree(self.root)
  def _print_tree(self,curr_node):
    if curr_node != None:
      self._print_tree(curr_node.left)
      print(str(curr_node.value))
      self._print_tree(curr_node.right)


def fill_tree(tree,num_eles = 100, max_int = 1000):
  from random import randint
  for _ in range(num_eles):
    curr_ele = randint(0,max_int)
    tree.insert(curr_ele)

tree = bst()
#fill_tree(tree)
tree.insert(5)
tree.insert(4)
tree.insert(6)
tree.insert(10)
tree.insert(9)
tree.insert(11)

tree.print_tree()
print("Height of tree: "+str(tree.height_tree()))

tree.delete_value(9)
tree.print_tree()



nodes = [0,1,2,3,4,5]

edges = {(0,1):1,
         (0,2):1.5,
         (0,3):3,
         (1,4):2.5,
         (1,3):0.5,
         (2,3):1.5,
         (3,5):1,
         (4,5):2
}


# adjacent_nodes = {v: {} for v in nodes}

# for (u,v),w_uv in edges.items():

#   adjacent_nodes[u][v] = w_uv       
#   adjacent_nodes[v][u] = w_uv

# adjacent_nodes

distance = {v:float('inf') for v in nodes} 
distance



nodes = [0,1,2,3,4,5]

edges = {(0,1):1,
         (0,2):1.5,
         (0,3):3,
         (1,4):2.5,
         (1,3):0.5,
         (2,3):1.5,
         (3,5):1,
         (4,5):2
}


def dijkstra(nodes, edges, source_index = 0):
  #step1
  distance = {v:float('inf') for v in nodes} 
  distance[source_index] = 0

  #step2
  #creating an adjacent nodes dictionary for all the surrounding nodes of the source node

  adjacent_nodes = {v: {} for v in nodes}

  for (u,v),w_uv in edges.items():

    adjacent_nodes[u][v] = w_uv        #[u]. ---> key of main dict  [v] key of sub dict.  w_uv ---> value
    adjacent_nodes[v][u] = w_uv

  temp_nodes = [v for v in nodes]

  while len(temp_nodes) > 0:
    upper_bounds = {v:distance[v] for v in temp_nodes}
    u = min(upper_bounds,key = upper_bounds.get)
    temp_nodes.remove(u)

    for v, w_uv in adjacent_nodes[u].items():
      distance[v] = min(distance[v], distance[u]+w_uv) 

  return distance

dijkstra(nodes, edges, source_index = 1)



























