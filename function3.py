def sum(a,b):
    try:

         return a + b
    except TypeError:
        raise Exception("Too many parameters provided. This function only accepts up to 2 parameters.")
print(sum(1,2,5))   
    