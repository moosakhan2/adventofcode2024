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
    unsafe = False
    for s in range(len(myarray)-1):
        if myarray[s] == myarray[s+1]:
            unsafe = True
            break
        elif (myarray[s] > myarray[s+1]) and (abs(myarray[s]-myarray[s+1]) <= 3):
            decreasing = True
            if increasing == True:
                unsafe = True
                break
        elif (myarray[s] < myarray[s+1]) and (abs(myarray[s]-myarray[s+1]) <= 3):
            if decreasing == True:
              unsafe = True
              break
            increasing = True
        else:
            unsafe = True
            break
    if (unsafe != True):
      print(f"Safe")
      safecounter += 1
    else:
        print("Unsafe")

print(safecounter)
        
  




