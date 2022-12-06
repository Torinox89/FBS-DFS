from collections import deque
Q = deque() #we will use the deque Q as a queue

"""
V (list) : The nodes that have been visited, in visitation order.
Q (queue): The nodes to be visited, in the order that they were discovered. 
     Recall that a queue is a FIFO data structure.
M (set): The nodes that have been visited, or that are marked to be visited. 
     This is the union of the nodes in V and Q.
"""

"""
Breadth-first traversal

Q.add(root)
M.add(root)

while not isempty(Q):
	cur = Q.pop()
	V.append(cur)
	for child in cur.children:
		if child not in M:
	    	Q.add(child)	
			M.add(child)
"""

"""
Breadth-first search

Q.add(root)
M.add(root)

while not isempty(Q):
	cur = Q.pop()
	if cur == to_find:
    	return True #we have found what we were looking for
          
	V.append(cur)
	for child in cur.children:
		if child not in M:
	    	Q.add(child)	
			M.add(child)

return False #element is not in tree
"""

"""
V (list) : The nodes that have been visited, in visitation order.
Q (queue): The nodes to be visited, in the order that they were discovered. 
     Recall that a queue is a FIFO data structure.
M (set): The nodes that have been visited, or that are marked to be visited. 
     This is the union of the nodes in V and Q.
"""

"""
Breadth-first traversal

Q.add(root)
M.add(root)

while not isempty(Q):
	cur = Q.pop()
	V.append(cur)
	for child in cur.children:
		if child not in M:
	    	Q.add(child)	
			M.add(child)
"""

"""
Breadth-first search

Q.add(root)
M.add(root)

while not isempty(Q):
	cur = Q.pop()
	if cur == to_find:
    	return True #we have found what we were looking for
          
	V.append(cur)
	for child in cur.children:
		if child not in M:
	    	Q.add(child)	
			M.add(child)

return False #element is not in tree
"""

class Node:     # TreeNode
  def  __init__(self, key):
    if key == "null":
      self.data = None
    else:
      self.data = key
    self.left = None
    self.right = None
  
def levelMax(root):
  """
  Breadth-first traversal
  
  Q.add(root)
  M.add(root)
  
  while not isempty(Q):
    cur = Q.pop()
    V.append(cur)
    for child in cur.children:
      if child not in M:
          Q.add(child)  
        M.add(child)
  """
  Q = deque()
  V = []
  M = set()
  bigs = []

  #add root to Q
  Q.appendleft(root)

  while len(Q) != 0:
    big = 0
    for _ in range(len(Q)): #this will only go through one level at a time
      cur = Q.pop()
      V.append(cur)
      if cur.data > big:
        big = cur.data
      for child in [cur.left,cur.right]:
        if child not in M and child != None:
          Q.appendleft(child)  
          M.add(child)
    bigs.append(big)  
  return bigs
  
def max_levels(lst):
  levels = 0
  for i in range(10):
    if len(lst) == 2**i - 1:
      levels = i + 1 # number of levels is not 0-indexed
      break

  root = Node(lst[0])
  root.left = Node(lst[1])
  root.right = Node(lst[2])
  root.left.left = Node(lst[3])
  root.left.right = Node(lst[4])
  #root.right.left = Node(lst[5]) (we skip this to avoid problems)
  root.right.right = Node(lst[6])

  print(levelMax(root))

max_levels([5, 3, 8, 2, 4, 'null', 9])