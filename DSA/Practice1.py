#Time Complexity 
#Techniquens to measure it :  1.By clock 

#By clock 
import time 

start = time.time()
for i in range(1,101):
    print(i)
print(time.time()-start)

# same code in while loop 
i=1
while i<101:
    i+= 1
print("time using while loop",time.time()-start)