#question2 of advent of code
#global variables
main_list = []
safe_count = 0
#subprograms

def valid_checker(report): #goes through each report in main_list and checks if it is valid
  safe = 0
  descending = False
  ascending = False
  if report == sorted(report):
    ascending = True
  elif report == sorted(report,reverse=True):
    descending = True
  
  if descending == True or ascending == True:
    for i in range(len(report)-1):
      difference = abs(report[i] - report[i+1]) 
      if difference > 0 and difference <4:
        safe = 1
      else:
        safe = 0
        return(safe)
  if safe == 1:
    difference = abs(report[len(report)-1] - report[len(report)-2])
    if difference > 0 and difference <4:
        safe = 1
  else:
    safe = 0
  return(safe)

  
 
#main code
with open("day2/question2_input.txt","r") as input_file:
  for line in input_file:
    main_list.append(line) #put all into one big list
    
for i in range (len(main_list)):
  main_list[i] = main_list[i].split() #splitting into groups of strings
  
for i in range(len(main_list)): #turning stings into integers
  secondary_index = 0
  mini_len = len(main_list[i])
  while secondary_index < (mini_len):
    main_list[i][secondary_index] = int(main_list[i][secondary_index])
    secondary_index += 1

for i in range(len(main_list)):
  safe_count = safe_count + valid_checker(main_list[i]) #checks for safe reports
  
print("The number of safe reports is:",safe_count)
