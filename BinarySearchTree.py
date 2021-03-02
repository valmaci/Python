import math

# Course: CS2302 Data Structures
# Author: Valeria Macias
# Assignment: Binary Search Trees 
# Instructor: Olac Fuentes
# T.A.: Ismael Villanueva-Miranda
# Date of Last Modification: 6/26/19
# Purpose: Binary Search Tree implementation and corresponding algorithms.

#TESTCHANGE

class BinarySearchTree(object):
  def __init__(self, item, left=None):
    self.item = item
    self.left = left
    self.right = right

# Inserts item into binary search tree
def insert(Tree, new_item):
  if Tree == None:
    Tree = BinarySearchTree(new_item)
  elif Tree.item > new_item:
    Tree.left = insert(Tree.left, new_item)
  else:
    Tree.right = insert(Tree.right, new_item)
  return Tree
  

# Prints tree in left child, parent, right child order
def inorder_print(Tree):
  if Tree != None:
    if Tree.left != None:
      inorder_print(Tree.left)
    print(Tree.item)
    if Tree.right != None:
      inorder_print(Tree.right)
  return

# Prints tree in parent, left child, right child order
def preorder_print(Tree):
    if Tree != None:
        print(Tree.item)
        if Tree.left != None:
            preorder_print(Tree.left)
        if Tree.right != None:
            preorder_print(Tree.right)
            
# Prints tree in left child, right child, parent order
def postorder_print(Tree):
    if Tree != None:
        if Tree.left != None:
            postorder_print(Tree.left)
        if Tree.right != None:
            postorder_print(Tree.right)
        print(Tree.item)

# Returns the Node containing the smallest item
def smallest(Tree):
  if Tree.left == None:
    return Tree
  else:
    return smallest(Tree.left)

# Returns the Node containing the largest item
def largest(Tree):
  if Tree.right == None:
    return Tree
  else:
    return largest(Tree.right)

# Returns Node which contains k or None if it doesn't exist
def search(Tree, k):
  if Tree == None:
    return None
  if Tree.item == k:
    return Tree
  if Tree.item > k:
    return search(Tree.left, k)
  else:
    return search(Tree.right, k)
  
# Returns number of Nodes in the Tree
def size(Tree):
  if Tree == None:
    return 0
  right = size(Tree.right)
  left = size(Tree.left)
  return 1 + right + left

# Returns height of the Tree
def height(Tree):
  if Tree == None:
    return 0
  if Tree.right != None:
    return 1 + height(Tree.right)
  if Tree.left != None:
    return 1 + height(Tree.left)
  right = height(Tree.right)
  left = height(Tree.left)
  return max(right, left)

# Prints every node item smaller than k
def print_smaller(Tree, k):
  if Tree == None:
    return
  if Tree.item < k:
    print_smaller(Tree.right, k)
    print(Tree.item)
    print_smaller(Tree.left, k)
  if Tree.item == k:
    print_smaller(Tree.left, k)
  if Tree.item > k: 
    print_smaller(Tree.left, k)
  return

# Prints all leafs of the tree
def print_leaf(Tree):
  if Tree == None:
    return
  if Tree.left == None and Tree.right == None:
    print(Tree.item)
  print_leaf(Tree.left)
  print_leaf(Tree.right)
  return

# Returns the largest item in the tree that is stored at depth
def largest_node_at_depth(Tree, depth):
  if depth == 0 and Tree == None:
    return -math.inf
  if depth == 0:
    return Tree.item
  right = largest_node_at_depth(Tree.right, depth-1)
  left = largest_node_at_depth(Tree.left, depth-1)
  return max(Tree.item, right, left)

# Prints all the items at depth
def print_depth(Tree, depth):
  if Tree == None:
    return
  if depth == 0:
    print(Tree.item, end=",")
  else:
    print_depth(Tree.left, depth-1)
    print_depth(Tree.right, depth-1)
  return

# Returns depth of the node with item k, or -1 if k is not in tree.
def depth_of_node(Tree, k):
  if Tree == None:
    return -1
  if Tree.item < k:
    return 1 + depth_of_node(Tree.right, k)
  if Tree.item > k:
    return 1 + depth_of_node(Tree.left, k)
  if Tree.item == k:
    return 0

# Returns a sorted list of the Binary Search Tree
def sort(Tree):
  if Tree == None:
    return []
  left = sort(Tree.left)
  right = sort(Tree.right)
  return left + [Tree.item] + right

# Creates a tree from a list
def build_tree(L):
  if L == []:
    return None
  else:
    mid = len(L)//2
    Tree = BinarySearchTree(L[mid])
    Tree.left = build_tree(L[:mid]) 
    Tree.right = build_tree(L[mid+1:])
  return Tree 

# Prints items by depth
def print_by_depth(Tree):
  if Tree != None:
    depth = height(Tree)
    for i in range(depth+2):
      print_depth(Tree, i)
      print()
  return

# Returns sum of items at depth
def sum_items(Tree,depth):
  sum = 0
  if Tree == None:
    return 0
  if depth == 0:
    return Tree.item
  else:
    sum += sum_items(Tree.left, depth-1)
    sum += sum_items(Tree.right, depth-1)
  return sum

# Returns the sum of the items from k to the root or -1 if k is not in the tree
def sum_path(Tree, k):
  if Tree == None:
    return -1
  if Tree.item == k:
    return k
  if Tree.item < k:
    s = sum_path(Tree.right, k)
  else:
    s = sum_path(Tree.left, k)
  if s == -1:
    return -1
  return s + Tree.item

# Prints tree vertically so the furthest left is the root, the furthest right 
  # are the leaves
def show_tree(Tree, ind):
  if Tree is not None:
    show_tree(Tree.right, ind+' ')
    print(ind, Tree.item)
    show_tree(Tree.left, ind+' ')

