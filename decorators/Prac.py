import time 

def timer(func):
    def wrapper(*args,**kwargs): 
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func._name_} rand in {end-start} ran in {end-start} time")
        return result
    return wrapper  

@timer # decorater functon ,itmakes the ex_function to go from timmer fucnction compulsory 
def ex_function(n):
    time.sleep(n)
    
ex_function(2)