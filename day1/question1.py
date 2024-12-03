#question1 of advent of code

#subprograms
def distance_checker(code1,code2):
    if code1 > code2:
        distance = code1 - code2
    else:
        distance =code2 - code1
    return(distance)

#global variables
overall_distance = 0
list_main = []
codelist1 = []
codelist2 = []
reading = True
#main code
with open("day1/question1_input.txt","r") as input_file:

    #read word by word
    for line in input_file:
        
        for number in line.split():
            list_main.append(number)

#sort into 2 lists
for i in range (len(list_main)):
    if (i == 0) or (i % 2) == 0:
        codelist1.append(list_main[i])
    else:
        codelist2.append(list_main[i])
        
#sort lists
codelist1.sort()
codelist2.sort()

#turning str into int
for i in range (len(codelist1)):
    codelist1[i] = int(codelist1[i])
    codelist2[i] = int(codelist2[i])
#get distance
for i in range (len(codelist1)):
    distance_add = distance_checker(codelist1[i],codelist2[i])
    overall_distance = overall_distance + distance_add
    
print("the overall distance is",overall_distance)