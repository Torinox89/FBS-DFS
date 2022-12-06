"""
V (list) : The nodes that have been visited, in visitation order.
S (stack): The nodes to be visited, in the order that they were discovered. 
     Recall that a stack is a FILO data structure.
M (set): The nodes that have been visited, or that are marked to be visited. 
     This is the union of the nodes in V and S.
"""

"""
Depth-first search

S.add(root)
M.add(root)

while not isempty(S):
	cur = S.pop()
	if cur == to_find:
    	return True #we have found what we were looking for
          
	V.append(cur)
	for child in cur.children:
		if child not in M:
	    	S.add(child)
			M.add(child)

return False #element is not in tree
"""
