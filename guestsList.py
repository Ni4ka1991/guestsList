#!/usr/bin/env Python3

from os import system


# ### DATA #################

guests_1 = [
 "Bethaney Bain",
 "Kacey Johns",
 "Manpreet Saunders" 
 ] 

guests_2 = [
 "Elwood Curtis",
 "Diya Griffin",
 "Kacey Johns"
 ]

guests_3 = [
 "Tobey Weiss",
 "Kadie Barnes",
 "Diya Griffin" 
 ]


# ### DATA ################

# ### LOGIC ##############

finalList = []

guests_1 += guests_2
guests_1 += guests_3

for i in guests_1:
 if i not in finalList:
  finalList.append( i )

finalList.sort()

# ### LOGIC ############


# ### VIEW #############
n = 1
system( "clear" )
print( "GUESTS LIST:\n" ) 
for i in finalList:
 print( f"{ n } > { i }" )
 n += 1
print()
# ### VIEW #############
