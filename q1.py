def compute_winner(history_A, history_B):
 win = ""
 headSumA = 0
 headMaxA = 0
 for i in history_A:
  if i == 'H':
   headSumA = headSumA + 1
  if i == 'T':
  	#changing highscore (of consecutive H's') if current HeadSum is greater than HeadMax
   if headMaxA <= headSumA:
      headMaxA = headSumA
      # sets highscore to 0 as consecutive row of H has terminated
   headSumA = 0
  if headMaxA < headSumA:
   headMaxA = headSumA
    #same iteration for history of B, switched variable names though
 headSumB = 0
 headMaxB = 0
 for j in history_B:
  if j == 'H':
   headSumB = headSumB + 1
  if j == 'T':
   if headMaxB <= headSumB:
      headMaxB = headSumB
   headSumB = 0 
  if headMaxB < headSumB:
   headMaxB = headSumB
 # initialised win variable is given string 'value' to be returned/outputted from the function
 if headMaxA < headMaxB:
   win = "B"
 if headMaxA > headMaxB:
   win = "A"
 if headMaxA == headMaxB:
   win = "D"
 return(win)
 
 
 
def encode(history):
 encodedHistory = ""
 historySum = 1

 for i in range(1,len(history)):
 	#checking if previous character was equivalent to the current position 
 	# IF so then highscore is increased
  if history[i] == history[i-1]:
   historySum = historySum + 1
   # until the condition when its not true, and the consecutive row letter (T or H)
   #is determined by the most recent inclusion
  else:
 	 if history[i-1] == 'H':
 	  encodedHistory = encodedHistory + 'H' + str(historySum)
 	 if history[i-1] == 'T':
 	  encodedHistory = encodedHistory + 'T' + str(historySum)
 	  # sum is intialised at 1 again, as going through the string, each consecutive row will start with 1
 	  # as otherwise does not exist in the string (i.e historySum = 0, as then it wouldnt be checked in the first place)
 	 historySum = 1 
 	
 	#i found that the last part of the inputted history wasn't being included so history[-1], iteration checks from 1 before   # i.e [i-1]
 encodedHistory = encodedHistory + history[-1] + str(historySum)
 
 return(encodedHistory)

def decode(compressed_history):
 uncompressedHistory = ""
 # i is done in steps of 2, as we're considering pairs'
 for i in range(0,len(compressed_history),2):
 	#known that n<9 so alternating letters and numbers, and starting with letter (and then 3rd, 5th...)
  letter = compressed_history[i]
  number = compressed_history[i+1]
  #basically string + the letter * how many times (given be number<9)
  uncompressedHistory = uncompressedHistory + letter * int(number)
 return(uncompressedHistory)
  
 
def compute_winner_compressed(compressed_history_A, compressed_history_B):


 winner = ""
 hMaxA = 0
 #as noticeable pattern to before with alternating letters and numbers, then step 2 (but DIFFERENT ALGO)
 for i in range(0,len(compressed_history_A),2):
 	#only care about H's
  if compressed_history_A[i] == "H":
   #further only care if its larger than any number we've seen immediately on RHS of a H
   if int(compressed_history_A[i+1]) > hMaxA:
    hMaxA = int(compressed_history_A[i+1])
    
    #practically repeated (to hMax inside this function) with variable name changes
 hMaxB = 0
 for j in range(0,len(compressed_history_B),2):
  if compressed_history_B[j] == "H":
   if int(compressed_history_B[j+1]) > hMaxB:
    hMaxB = int(compressed_history_B[j+1])
    
    #another initiliased variable being assigned a value
 if hMaxA < hMaxB:
  winner = "B"
 if hMaxA > hMaxB:
  winner = "A"
 elif hMaxA == hMaxB:
  winner = "D"

 return(winner)
