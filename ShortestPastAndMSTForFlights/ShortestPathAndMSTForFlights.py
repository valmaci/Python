# Course: CS2302 Data Structures
# Author: Valeria Macias
# Instructor: Olac Fuentes
# T.A.: Ismael Villanueva-Miranda
# Date of last modification: 7/30/19
# Purpose: Find the shortest flight path between cities

import xlrd
import math
import numpy as np
import matplotlib.pyplot as plt

def XLSXMtoAL(M): 
# Returns adjacency list of .xlsx Matrix
    AL = [[] for i in range(len(M[0])-1)]
    for x in range(1,len(M[0]),1):
        for y in range(1,len(M[0]),1):
            AL[x-1].append([FindCity(M,y-1),int(M[x][y])])
    return AL
    
def CitiesIndex(M):
# Prints each citie's index number
    for i in range(1,len(M[0])):
        print(i-1,":",M[0][i])
    return 

def FindIndex(M, city):
# Returns the index number of the city
    for i in range(1,len(M[0])):
        if M[0][i] == city:
            return i-1
    return -1

def FindCity(M, index):
# Returns the city name of the index number
    if index == -1:
        return
    return M[0][index+1]
    
def ShortestPath(M, AL, city): 
#Finds the shortest path from every city to every other city and displays the city names in sequence and overall distance
    startCity = FindIndex(M, city)
    unvisited = [i for i in range(len(AL))]
    distance = [math.inf for c in AL]
    path = [-1 for c in AL]
    distance[startCity] = 0
    while len(unvisited) > 0:
        currentC = unvisited[0]
        for c in unvisited[1:]:
            if distance[c] < distance[currentC]:
                currentC = c
        unvisited.remove(currentC)
        for adjC in AL[currentC]:
            if adjC[1] != -1:
                flightWeight = adjC[1]
                apd = distance[currentC]+flightWeight
                if apd < distance[FindIndex(M,adjC[0])]:
                    distance[FindIndex(M,adjC[0])] = apd
                    path[FindIndex(M,adjC[0])] = currentC
    for f in range(len(path)):
        PrintPathDistance(M,path,path[f],f)
        print(distance[f])
    print('\n')
    return path,distance

def PrintPathDistance(M,path,currentP,index):
# Assists ShortestPath function in printing path recursively
    if currentP==-1:
        print(FindCity(M,index), end='-')
    else:
        PrintPathDistance(M,path,path[currentP],currentP)
        print(FindCity(M,index), end='-')
    return

def ALtoEL(M,AL):
# Adjacency list to edge list
  edges = 0
  for i in range(len(AL)):
    edges += len(AL[i])
  EL = [ [] for i in range(edges)]
  j = 0
  for i in range(len(AL)):
    if len(AL[i]) < 1:
      i += 1 
    else:
      for e in AL[i]:
        EL[j] = [FindCity(M,i),e[0],e[1]]
        j += 1
  return EL

def Unite(S,i,j):
# Assists MinSpanningTree function
    removeSet = S[j]
    S.remove(S[j])
    for n in removeSet:
        S[i].append(n)
    return S

def MinSpanningTree(M,AL):
# Returns the Minimum Spanning Tree of an adjacency list
    flightList = ALtoEL(M,AL)
    citySets = [[]for i in range(len(M[0][1:]))]
    i = 0
    for city in M[0][1:]:
        citySets[i].append(city)
        i+=1
    resultList = []
    while len(citySets)>1 and len(resultList)<len(AL):
        minDist = math.inf
        nextFlightIndex = -1
        for f in range(len(flightList)):
            if flightList[f][2] != -1 and flightList[f][2]<minDist:
                minDist = flightList[f][2]
                nextFlightIndex = f
        nextFlight = flightList[nextFlightIndex]    
        flightList.remove(flightList[nextFlightIndex])
        cSet1 = 0
        cSet2 = 0
        for c in range(len(citySets)):
            if nextFlight[0] in citySets[c]:
                cSet1 = c
            if nextFlight[1] in citySets[c]:
                cSet2 = c
        if cSet1 != cSet2:
            resultList.append(nextFlight)
            if cSet1<cSet2:
                citySets = Unite(citySets,cSet1,cSet2)
            else:
                citySets = Unite(citySets,cSet2,cSet1)
    return resultList

