import collections

def swapchars(phrase):
    cnt = collections.Counter(phrase.translate(None, " ?.!/;:"))
    least = cnt.most_common()[-1][0]
    most = cnt.most_common()[0][0]
    newstr = ""
    for char in phrase:
        if char == least:
            newstr += most
        elif char == most:
            newstr += least
        else:
            newstr += char
    return newstr
	
#####################################################################

def sortcat(n, *args):
    lst = []
    finlst = ""
    for string in args:
	    lst.append(string)
    lst.sort(key = len, reverse = True)
    lst.insert(0, 'Don\'t use 0 as the argument please!')
    lst2 = lst[1:n]
    lst2.append(lst[n])
    for strs in lst2:
        finlst += strs
    return finlst
	
#####################################################################

file = open("states.txt", "r")
abbrev = {}
for line in file:
    full,abrv = line.split(",")
    abrv = abrv[0:len(abrv)-1]
    abbrev[abrv] = full

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

def abb_lookup (state):
    full = (full for full,abrv in abbrev.items() if abrv==state).next()
    return full

def abbs_lookup (dic, *args):
    states = []
    for state in args:
        full = (full for full,abrv in abbrev.items() if abrv==state).next()
        states.append(full)
    return states
