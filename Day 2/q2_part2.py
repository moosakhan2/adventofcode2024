data = []

print("Enter the data (type 'done' to stop):")

# Read and process input
while True:
    line = input()
    if line.lower() == 'done':
        break
    # Convert the line into a pair of integers
    numbers = list(map(int, line.split()))
    data.append(numbers)

safecounter = 0



for j in range(len(data)):
    myarray = data[j]
    increasing = False
    decreasing = False
    increasing_counter = 0
    decreasing_counter = 0
    unsafe = False
    noofcorrections = 0
    for s in range(len(myarray)-1):
        if myarray[s] == myarray[s+1]:
            if noofcorrections != 0:
                unsafe = True
                break
            else:
                noofcorrections += 1

        elif (myarray[s] > myarray[s+1]) and (abs(myarray[s]-myarray[s+1]) <= 3):
            decreasing_counter += 1
            decreasing = True
            if (increasing == True) and (decreasing_counter>1) and (noofcorrections > 0):
                unsafe = True
                break
            elif (increasing == True) and (decreasing_counter == 1):
                noofcorrections += 1
                increasing = False
                decreasing = False
        
        elif (myarray[s] < myarray[s+1]) and (abs(myarray[s]-myarray[s+1]) <= 3):
            increasing_counter +=1
            increasing = True
            if (decreasing == True) and (increasing_counter > 1) and (noofcorrections > 0):
              unsafe = True
              break
            elif (decreasing == True) and (increasing_counter == 1):
                noofcorrections += 1
                decreasing = False
                increasing = False
  
        else:
            unsafe = True
            break
    if (unsafe != True):
      print(f"Safe")
      safecounter += 1
    else:
        print("Unsafe")

print(safecounter)
        
  




