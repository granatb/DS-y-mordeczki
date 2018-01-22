class BST:

	class Node:
		def __init__(self,val,left,right):
			self.elem=val
			self.left=left
			self.right=right
	
	def __init__(self):
		self.__root=None
		self.__n=0
	
	def __len__(self):
		return self.__n

	def insert(self,val):
		if self.__n==0: #równoważne z: if self.__root is None
			self.__root=BST.Node(val,None,None)
			self.__n=1
		else:
			cur=self.__root
			while True:
				if val==cur.elem:
					return
				elif val<cur.elem:
					if cur.left is None:
						cur.left=BST.Node(val,None,None)
						self.__n+=1
						return
					else:
						cur=cur.left
				else:
					if cur.right is None:
						cur.right=BST.Node(val,None,None)
						self.__n+=1
						return
					else:
						cur=cur.right

	def search(self,val):
		cur=self.__root
		while cur is not None:
			if cur.elem==val:
				return True
			elif val<cur.elem:
				cur=cur.left
			else:
				cur=cur.right
		return False

	def show(self):

		def __show(cur):
			if cur is None:
				return
			__show(cur.left)
			print(cur.elem)
			__show(cur.right)

		__show(self.__root)

	def delete(self,val):

		#znajdowanie
		cur=self.__root
		parent=None
		pardir=None
		while cur is not None:
			if cur.elem==val:
				wyraz=cur
				break
			elif val<cur.elem:
				parent=cur
				pardir="L"
				cur=cur.left
			else:
				parent=cur
				pardir="R"
				cur=cur.right
		if cur is None:
			raise Exception(str.format("{0} nie jest elementem BST",val))

		def __delete(node,parent,pardir):
			#gdy node nie ma dzieci
			if node.left==None and node.right==None:
				if parent is None and pardir is None:
					self.__root=None
				elif pardir=="L":
					parent.left=None
				else:
					parent.right=None

			#gdy node ma 1 dziecko
			elif node.left is not None and node.right is None:
				if parent is None and pardir is None:
					self.__root=self.__root.left
				elif pardir=="L":
					parent.left=node.left
				else:
					parent.right=node.left
			elif node.right is not None and node.left is None:
				if parent is None and pardir is None:
					self.__root=self.__root.right
				elif pardir=="L":
					parent.left=node.right
				else:
					parent.right=node.right

			#gdy node ma 2 dzieci
			else:
				cur=node.left
				if cur.right is None:
					cur.right=node.right
					if node.elem==self.__root.elem:
						self.__root=cur
					elif pardir=="L":
						parent.left=node.left
					else:
						parent.right=node.left
				else:
					while cur.right is not None:
						parcur=cur
						cur=cur.right
					node.elem=cur.elem
					if cur.left is None:
						parcur.right=None
					else:
						parcur.right=cur.left

		__delete(wyraz,parent,pardir)
		self.__n-=1
"""
d=BST()

import random
x=[0]*100
for i in range(100):
	v = random.randint(0,10000)
	print(v)
	d.insert(v)
	x[i]=v
print()
for i in range(100):
	print("len=",len(d))
	d.delete(x[i])
	d.show()
	print()
"""
