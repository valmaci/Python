# Course: CS2302 Data Structures
# Author: Valeria Macias
# Assignment: HashTable with chain linking 
# Instructor: Olac Fuentes
# T.A.: Ismael Villanueva-Miranda
# Date of Last Modification: 7/28/19
# Purpose: HashTable with chain linking implementation using plist buckets and corresponding 
#           algorithms. Hash is value of item % table length. -1 is empty. -2 is deleted.

class HashTable(object):
  # Builds a hash table of size ‘size’
  # bucket is a list of (initially empty) lists
  # Constructor
  def __init__(self, size):
    self.bucket = [[] for i in range(size)]
    
# Hash is value of item modulo the length of the table  
def h(H, k):
  return k % len(H.bucket)
  
# Inserts item k to table H  
def insert(H, k):
  H.bucket[h(H, k)].append(k)
  return

# Returns the index of k in H as (bucket index, k index)
# If k is not in the table, returns bucket were k should be and -1
def find(H, k):
  b = h(H, k)
  try:
    i = H.bucket[b].index(k)
  except:
    i = -1
  return b, i

# Removes k from table and returns the bucket were k was.
  # if k not in table, returns -1
def delete(H, k):
  b = h(H, k)
  try:
    H.bucket[b].remove(k)
    return b
  except:
    return -1

# Returns the number of elements in the table
def size(H):
  count = 0
  for i in range(len(H.bucket)):
    count += len(H.bucket[i])
  return count

# Computes the load factor. Ideal should be less than 1
def load_factor(H):
  return size(H) / len(H.bucket)

# Returns the length of the longest bucket in the table 
def longest_bucket(H):
  max = 0
  for i in range(len(H.bucket)):
     if len(H.bucket[i]) > max:
       max = len(H.bucket[i])
  return max

# Returns true if every key has been inserted in the correct bucket in the table 
def verify_bucket(H):
  for i in range(len(H.bucket)):
    for j in range(len(H.bucket[i])):
      if H.bucket[i][j] % len(H.bucket) != i:
        return False
  return True

# Insert function that does not allow duplicates
def insert_no_duplicates(H, k):
  if k in H.bucket[h(H,k)]:
    return
  else:
    H.bucket[h(H, k)].append(k)
    return

# Inserts key at beginning of bucket
def insert_at_beginning(H, k):
  b = h(H, k)
  l = H.bucket[b]
  H.bucket[b] = [k]
  for i in l:
    H.bucket[b].append(i)
  return

# Moves element to beginning of bucket when it is searched and found
def find_move(H, k):
  b, i = find(H, k)
  if i != -1:
    delete(H, k)
    insert_at_beginning(H, k)
  return

# Returns the largest element in the table that has the same hash value as k, 
# or -1 if none.
def largest_at_hash_k(H, k):
  i = k%len(H.bucket)
  largest = -1
  for j in range(len(H.bucket[i])):
    if H.bucket[i][j] > largest:
      largest = H.bucket[i][j]
  return largest

