# print natural number from 1 to n 
# last_num = int(input("enter the last number: "))
 
# print("list of the numbers from 1 to {}".format(last_num))

# for i in range(1,last_num+1):
#     print(i,end=" ")
    
# print natural number from 1 to n inn reverse order 

last_num = int(input("enter the last number: "))
 
print("list of the numbers from {} to 1".format(last_num))

for i in range(last_num,0,-1):
    print(i,end=" ")