def reverse(text):
    if type(text) == int:
        print "This function only takes strings"
        return False
    else:
        revlist = []
        newstring = ""
        length = len(text) - 1
        for letter in text:
            revlist.append(letter)
        for i in revlist:
            print revlist[length]
            newstring += revlist[length]
            length -= 1
        return newstring


print reverse("Python!")