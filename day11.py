print ("positional")
def test(first,last):
    print(first,last)

test("sudan","bhandari")
test("bhandari","sudan")



print("keyword")
def test(first,last):
    print(first,last)
test(first="sudan",last="bhandari")
test(last="bhandari",first="sudan" )

    
def test2(first, last="thapa"):
    print(first,last)
    test2(first="sudan")
    test2(first="sudan", last="KC")


a= [1,2,3,3,4]
sum = 0
for i in a:
    sum = sum+i
print(sum)


def testing(*data):
    sum = 0
    for i in data:
        sum = sum+i
    return sum

print(123,2324,324,2234,23,2323,423,324)

def calculate_average(*data):
    if len(data)==0:
        return 0
    length = len(data)
    sum = 0
    for i in data:
        sum = sum+i
        avg = sum/length
    return avg
    
print("average of given numbers is",calculate_average(2,3,4,5))


#value = concatenate_string()


def merge_dicts(**kwargs):
    merge = 0
    for d in kwargs.values():
        if isinstance(d.dict):
            merge.update(d)
        else:
            raise ValueError("all values must be dictionaries.")
    return merge

    dict1 = {"'a'= 1, 'b'= 2"}
    dict2 = {"'b'= 3, 'c'=4"}

    result = merge_dicts(first = dict1, second = dict2,)

def flexible_calculator(*args, **kwagrs):
    pass

    for value in args:

     flexible_calculator(1,2,3,4,5,6, operation = "add")
     
    