
# coding: utf-8

# In[193]:


class BST:

    class Node:
        def __init__(self, value, left = None, right = None):
            self.value = value
            self.left = left
            self.right = right
        def __repr__(self):
            string = "Value: {0}\n".format(self.value)
            if self.left is not None:
                string += "Left child: {0}\n".format(self.left.value)
            else:
                string += "Left child: None\n"
            if self.right is not None:
                string += "Right child: {0}\n".format(self.right.value)
            else:
                string += "Right child: None\n"
            return string

    def __init__(self):
        self.__root = None
        self.__n = 0
        
    def add(self, value):
        if self.__root == None:
            self.__root = BST.Node(value)
            self.__n += 1
            return
        cur = self.__root
        while True:
            if value < cur.value:
                if cur.left is None:
                    cur.left = BST.Node(value)
                    self.__n += 1
                    return
                else:
                    cur = cur.left
            elif value > cur.value:
                if cur.right is None:
                    cur.right = BST.Node(value)
                    self.__n += 1
                    return
                else:
                    cur = cur.right
            else:
                return
            
    def delete(self, value):
        assert self.__n > 0
        if value == self.__root.value:
            right_branch_min = self.__root.right
            if self.__root.right is not None:
                while right_branch_min.left is not None:
                    right_branch_min = right_branch_min.left
            if right_branch_min is None:
                self.__root = self.__root.left
                self.__n -= 1
                return
            right_branch_min.left = self.__root.left
            self.__root = self.__root.right
            self.__n -= 1
            return
        cur = self.__root
        while True: #W tej pętli szukamy Node-a, w którym znajduje się szukana wartość
            if value < cur.value:
                if cur.left is None: return
                parent = cur
                isLeft = True
                cur = cur.left
            elif value > cur.value:
                if cur.right is None: return
                parent = cur
                isLeft = False
                cur = cur.right
            else:
                break
        right_branch_min = cur.right
        if cur.right is not None:
            while right_branch_min.left is not None:
                right_branch_min = right_branch_min.left
        if isLeft:
            if right_branch_min is None:
                parent.left = cur.left
                self.__n -= 1
            else:
                right_branch_min.left = cur.left
                parent.left = cur.right
                self.__n -= 1
        else:
            if right_branch_min is None:
                parent.right = cur.left
                self.__n -= 1
            else:
                right_branch_min.left = cur.left 
                parent.right = cur.right 
                self.__n -= 1
    
    def __repr__(self):
        def _traverse(node, values):
            if node is None:
                return
            _traverse(node.left, values)
            values.append(node.value)
            _traverse(node.right, values)
        values = []
        if self.__root is None: return "None"
        _traverse(self.__root, values)
        return str(values)
    
    def __len__(self):
        return self.__n
    
    def root(self):
        return self.__root


# In[194]:


import random
B = BST()


# In[196]:


for i in range(100):
    B.add(random.randint(0,100))
    print(B)
for i in range(100):
    v = random.randint(0,100)
    print(v)
    print(B.root())
    B.delete(v)
    print(B)


# In[195]:


B.add(9)
B.add(6)
print(B.root())
B.delete(9)
print(B.root())


# In[221]:


print(B.root())
B.delete(B.root().value)
print(B)
print(B.root())

