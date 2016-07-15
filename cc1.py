answer = raw_input('--> ')

def the_flying_circus():
    
    print "Select a number beteen 1 and 10."   
    if type(answer) is not int or int(answer) in range(10, 999) and range(-999,0):
        print "You didn't pick a valid number."
        return False
        
    elif int(answer) in range(0, 10):
        print answer
        print "I chose a number between one and ten!"
        return True
		
    else:
        return 0
		

# start the script
the_flying_circus()       