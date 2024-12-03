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

    array1=[]
    array2=[]

for i in range(len(data)):
    array1.append(data[i][0])
    array2.append(data[i][1])
  

mytotalvalue = 0
for s in range(len(data)):
    counter = 0
    myvalue = array1[s]
    for j in range(len(array2)):
        if array2[j] == myvalue:
            counter +=1
    mytotalvalue += counter * myvalue

print(mytotalvalue)


