import matplotlib.pyplot as plt
import time 
import random
#sort function
def Bubble_Sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                 arr[j], arr[j+1] = arr[j+1], arr[j]


    return arr

#creation of arrays
arr_1 = []
for i in range(1,11):
    arr_1.append(random.randint(1,100))

arr_2=[]
for i in range(1,101):
    arr_2.append(random.randint(1,100))

arr_3=[]
for i in range(1,1001):
    arr_3.append(random.randint(1,1000))

arr_4=[]
for i in range(1,10001):
    arr_4.append(random.randint(1,1000))


#measuring time for the different arrays being sorted

start_time= time.time()
Bubble_Sort(arr_1)
end_time= time.time()
elapsed_time_1= start_time - end_time
print(f"Bubble sort time for n=10: {elapsed_time_1} seconds")

start_time= time.time()
Bubble_Sort(arr_2)
elapsed_time_2= start_time - end_time
print(f"Bubble sort time for n=100: {elapsed_time_2} seconds")

start_time= time.time()
Bubble_Sort(arr_3)
elapsed_time_3= start_time - end_time
print(f"Selection sort time for n=1000: {elapsed_time_3} seconds")

start_time= time.time()
Bubble_Sort(arr_4)
elapsed_time_4= start_time - end_time
print(f"Bubble Sort sort time for n=10000: {elapsed_time_4} seconds")


#plotting the graph

x = [10, 100, 1000, 10000]

y =[elapsed_time_1,elapsed_time_2,elapsed_time_3,elapsed_time_4]


plt.plot(x,y)

plt.xlabel("Size of array (n)")
plt.ylabel("Time complexity (seconds)")
plt.title("Time complexity of sorting algorithms")

# display the graph
plt.show()
