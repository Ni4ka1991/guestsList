#!/usr/bin/env Python3

from os import system


# ### DATA #################

guests_1 = [ "Bethaney Bain", "Kacey Johns", "Manpreet Saunders" ]
guests_2 = [ "Elwood Curtis", "Diya Griffin", "Kacey Johns" ]
guests_3 = [ "Tobey Weiss", "Kadie Barnes", "Diya Griffin" ]


# ### DATA ################


system( "clear" )

guests_1 += guests_2
guests_1 += guests_3

print( guests_1 )


#guests_1.extend( guests_2 )
#print( guests_1 )
