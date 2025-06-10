#recursion
#for factorial numbers
def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))

#WAP to make a flatten list using recursion of given 
#a = [1,2,2,2,2,[1,55,23], "sudan","hello","testing",["hello", "world"]]

#def flatten_list(nested_list, flat_list=None):
 #   if flat_list is None:
  #      flat_list = []  # Initialize the flat list

   # for item in nested_list:
    #    if isinstance(item, list):
     #       flatten_list(item, flat_list)  # Recursive call with positional arguments
      #  else:
       #     flat_list.append(item)  # Use list method append

    #return flat_list

# Given list
#a = [1, 2, 2, 2, 2, [1, 55, 23], "sudan", "hello", "testing", ["hello", "world"]]

# Calling the function
#flattened = flatten_list(a)

#print("Flattened List:", flattened)

a = [1, 2, 2, 2, 2, [1, 55, 23], "sudan", "hello", "testing", ["hello", "world"]]
def flatten_list(data):
    flat_list = [1]
    for i in data:
        if isinstance(i,list):
            flat_list.extend(flatten_list(i))
        else:
            flat_list.append(i)
    return(flat_list)
print(flatten_list(a))