def MSTAL(M,EL):
# Returns the undirected adjacency list of a MST
    AL = [[]for i in range(len(EL)+1)]
    for flight in EL:
        AL[FindIndex(M,flight[0])].append(flight[1:])
        AL[FindIndex(M,flight[1])].append([flight[0]]+[flight[2]])
    return AL

#======MAIN======

# Creates a matrix from cities.xlsx data
wb = xlrd.open_workbook("cities.xlsx")
sheet = wb.sheet_by_index(0)
rows = sheet.nrows
columns = sheet.ncols

citiesMatrix = [[[] for i in range(rows)] for j in range(columns)]

for x in range(rows):
    for y in range(columns):
        citiesMatrix[x][y] = sheet.cell(x,y).value

# Creates an adjacency list representation of the matrix
AL = XLSXMtoAL(citiesMatrix)

# ShortestPath is ran once for every city
ShortestPath(citiesMatrix,AL,'El Paso')
ShortestPath(citiesMatrix,AL,'San Antonio')
ShortestPath(citiesMatrix,AL,'Houston')
ShortestPath(citiesMatrix,AL,'Amarillo')
ShortestPath(citiesMatrix,AL,'Dallas')
ShortestPath(citiesMatrix,AL,'Austin')
ShortestPath(citiesMatrix,AL,'Jackson')
ShortestPath(citiesMatrix,AL,'Laredo')
ShortestPath(citiesMatrix,AL,'Tulsa')
ShortestPath(citiesMatrix,AL,'Lubbock')
ShortestPath(citiesMatrix,AL,'Las Vegas')
ShortestPath(citiesMatrix,AL,'Midland')
ShortestPath(citiesMatrix,AL,'McAllen')
ShortestPath(citiesMatrix,AL,'Denver')
ShortestPath(citiesMatrix,AL,'Albuquerque')
ShortestPath(citiesMatrix,AL,'Los Angeles')
ShortestPath(citiesMatrix,AL,'Oklahoma City')
ShortestPath(citiesMatrix,AL,'Phoenix')
ShortestPath(citiesMatrix,AL,'New Orleans')
ShortestPath(citiesMatrix,AL,'Wichita')

# Creates a minimum spanning tree
MST = MinSpanningTree(citiesMatrix,AL)
# Creates an adjancecy list representation of the minimum spanning tree
MSTAL = MSTAL(citiesMatrix,MST)

print("MST:\n")
# ShortestPath is ran once for every city using the Minimum Spanning Tree adjacency list
ShortestPath(citiesMatrix,MSTAL,'El Paso')
ShortestPath(citiesMatrix,MSTAL,'San Antonio')
ShortestPath(citiesMatrix,MSTAL,'Houston')
ShortestPath(citiesMatrix,MSTAL,'Amarillo')
ShortestPath(citiesMatrix,MSTAL,'Dallas')
ShortestPath(citiesMatrix,MSTAL,'Austin')
ShortestPath(citiesMatrix,MSTAL,'Jackson')
ShortestPath(citiesMatrix,MSTAL,'Laredo')
ShortestPath(citiesMatrix,MSTAL,'Tulsa')
ShortestPath(citiesMatrix,MSTAL,'Lubbock')
ShortestPath(citiesMatrix,MSTAL,'Las Vegas')
ShortestPath(citiesMatrix,MSTAL,'Midland')
ShortestPath(citiesMatrix,MSTAL,'McAllen')
ShortestPath(citiesMatrix,MSTAL,'Denver')
ShortestPath(citiesMatrix,MSTAL,'Albuquerque')
ShortestPath(citiesMatrix,MSTAL,'Los Angeles')
ShortestPath(citiesMatrix,MSTAL,'Oklahoma City')
ShortestPath(citiesMatrix,MSTAL,'Phoenix')
ShortestPath(citiesMatrix,MSTAL,'New Orleans')
ShortestPath(citiesMatrix,MSTAL,'Wichita')
