'''
Created on Jul 28, 2017

@author: benjaminsenyonyi, AliAghaee
'''
import metrics
import numpy
import collections
from metrics import BuildAdjacencyMatrix, CountOutDegrees, countEdges
from metrics import FloydWarshall
import time
from scipy import longfloat
from numpy.core.arrayprint import LongFloatFormat
# from networkx.algorithms import centrality

adjstartTime = time.time()
adjMatrix, nodelist  = BuildAdjacencyMatrix(".../onehash")

print("adjMatrix created")
adjTime = time.time() - adjstartTime
numberOfNodes = len(nodelist)
numberOfEdges = countEdges(adjMatrix)
print("Number of Nodes:", numberOfNodes)
print(numberOfEdges)
numberOfComponents , componentsLabelsArray = metrics.GetConnectedComponents(adjMatrix)
print("Connected Components calculated:", numberOfComponents)

sizeOfConnectedComponents = collections.Counter(componentsLabelsArray.flatten()).values()



floydstartTime = time.time()
floydtime = time.time()
distMat, countMat, diameterDir = FloydWarshall(adjMatrix, None)
print("FloydWarshall done")
floydTime = time.time() - floydstartTime



#countInDegree
cinstartTime = time.time()
countInDegree = sorted(metrics.CountInDegrees(adjMatrix), reverse=True)
print(countInDegree)
print("InDegree calculated")
newinDegree = numpy.array(countInDegree)
newinDegree.astype(LongFloatFormat)
cinTime = time.time() - cinstartTime

#countOutDegree
coutstartTime = time.time()
countOutDegree = sorted(metrics.CountOutDegrees(adjMatrix), reverse=True)
print(countOutDegree)
print("OutDegree calculated")
newoutDegree = numpy.array(countOutDegree)
newoutDegree.astype(LongFloatFormat)
coutTime = time.time() - coutstartTime

#closenessCentrality
closecentralstartTime = time.time()
closeness, diameter = metrics.CalculateClosenessCentrality(adjMatrix)
closenessCentrality  = sorted(closeness, reverse=True)
print("closenessCentrality calculated")
closecentralTime = time.time() - closecentralstartTime

#betweennessCentrality
btncentralstartTime = time.time()
# betweennessCentrality= sorted(metrics.CalculateBetweennessCentrality(distMat, countMat, None), reverse=True)
print("betweennessCentrality calculated")
btncentralTime = time.time() - btncentralstartTime

#betweennessCentralityNormalized
normbtncentralstartTime = time.time()
# betweennessCentralityNormalized = sorted(metrics.CalculateBetweennessCentrality(distMat, countMat, None), reverse=True)
print("betweennessCentralityNormalized calculated")
normbtncentralTime = time.time() - normbtncentralstartTime


#rootNode
rootNodestartTime = time.time()
rootIndex, rootIndices = metrics.GetRootNode(adjMatrix)
rootNode = nodelist[rootIndex]
print("rootNode calculated")
rootNodeTime = time.time() - rootNodestartTime

#rootInfluence
rootInfluencestartTime = time.time()
rootIndex, rootInfluence, rootIndices = metrics.CalculateRootInfluence(adjMatrix)
rootInfluence = nodelist[rootIndex]
print("rootInfluence calculated")
rootInfluenceTime = time.time() - rootInfluencestartTime

#leafIndices
leafIndicesstartTime = time.time()
leafIndices = set(metrics.GetLeafIndices(adjMatrix))
print("leafIndices calculated")
leafIndicesTime = time.time() - leafIndicesstartTime


#allNodesDistancesFromRoot
nodesDistancesstartTime = time.time()
allNodesDistancesFromRoot = metrics.GetAllNodesDistancesFromRoot(distMat, adjMatrix=adjMatrix)
print("allNodesDistancesFromRoot calculated")
nodesDistancesTime = time.time() - nodesDistancesstartTime

#allNodesDistancesToLeaf
leafnodesDistancesstartTime = time.time()
allNodesDistancesToLeaf = metrics.GetAllNodesDistancesToLeaf(distMat, adjMatrix) 
print("allNodesDistancesToLeaf calculated")
leafnodesDistancesTime = time.time() - leafnodesDistancesstartTime

# calculate Wiener Index
wienerIndex_startTime = time.time()
wienerIndex = metrics.GetWienerIndex(adjMatrix, numberOfComponents, componentsLabelsArray)
print("Wiener Index calculated")
wienerIndex_Time = time.time() - wienerIndex_startTime

# Calculate NX Betweenness centrality
bt_startTime = time.time()
btn_centrality = sorted(metrics.GetBetweenness(adjMatrix), reverse = True)
print("NetworkX Betweenness Centrality calculated")
bt_Time = time.time() - bt_startTime


