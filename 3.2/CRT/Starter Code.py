import random

def printSol(S, c, O):
    # This procedure prints details of a solution to the screen.
    print("\nSolution\n--------")
    for i in range(len(S)):
        print("Lane",  i, "=", S[i], "(used", sum(S[i]), "of", c, "cm)")
    print("Overflow =", O)
    print("Total length in overflow =", sum(O), "cm")
    
def getLane(ch,carLen, S, L):
    if(ch==1):
        lane = getFirstLane(carLen, S, L)
    elif(ch==2):
        lane = getEmptyLane(carLen, S, L)
    elif(ch==3):
        lane = getFullLane(carLen, S, L)
    elif(ch==4):
        lane = getRandomLane(carLen, S, L)
    return lane
        

def getFirstLane(carLen, S, L):
    # This function returns the number of the first suitable lane for the current car. 
    # It returns -1 is there is no suitable lane
    for i in range(len(S)):
        if sum(S[i]) + carLen <= c:
            return i
    #If we are here, no lane is suitable.
    return -1

def getEmptyLane(carLen, S, L):
    # This function returns the emptiest lane with sufficient capacity for the vehicle

def getFullLane(carLen, S, L):
    # This function returns the fullest lane with sufficient capacity for the vehicle

def getRandomLane(carLen, S, L):
    # This function returns the random lane with sufficient capacity for the vehicle
    
   
# Main Program -------------------------------------------------------------
# Read in the problem file. All car lengths are put into the list L
L = []
with open("input.txt","r") as f:
    c = int(f.readline())
    numLanes = int(f.readline())
    for line in f:
        L.append(int(line))

# Having read in the file, output some information to the screen
print("Number of vehicles                                =", len(L))
print("Total length of vehicles                          =", sum(L), "cm")
print("Number of lanes                                   =", numLanes)
print("Capacity per lane                                 =", c, "cm")
print("List of all vehicle lengths (in order of arrival) =", L)

# Now declare the data structures used for storing the vehicles in each lane
# and the vehicles in the overflow
S = [[] for i in range(numLanes)]
O = []
print("Menu for entering Choice :")
print("Enter 1 for first suitable lane")
print("Enter 2 for Empty suitable lane")
print("Enter 3 for full suitable lane")
print("Enter 4 for random suitable lane")
ch = int(input("Enter your choice : "))
# Here is the basic algorithm. It takes each vehicle in turn and places it
# into the first lane observed to have sufficient capacity. When no suitable 
# lane exists, the vehcile is put into the overflow list instead
for i in range(len(L)):
    carLen = L[i]
    lane = getLane(ch,carLen,S,L)
    if lane != -1:
        S[lane].append(carLen)
    else:
        O.append(carLen)

# Print details of the solution to the screen
printSol(S, c, O)