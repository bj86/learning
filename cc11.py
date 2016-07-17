def anti_vowel(text):
    if type(text) == int:
        return False
    else:
        newstring = ""
        print "Input: %s" % text
        for c in text:
            if c in "aeiouAEIOU":
                print "Deleting vowel %s" % c
                newstring += ""
            else:
                newstring += c
        print "Result: %s" % newstring        
        return newstring

print anti_vowel("sveinur")