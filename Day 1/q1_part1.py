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
  
array1.sort()
array2.sort()

distance_counter = 0

for i in range(len(array1)):
    distance_counter += abs(array1[i] - array2[i])


print(distance_counter)

