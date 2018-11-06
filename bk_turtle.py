list_number = [1,23,34,12,-1,0,3]
any = ['a',1,2.3,'xx',1,23,2.34,'adf','awer']
# fliter data in python .

# append , sort , remove , pop, index
print(list_number)
# list_number.pop()
# print(list_number)
list_number.append(-20)
list_number.append(80)

myName = "abdulrahman"
list_my_name = list(myName)
list_number.sort()
print(list_my_name)

list_coll = [1,'a','cat','rat',10,True,2.5,'awesome']
list_str = [item for item in list_coll if isinstance(item, str)]
print(list_str)
