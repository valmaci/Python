# Course: CS2302 Data Structures
# Author: Valeria Macias
# Assignment: Lab6
# Instructor: Olac Fuentes
# T.A.: Ismael Villanueva-Miranda
# Date of Last Modification: 8/5/19
# Purpose: A Backtracking algorithm, Greedy algorithm, Randomized algorithm, and
#   Dynamic algorithm implementation of the Knapsack Problem.

import numpy as np

# 1.) Backtracking algorithm that solves the 
# optimization 0-1 knapsack problem.
# Returns the highest-value load that can fit in the knapsack and its value.

def Backtracking(capacity,weight,value):
    indexes = [i for i in range(len(weight))]
    indexList = IndexPermutations(indexes,[],[])
    weightCombos = []
    valueCombos = []
    for i in range(len(indexList)):
        cap = capacity
        weightCombos.append([])
        valueCombos.append([])
        for ind in indexList[i]:
            cap = cap-weight[ind]
            if cap >= 0:
                weightCombos[-1].append(weight[ind])
                valueCombos[-1].append(value[ind])
            else:
                cap = cap+weight[ind]
                continue
    maxWeightCombo = []
    maxValue = 0
    for j in range(len(valueCombos)):
        if sum(valueCombos[j]) > maxValue:
            maxValue = sum(valueCombos[j])
            maxWeightCombo = weightCombos[j]
    return maxWeightCombo, maxValue
                
def IndexPermutations(indexes,newIndexes,indexList):
    if len(indexes) == 0:
        indexList += [newIndexes]
    else:
        for i in range(len(indexes)):
            ind = indexes[i]
            notInd = indexes[:i]
            for n in indexes[i+1:]:
                notInd.append(n)
            newInd = []
            for m in newIndexes:
                newInd.append(m)
            newInd.append(ind)
            IndexPermutations(notInd,newInd,indexList)
    return indexList
        
# 2.) Greedy algorithm that solves the
# optimization continuous knapsack problem. 
# Returns the highest value load that can fit in the knapsack and it's total value.

def Greedy(capacity,weight,value):
    itemIndex = SortDescendingFractional(weight,value)
    remaining = capacity
    ksWeight = []
    ksValue = []
    for i in range(len(itemIndex)):
        if weight[itemIndex[i]] <= remaining:
            ksWeight += [weight[itemIndex[i]]]
            ksValue += [value[itemIndex[i]]]
            remaining = remaining - weight[itemIndex[i]]
        else:
            fraction = remaining/weight[itemIndex[i]]
#            ksWeight += [fraction*(value[itemIndex[i]]/weight[itemIndex[i]])]
#            ksValue += [value[itemIndex[i]]*(fraction * (value[itemIndex[i]]/weight[itemIndex[i]]))]
            ksWeight += [fraction*weight[itemIndex[i]]]
            ksValue += [value[itemIndex[i]]*fraction]
            break
    return ksWeight, sum(ksValue)
    
def SortDescendingFractional(w,v):
    ratios = [[]for i in range(len(w))]
    for i in range(len(w)):
        ratios[i] = v[i]/w[i]
    ratios.sort(reverse=True)
    indexes = [i for i in range(len(ratios))]
    for i in range(len(w)):
        for j in range(len(ratios)):
            if v[i]/w[i] == ratios[j]:
                indexes[j] = i
    return indexes
    

# 3.) Randomized algorithm that solves the optimization 0-1 knapsack problem.
# Generates many random permutations(use np.random.permutations(n)) of the items
# and for every permutaiton, adds the items to the knapsack one by one until the 
# capacity is reached. Returns the permutation which results in the largest value.

def Randomized(capacity,weight,value,n):
    indexes = [i for i in range(len(weight))]
    randInd = [[] for i in range(n)]
    for i in range(n):
        randInd[i] = np.random.permutation(indexes)
    weightCombos = []
    valueCombos = []
    for j in range(len(randInd)):
        cap = capacity
        weightCombos.append([])
        valueCombos.append([])
        for ind in randInd[j]:
            cap = cap-weight[ind]
            if cap >= 0:
                weightCombos[-1].append(weight[ind])
                valueCombos[-1].append(value[ind])
            else:
                cap = cap+weight[ind]
                continue
    maxWeightCombo = []
    maxValue = 0
    for j in range(len(valueCombos)):
        if sum(valueCombos[j]) > maxValue:
            maxValue = sum(valueCombos[j])
            maxWeightCombo = weightCombos[j]
    return maxWeightCombo, maxValue

# 4.) Dynamic programming algorithm that solves
# the optimization integer knapsack problem.
# Returns the highest load that can fit in the knapsack
                 
def Dynamic(capacity,weight,value):
    ksValue = np.zeros(capacity+1,dtype=int)
    ksWeight = [[]for i in range(capacity+1)]
    ksWeight[0].append(0)
    weightCopy = []
    for wt in weight:
        weightCopy.append(wt)
    weightCopy.sort()
    valueCopy = []
    for i in range(len(weightCopy)):
        for j in range(len(weight)):
            if weightCopy[i] == weight[j]:
                valueCopy.append(value[j])
    wind = 0
    for w in weightCopy:
        for d in range(w,capacity+1):
            if ksWeight[d-w] != []:
                if d == w and valueCopy[wind] >= ksValue[d]:
                    ksWeight[d] = []
                    ksWeight[d].append(w)
                    ksValue[d] = valueCopy[wind]
                elif sum(ksWeight[d-w])+w == d and ksValue[d-w]+valueCopy[wind] >= ksValue[d]:
                    ksWeight[d] = []
                    ksWeight[d] += ksWeight[d-w]
                    ksWeight[d].append(w)
                    ksValue[d] = ksValue[d-w]+valueCopy[wind]
                elif sum(ksWeight[d-w])+w < d and ksValue[d-w]+valueCopy[wind] >= ksValue[d]:
                    ksWeight[d] += w
                    ksValue[d] += valueCopy[wind]
        wind +=1
    maxLoad = []
    maxValue = 0
    for i in range(len(ksValue)):
        if ksValue[i] > maxValue:
            maxValue = ksValue[i]
            maxLoad = ksWeight[i]
    return maxLoad, maxValue

#=======TEST CASES========

# 1
weight1 = [3, 1, 9, 2]
value1 = [4, 1, 6, 3]

print('BT1',Backtracking(10,weight1,value1))
print('GR1',Greedy(10,weight1,value1))
print('R1',Randomized(10,weight1,value1,3))
print('D1',Dynamic(10,weight1,value1))
print()
# 2
weight2 = [10, 4, 3, 6, 9, 8]
value2 = [1000,1,6,4,7,2]

print('BT2',Backtracking(9,weight2,value2))
print('GR2',Greedy(9,weight2,value2))
print('R2',Randomized(9,weight2,value2,3))
print('D2',Dynamic(9,weight2,value2))
print()

# 3
weight3 = [10, 4, 3, 6, 9, 8, 1, 2]
value3 = [5,1,6,4,7,2,3,1]

print('BT2',Backtracking(11,weight3,value3))
print('GR2',Greedy(11,weight3,value3))
print('R2',Randomized(11,weight3,value3,3))
print('D2',Dynamic(11,weight3,value3))
print()