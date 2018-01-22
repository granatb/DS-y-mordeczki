class BST:
	
	class Node:
		def __init__(self, val, left, right):
			self.val = val
			self.left = left
			self.right = right
			
	def __init__(self):
		self.root = None
		self.n = 0
		
	def __len__(self):
		return self.n
	
	def insert(self, val):
		if self.root is None:
			self.root = BST.Node(val, None, None)
			self.n = 1
		else:
			cur = self.root
			while True:
				if val == cur.val: return #nie wstawiamy duplikatow
				elif val < cur.val:
					if cur.left is None:
						# wstawiamy
						cur.left = BST.Node(val, None, None)
						self.n += 1
						return
					else:
						cur = cur.left
				else:
					if cur.right is None:
						cur.right = BST.Node(val, None, None)
						self.n += 1
						return
					else:
						cur = cur.right
						
	def search(self, val):
		cur = self.root
		while cur is not None:
			if val == cur.val: return True
			elif val < cur.val: cur = cur.left
			else: cur = cur.right
		return False
	
	def show(self):
		def _show(cur):
			# in-order
			if cur is None: return
			_show(cur.left)
			print(cur.val)
			_show(cur.right)
			
		_show(self.root)

	def delete(self, val):
		def find_Node(self, val):
			cur = self.root
			while True:
				if cur.val == val: return cur
				elif val < cur.val:
					cur = cur.left
				else:
					cur = cur.right
		Node = find_Node(self, val)
		
		
		
		if Node.right == None and Node.left == None:
			cur = self.root
			while True:
				
				if val < cur.val:
					if cur.left.val == val: 
						cur.left = None
						break
					else: cur = cur.left
					
				else:
					if cur.right.val == val:
						cur.right = None
						break
					else: cur = cur.right
		elif Node.right == None:
			cur = self.root
			while True:
				if val == self.root.val:
					self.root = self.root.left
					break
				
				elif val < cur.val:
					if cur.left.val == val: 
						cur.left = Node.left
						break
					else: cur = cur.left
					
				else:
					if cur.right.val == val:
						cur.right = Node.left
						break
					else: cur = cur.right
		
		elif Node.left == None:
			cur = self.root
			while True:
				print(cur.val)
				if val == self.root.val:
					self.root = self.root.right
					break
				
				elif val < cur.val:
					if cur.left.val == val: 
						cur.left = Node.right
						break
					else: cur = cur.left 
				elif val == self.root.val:
					self.root = self.root.right
					
				else:
					if cur.right.val == val:
						cur.right = Node.right
						break
					else: cur = cur.right
		elif Node.left is not None and Node.right is not None:
			cur = Node
			right_min = cur.right
			
			while right_min.left is not None:
				right_min = right_min.left
				
			

			
			cur = find_Node(self, self.root.val)
			i = 0
			while True:
				
					
			
				
				if right_min.val < cur.val:
					if cur.left.val == right_min.val: 
						cur.left.right = right_min.right
						break
					else: cur = cur.left
					
				else:
					if cur.right.val == right_min.val: 
						cur.left.right = right_min.right
						break
					
					else: cur = cur.right
			
			
			cur = self.root
			while True:
				if cur.val == val: 
					cur.val = right_min.val
					break
				elif val < cur.val:
					cur = cur.left
				else:
					cur = cur.right
		self.n -= 1
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
					
A = BST()
A.insert(8)

A.insert(9)
A.insert(8.5)
A.insert(9.5)


A.show()
A.delete(8)
A.show()
		
		
		
		
		
		
