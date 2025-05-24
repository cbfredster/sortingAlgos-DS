#layout of basic backtracking function from eamon's slides has been implemented into code.

#if current solution is valid then
#if current solution is complete then
#return current solution
#else
#for each extension of the current solution do
#extend_solution(extension)


#backtracking function with two variable inputs (the array being checked and the #intended length)
def backtrack(theArray, k):
	# check for if the length of the 'ordered' is sufficient and =k
        if len(theArray) == k:
        	# no requirement or change of array as reached len(theArray)=A
            print(theArray)
            #returns true for ordering statement (boolean value assigned)
            return True
            #proceeding to check any numbers between non-k-length array up to k
        for i in range(k):  
        	#as the value in elements are equivalent to their position, 
        	# If the number isn't within the array then then the position hasn't 
        	#been assigned a value yet
        	#checks to see if the array is valid
            if i != theArray[i]:  
            	#extends the solution, by +1 iteration
                if backtrack(theArray[i+1],k):
                	return True
         #if no values can be found in the for loop then returns False
        return False
                
def ordering(k):
	#initialise array of size k-input
 A=[""]*k
 #run through assigning value to positions
 for i in range(k):
  A[i]=i
  #check with backtrack (uselessly) in this case because most trivial case of strict monotonicity 
 if backtrack(A,k) == True:
  return(A)

#-------------------------------------
#SEPERATE THOUGHT PROCESS FOR NEXT PART OF QUESTION 4
  
def paiwriseDifferences(partialD,k):
 #runs through the length of partialD (sequence of pairwise differences), and is len(partialD)-1 because the last element value isn't required, as checked by penultimate element for modulus difference
 for j in range(len(partialD)-1):
 #formula given inside D[] in question, (r1-r0)modk but
 # written as partialD (partial difference but already
 # used similiar variable name), essentially difference between two succesive pairs of element data values modulus len(k)
  return ((partialD[j+1]-partialD[j])%k)

def checkforvalidsequence(partialD,k):
 #trivial check, as array of len=1 will have null pairwise difference as nothing to compare to.
 if len(partialD) == 1:
  return True
  # for lengths of arrays 1 < len(array)
  for i in range(len(paiwriseDifferences(partialD,k))-1):
  	#check if the modulus differnece between an position value(i+1) and position value(i) is greater or equivalent
  	#as this satisfies the ordering condition of non-strict monotonicity
   if paiwriseDifferences(partialD,k)[i] <= paiwriseDifferences(partialD,k)[i+1]:
   	#as condition of non-strict monotonicity is met then return true for checking valid sequence
     return True
   else:
   	#compliment of not being non-strict monotonic increasing is monotonic decreasing, therefore being invalid hence False
    return False
