class HashTable():
    """Implements a simple hash table of size k, with all 
    empty entries denoted as '-' at initialisation.

    You must not modify this code.

    Set up your hashtable as follows, with some sensible integer value for k:
        h = HashTable(k)
    
    For a HashTable h:
        h.lookup(pos) returns the data in position pos.
        h.add(pos, data) adds data in position pos. 
        h.check(table) checks that the current entries are equal to 
            table, which is represented as a list. This is only used for 
            testing that the hash table contains what we expect.
        h.print_table prints h.
    """
    def __init__(self, k):
        self.__table = ["-"] * k  
    def lookup(self, pos):
        return self.__table[pos]
    def add(self, pos, data):
        self.__table[pos] = data
    def check(self, table_of_data):
        return self.__table == table_of_data
    def print_table(self):
        print(self.__table)

def hash_quadratic(d):
	#hashtable is 17 as determined by hash function component mod17 (no need to be variable as mod17 restricts the position #max at position 17)
 h = HashTable(17)
 for i in range(len(d)):
 	# hashing function is given as (3k+5)mod17) and quadtratic probing number starts off at zero
	  hashingFunction = ((3*d[i]+5)%17)
	  probeIteration = 0
	  # using given lookup(pos) function using the quadtratic probing function inside (starting at zero), until a free space #has been found (basically iterating probeIteration if position is NOT "-")
	  while h.lookup((hashingFunction+probeIteration**2)%17) != "-":
	    probeIteration = probeIteration + 1
	    #using given add(pos,data) function, where position is determined by the probeIteration value and the original element value from the original array 'd'
	    #plus within the for loop so probIteration value is automatically assigned back to 0.
	  h.add(((hashingFunction+probeIteration**2)%17), d[i])
 return(h.print_table())
	


def hash_double(d):
	#same hashtable size determined by mod17
 h = HashTable(17)
 #extremely similiar format only minor change is switch of quadratic to secondary hash function
 for i in range(len(d)):
	 k = ((3*d[i]+5)%17)
	 j = 0
	 #within lookup() quadratic has been swictched for 2ndry hash function
	 while h.lookup((k+j*(13-((d[i])%13)))%17) != "-":
	    j = j + 1  
	    #same again here with switching
	 h.add(((k+j*(13-((d[i])%13)))%17), d[i])
 return(h.print_table())
