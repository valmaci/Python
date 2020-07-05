import numpy as np

# Course: CS2302 Data Structures
# Author: Valeria Macias
# Assignment: HashTable Linear Probing
# Instructor: Olac Fuentes
# T.A.: Ismael Villanueva-Miranda
# Date of Last Modification: 7/21/19
# Purpose: HashTable Linear Probing implementation using np array and corresponding 
#           algorithms. Hash is value of item % table length. -1 is empty. -2 is deleted.

class HashTableI(object):
  # Builds a hash table of size ‘size’, initializes items to -1 (which means empty)
  # Constructor
  def __init__(self, size):
    self.item = np.zeros(size, dtype = np.int) -1
    
# Inserts k in H and returns position or -1 if H is full
def insert(H, k):
  for i in range(len(H.item)):
    pos = (k+i)%len(H.item)
    if H.item[pos] < 0:
      H.item[pos] = k 
      return pos
  return -1
  
# Returns the position of k in H, or -1 if k is not in the table
def find(H, k):
  for i in range(len(H.item)):
    pos = (k+i)%len(H.item)
    if H.item[pos] == k:
      return pos
    if H.item[pos] == -1:
      return -1
  return -1
  
# Deletes k from H and returns position were k was or -1 if not in table. Then 
# sets table item where k was to -2.
def delete(H, k):
  f = find(H, k)
  if f >= 0:
    H.item[f] = -2
  return f 
  
# Returns the amount of items in table.
def total_items(H):
  sum = 0
  for i in range(len(H.item)):
    if H.item[i] >= 0:
      sum += 1
  return sum
  
# Returns the number of items in table divided by capacity. 
  # Ideal load factor is less than 1.
def load_factor(H):
  return total_items(H) / len(H.item)
  

# Inserts k in table if k is not already in table.  
def insert_no_duplicates(H, k):
  if find(H, k) < 0:
    insert(H, k)
  return

# Returns the largest element in the table that has the same hash value as k, or -1 if no element in H has the same hash value as k.
def largest_with_hash_k(H, k):
  i = k%len(H.item)
  largest = H.item[i]
  j = i
  while H.item[j] % len(H.item) == i:
    if H.item[j] > largest:
      largest = H.item[j]
    j += 1
  return largest
