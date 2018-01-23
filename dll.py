class LinkedList:

	class Node:
		def __init__(self, elem, next, prev):
			self.elem = elem
			self.next = next
			self.prev = prev

	def __init__(self):
		self.__head = LinkedList.Node(None,None,None)
		self.__n= 0

	def __len__(self):
		return self.__n

	def push_front(self, elem):
		if self.__n==0:
			self.__head = LinkedList.Node(elem, self.__head,self.__head)
			self.__head.next.prev=self.__head
			self.__head.prev.next=self.__head
		else:
			self.__head=LinkedList.Node(elem,self.__head,self.__head.prev)
			self.__head.prev.next=self.__head
			self.__head.next.prev=self.__head
		self.__n += 1

	def push_back(self, elem):
		if self.__n==0:
			self.__head = LinkedList.Node(elem, self.__head,self.__head)
			self.__head.next.prev=self.__head
			self.__head.prev.next=self.__head
		else:
			self.__head.prev.prev=LinkedList.Node(elem,self.__head.prev,self.__head.prev.prev)
			self.__head.prev.prev.prev.next=self.__head.prev.prev
		self.__n += 1

	def pop_front(self):
		assert self.__n > 0
		box = self.__head
		if self.__n==1:
			self.__head=LinkedList.Node(None,None,None)
		else:
			box.next.prev=self.__head.prev
			box.prev.next=self.__head.next
			self.__head=box.next
		self.__n -= 1
		return box.elem

	def pop_back(self):
		assert self.__n>0
		box = self.__head.prev.prev
		if self.__n==1:
			self.__head=LinkedList.Node(None,None,None)
		else:		
			box.next.prev=box.prev
			box.prev.next=box.next
		self.__n-=1
		return box.elem

	def __getitem__(self,i):
		assert self.__n>0 and i<self.__n and i>=0
		cur=self.__head
		for j in range(i):
			cur=cur.next
		return cur.elem

	def __repr__(self):
		s = "["
		cur = self.__head
		while cur.elem is not None: # while cur itp.
			s += repr(cur.elem)
			if cur.next.elem is not None: s += ","
			cur = cur.next
		s += "]"
		return s

###
l = LinkedList()

for i in range(5): 
	l.push_front(i+1)
	l.push_back(1/(i+1))
print(l)
for i in range(5):
	print(l.pop_front())
	print(l)
	print(l.pop_back())
	print(l)
