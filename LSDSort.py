
# coding: utf-8

# In[62]:


def isSorted(t):
    n = len(t)
    for i in range(1,n):
        if t[i] < t[i-1]:return False
    return True

def LSD_sort(t):
    """
    sortowanie pozycyjne względem najmniej znaczącej cyfry
    """
    def list_to_buckets(t, i, base = 10):
        buckets = [[] for _ in range(base)]
        for e in t:
            buckets[(e%(base**i))//(base**(i-1))].append(e)
        return buckets
    
    def buckets_to_list(buckets):
        t  = []
        for bucket in buckets:
            for element in bucket:
                t.append(element)
        return t
    
    for i in range(1, len(str(max(t)))+1):
        t = buckets_to_list(list_to_buckets(t, i))
    assert isSorted(t)
    return t


# In[67]:


import random
t = [0]*500
for i in range(500):
    t[i] = random.randint(0, 1000)
t = LSD_sort(t)


# In[68]:


print(t)


# In[69]:


isSorted(t)


# In[46]:


LSD_sort(t)

