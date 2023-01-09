dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dict_num=dic1|dic2|dic3



for key in dict_num:
    print("key:", key)

for value in dict_num.values():
    print("value:", value)

for item in dict_num.items():
    print("Item:", item)