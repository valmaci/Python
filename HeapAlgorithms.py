
# Course: CS2302 Data Structures
# Author: Valeria Macias
# Assignment: Heaps
# Instructor: Olac Fuentes
# T.A.: Ismael Villanueva-Miranda
# Date of Last Modification: 7/9/19
# Purpose: Max Heap implementation using plist and corresponding algorithms

import numpy as np

# Returns index of parent
def parent(i):
  return (i-1)//2

# Returns index of left child
def left_child(i):
    return (2*i) + 1

# Returns index of right child
def right_child(i):
    return (2*i) + 2

# Creates max heap: Appends item at end then swaps repeatedly with parent until 
# item is not greater than parent
def heap_insert(H,item):
    H.append(item)
    i = len(H)-1
    while i>0 and item > H[parent(i)]:
        H[i] = H[parent(i)]
        i = parent(i)
    H[i] = item
    
# Removes and returns root from max heap. 
# Then sorts max heap by replacing parent with largest child until the 
# smallest value in the heap becomes a parent or the heap ends.
def extract_max(H):
    if len(H) <1:
        return None
    if len(H) ==1:
        return H.pop()
    root = H[0]
    p = H.pop() # minimum value of max heap
    i = 0
    while True:
        L = [p] # min value, left child and right child are appended, if exist
        if left_child(i) <len(H): 
            L.append(H[left_child(i)])
            if right_child(i) <len(H):
                L.append(H[right_child(i)])
        m = max(L) # Compares children with minimum value of max heap and extracts max
        H[i] = m # Parent is repeatedly swapped with max of children and minimum value
        if m == p: # The minimum value has found its place as a parent in the heap, the swaps end
            break
        elif m == L[1]: # The max is the left child
            i = left_child(i)
        else: # The max is the right child
            i = right_child(i)
    return root   
    
# Sorts max heap in aschending order
def heap_sort(A):
    H = []
    # converts list to a max heap
    for a in A:
        heap_insert(H,a)
    # Inserts max from last index to 0
    for i in range(len(A)):
        A[-(1+i)] = extract_max(H)

# Takes a list and returns true if it is a heap    
def is_heap(L):
  for i in range(len(L)):
    if left_child(i) <= len(L)-1: #if left child exists
      if L[i] < L[left_child(i)] or L[i] < L[right_child(i)]: # if parent value is less than children
        return False
  return True
  
# Returns the index of the sibling of H[k], if it exists
def sibling(H, k):
  if k%2 == 0:
    sibling = k-1
  else:
    sibling = k+1
  if sibling > 0 and sibling < len(H):
    return sibling
  else:
    return None

# Prints the parent, sibling, H[k], left child and right child of index k, if exists
def print_fam(H,k):
    p = parent(k)
    s = sibling(H,k)
    lc = left_child(k)
    rc = right_child(k)
    if p >=0 and p < len(H):
        print("Parent:", H[p])
    if s != None:
        if left_child(p) == k:
            print("k:", H[k])
            print("Right Sibling:",H[s])
        else:
            print("Left Sibling:",H[s])
            print("k:", H[k])
    if lc >= 0 and lc < len(H):
        print("Left Child:", H[lc])
    if rc >= 0 and rc < len(H):
        print("Right Child:", H[rc])

  
# Returns the second largest element in a heap, or None if the heap has less than two elements
def second_largest(H):
  if len(H) < 2:
    return None
  L = []
  for i in H:
    L.append(i)
  m = max(L)
  L.remove(m)
  return max(L)

# Prints all the elements in the path from H[k] to the root
def print_path(H, k):
  if k == 0:
    print(H[k])
  else:
    p = parent(k)
    print(H[k], end=' ')
    print_path(H, p)
  return

# Receives a heap and determines if it contains two siblings which are equal
def equal_siblings(H):
  if len(H) > 2:
    for i in range(len(H)):
      p = parent(i)
      lc = -1
      rc = -2
      if left_child(p) < len(H):
        lc = left_child(p)
      if right_child(p) < len(H):
        rc = right_child(p)
      if H[lc] == H[rc]:
        return True
  return False

# Returns the largest difference between a parent and its children
def generation_gap(H):
  gap = 0
  if len(H) > 2:
    for i in range(len(H)):
      if left_child(i) < len(H):
        if H[i] - H[left_child(i)] > gap:
          gap = H[i] - H[left_child(i)]
      if right_child(i) < len(H):
        if H[i] - H[right_child(i)] > gap:
          gap = H[i] - H[right_child(i)]
  return gap

# Returns true if H is a max heap, false otherwise
def check_heap(H):
  for i in range(len(H)):
    if left_child(i) < len(H):
      if H[i] < H[left_child(i)]:
        return False
    if right_child(i) < len(H):
      if H[i] < H[right_child(i)]:
        return False
  return True
  
# Returns the sum of the elemnts in the path from H[k] to the root
def sum_path(H, k):
  s = H[k]
  if k > 0:
    s += sum_path(H, parent(k))
  return s