# Calculate new closeness centrality
clo_centralitystartTime = time.time()
clo_centrality = sorted(metrics.closeness(adjMatrix), reverse = True)
clo_centralityTime = time.time() - clo_centralitystartTime


# Calculate Density
density_startTime = time.time()
graphDensity = metrics.GetGraphDensity(adjMatrix)
print(graphDensity)
density_Time = time.time() - density_startTime

# Calculate Eccentricity
eccentricity_startTime = time.time()

eccentricity_Time = time.time() - eccentricity_startTime

clustering_coeff = metrics.GetClusteringCoefficent(adjMatrix)



print("Writing to results file")


#Writing all metrics to a result.txt file
f = open('Results.txt','w')
f.write("Number of Nodes:"+str(numberOfNodes)+'\r\n\r\n')
f.write("Number of Edges:"+str(numberOfEdges)+'\r\n\r\n')
f.write("Number of Connected Components:"+str(numberOfComponents)+'\r\n\r\n')
f.write("Labels of Connected Components:\r\n"+str(componentsLabelsArray)+'\r\n\r\n')
f.write("Size of each component per Label:\r\n"+str(sizeOfConnectedComponents)+'\r\n\r\n')
#f.write("Count InDegree:\r\n"+str(countInDegree)+'\r\n\r\n')
f.write("Root Node:"+str(rootNode)+'\r\n\r\n')
f.write("Root Influence:"+str(rootInfluence)+'\r\n\r\n')
f.write("Count InDegree:\r\n"+str(newinDegree)+'\r\n\r\n')
f.write("Count OutDegree:\r\r\n"+str(newoutDegree)+'\r\n\r\n')
f.write("Closeness Centrality:\r\n"+str(closenessCentrality)+'\r\n\r\n')
# f.write("Betweenness Centrality:\r\n"+str(betweennessCentrality)+'\r\n\r\n')
# f.write("Betweenness CentralityNormalized:\r\n"+str(betweennessCentralityNormalized)+'\r\n\r\n')
f.write("Leaf Indices:\r\n"+str(leafIndices)+'\r\n\r\n')
f.write("All Nodes Distances From Root:\r\n"+str(allNodesDistancesFromRoot)+'\r\n\r\n')
f.write("All Nodes Distances To Leaf:\r\n"+str(allNodesDistancesToLeaf)+'\r\n\r\n')
# f.write("Diameter from FloydWarshall is:\r\r\n" + str(diameterDir) + '\r\n\r\n')
f.write("NetworkX Betweenness Centrality: \r\r\n" + str(btn_centrality) + '\r\r\n')
f.write("NetworkX Closeness Centrality: \r\r\n" + str(clo_centrality) + '\r\r\n')
f.write("Diameter :\r\r\n" + str(diameter) + '\r\n\r\n')
f.write("Density of Graph: \r\r\n" + str(graphDensity) + '\r\r\n')
f.write("Wiener Index: \r\r\n" + str(wienerIndex) + '\r\r\n')
f.close()
print("Writing to results file completed")
print("Writing to time performance file")

#Performance test results
f2 = open('Time-performance.txt','w')
f2.write("Adjacency matrix calculation time: "+str(adjTime)+" seconds"+'\r\n\r\n')
f2.write("Floyd Warshall calculation time: "+str(floydTime)+" seconds"+'\r\n\r\n')
f2.write("In degree calculation time: "+str(cinTime)+" seconds"+'\r\n\r\n')
f2.write("Out Degree calculation time: "+str(coutTime)+" seconds"+'\r\n\r\n')
f2.write("Closeness Centrality calculation time: "+str(closecentralTime)+" seconds"+'\r\n\r\n')
f2.write("Betweenness Centrality calculation time: "+str(btncentralTime)+" seconds"+'\r\n\r\n')
f2.write("Root Node calculation time: "+str(rootNodeTime)+" seconds"+'\r\n\r\n')
f2.write("Root Influence calculation time: "+str(rootInfluenceTime)+" seconds"+'\r\n\r\n')
f2.write("Leaf Indices calculation time: "+str(leafIndicesTime)+" seconds"+'\r\n\r\n')
f2.write("All Nodes Distances from Root calculation time: "+str(nodesDistancesTime)+" seconds"+'\r\n\r\n')
f2.write("All Nodes Distances to Leaf calculation time: "+str(leafnodesDistancesTime)+" seconds"+'\r\n\r\n')
f2.write("Graph Density calculation time: "+str(density_Time)+" seconds"+'\r\n\r\n')
f2.write("NX Betweenness Centrality calculation time: "+str(bt_Time)+" seconds"+'\r\n\r\n')
f2.close()
print("Writing to time performance file completed")