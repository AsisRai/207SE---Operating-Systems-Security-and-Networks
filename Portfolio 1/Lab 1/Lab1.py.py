#vocabularies
agent=["bot", "mike"]					
direction=["forward", "backward", "left", "right"]	#saves words as there types
objec=["nut", "plum", "cat", "cup"]
action=["pick", "put", "lift", "drop", "go"]
pronoun=["i", "you", "we"]
colour=["red", "blue"]

sentance= input("Input sentance structure: ")	#take input from user
sentance = sentance.lower()	#takes the input and makes everything lowercase
words = sentance.split() 	#splits string 

#Grammer Rules
correct1=["age", "act", "obj"]
correct2=["age", "act", "col", "obj"]
correct3=["age", "act", "dir"]
correct4=["pro", "act", "obj"]
correct5=["pro", "act", "dir"]		

Nlist=[]			#create a new list

for i in range(len(words)):	#for loop to go through each word in input string
    if words[i] in agent:	#match a word with its type
        Nlist.append("age")	#append age (meaning agent) to the new list
        continue
    elif words[i] in direction:
        Nlist.append("dir")
        continue
    elif words[i] in objec:
        Nlist.append("obj")
        continue
    elif words[i] in action:
        Nlist.append("act")
        continue
    elif words[i] in pronoun:
        Nlist.append("pro")
        continue
    elif words[i] in colour:
        Nlist.append("col")
        continue		#output will be a list like ["age", "act", "obj"]


if Nlist == correct1:		#match Nlist with a grammer rule, if it matches then print correct grammer, if not then print Incorrect grammer
    print (" Correct Grammer! ")
elif Nlist == correct2:
    print (" Correct Grammer! ")
elif Nlist == correct3:
    print (" Correct Grammer! ")
elif Nlist == correct4:
    print (" Correct Grammer! ")
elif Nlist == correct5:
    print (" Correct Grammer! ")
else:
    print ("Incorrect Grammer!")		
