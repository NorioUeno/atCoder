#!/opt/homebrew/bin/python3

import json


sales_record = [
    {1000,"AAA", "B",100}
    ,{1000,"BBB", "B",100}
    ,{1001,"AAA", "A",300}
    ,{1002,"CCC", "A",200}
    ,{1003,"AAA", "A",100}
    ,{1003,"BBB", "B",100}
]

sales_hisory = [
    {1000, "AAA"}
    ,{1000, "BBB"}
    ,{1001, "AAA"}
    ,{1002, "CCC"}
    ,{1003, "AAA"}
]


# print(sales_hisory)

output = []

for parson in sales_hisory:
    frequency = 0
    print(list(parson)[0])
    for salese in sales_record:
        if parson[0] == salese[0]:
            frequency += 1
    output.append({parson[0]:frequency})

print(output)