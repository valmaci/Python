README

The purpose of this program is primarily to understand the shortest path algorithm
and Minimum Spanning Trees (MST). 

The program first reads and creates a matrix of a .xlsx file containing simulated flight 
path distances between cities. -1 means there is no flight  path between the cities.

The program then runs the shortest path algorithm on the matrix and
displays the result.

The program then creates a MST and runs the shortest path algorithm
on the MST and displays the results.

The results show that even though the greedy MST algorithm removed the paths containing
the greatest distances, it did not provide shorter distances between cities because 
the MST removes many flight paths. The more flight paths there are, the shorter distances 
can be found between cities. 



