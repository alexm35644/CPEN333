import multiprocessing

# Exceptions 

try: 
    print(1/1)
except ZeroDivisionError: # This only catches this specific exception 
    print("exception") 
except:                   # This catches any exception 
    print("exception: it will be other than divide by zero") 
else:                     # Don't need this here but gives an extra option if it runs
    print("no exception")
finally:                  # This executes regardless  
    print("finally is executed")
    # Responsible for releasing rescourses like closing file 

# Multi processing 

print("CPU Count:", multiprocessing.cpu_count())
