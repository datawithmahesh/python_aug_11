a = {
    "name":"mahesh",
    "age":25,
    "gender":"mahesh",
}
print(a["name"])
print(a.keys())
print(a.values())

# print (a['ages'])
print(a.get('age', 'not found'))


# add to dict
a["phone"] = "23345677654"
a['age'] = 30
print(a)

myfamily = {
  "child1" : {
    "name" : "ramesh",
    "year" : 1990
  },
  "child2" : {
    "name" : "kalawati",
    "year" : 1996
  },
  "child3" : {
    "name" : "mahesh",
    "year" : 2000
  }
}
print(myfamily.values())

userdetails = {
    "name": "gokul",
    "age": 24,
    "gender":"male",
    "phone": {
        "type":"ntc",
        "number":"1234567890"
    }
}
print(f"my phone mumber of {userdetails['phone']['type']} is {userdetails['phone'] ['number']}")