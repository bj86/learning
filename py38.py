ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # this method returns the number of elements in the list.
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # given a negative integer, the script will read backwards.
print stuff.pop() # removes and returns the given position in the list.
print ' '.join(stuff) # str.join(sequence) - This is a sequence of the elements to be joined.
print '#'.join(stuff[9:7]) # Joins the elements at the given positions. 
print stuff[8:6]