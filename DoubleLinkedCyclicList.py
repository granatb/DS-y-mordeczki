
# coding: utf-8

# In[18]:


class LinkedList:
    """
    sruktura danych zawierajaca polaczane wezly przechowujace:
    element
    wskaznik na kolejny wezel
    opcjonalnie wskaznik na poprzedni wezel
    """
    
    class __Node:
        """
        ukryta podklasa pomocnicza symbolizujaca wezly
        """
        
        def __init__(self, value, next, prev):
            """
            konstruktor wezla
            """
            self.value=value
            self.next=next
            self.prev=prev
    
    def __init__(self):
        """
        konstruktor LinkedList
        Head - korzen, pierwszy element listy
        n - dlugosc listy
        """
        self.__head=LinkedList.__Node(None, None, None)
        self.__head.prev=self.__head
        self.__head.next=self.__head
        self.__n=0
        
    def __len__(self):
        """
        wyswietlanie dlugosci listy
        """
        return self.__n
    
    def __repr__(self):
        """
        wypisanie zawartosci listy
        """
        s="["
        cur = self.__head
        for i in range(self.__n):
            s+=repr(cur.value)
            if not i == self.__n-1:
                s+="->"
            cur = cur.next
        s+="]"
        return s
    
    def __getitem__(self, index):
        """
        wypisanie i-tego elementu
        """
        assert self.__n > 0 and index < self.__n, "Index out of range"
        cur = self.__head
        for i in range(index):
            cur=cur.next
        return cur.value
    
    def push_front(self, value):
        """
        dodanie wartosci na poczatku listy
        """
        if self.__head.value is None:
            self.__head.value = value
            self.__n+=1
        else:
            self.__head = LinkedList.__Node(value, self.__head, self.__head.prev)
            self.__n+=1
        self.__head.prev.next=self.__head
        self.__head.next.prev=self.__head

    def push_back(self, value):
        """
        Dodanie wartosci na koncu listy
        """
        if self.__head.value is None:
            self.__head.value = value
            self.__n+=1
        else:
            self.__head.prev.next = LinkedList.__Node(value, self.__head, self.__head.prev)
            self.__head.prev = self.__head.prev.next
            self.__n+=1
        
    def pop_front(self):
        """
        zwrocenie wartosci z poczatku listy
        """
        assert self.__n > 0, "List is empty"
        if self.__n == 1:
            val = self.__head.value
            self.__head.value = None
            self.__n-=1
            return val
        popped = self.__head
        self.__head = popped.next
        self.__head.prev = popped.prev
        self.__n -= 1
        return popped.value
    
    def pop_back(self):
        """
        zwrocenie wartosci z konca listy
        """
        assert self.__n > 0, "List is empty"
        if self.__n == 1:
            val = self.__head.value
            self.__head.value = None
            self.__n -= 1
            return val
        popped = self.__head.prev
        self.__head.prev = popped.prev
        self.__head.prev.next = self.__head
        self.__n -= 1
        return popped.value
        
    def push(self, index, value):
        """
        dodaj wartosc do listy po zadanych indeksie
        """
        assert 0 <= index < self.__n, "Index out of range"
        cur = self.__head
        for i in range(index):
            cur = cur.next
        cur.next=LinkedList.__Node(value, cur.next, cur)
        cur.next.next.prev = cur.next
        self.__n+=1
        
    def pop(self, index):
        """
        zwroc wartosc o podanym indeksie
        """
        assert 0 <= index < self.__n
        if index == 0: return self.pop_front()
        elif index == self.__n-1: return self.pop_back()
        else:
            cur = self.__head
            for i in range(index-1):
                cur = cur.next
            popped = cur.next
            popped.next.prev = cur
            cur.next = popped.next
            self.__n -= 1
            return popped.value
            


# In[19]:


ll = LinkedList()


# In[20]:


import random
for i in range(15):
    ll.push_front(random.randint(0,10))


# In[27]:


len(ll)


# In[26]:


print(ll)


# In[25]:


ll.pop(13)


# In[3]:


len("-17")

