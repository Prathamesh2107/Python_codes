accounts = [
    [8, 5],
    [7, 3],
    [6, 5]
]
wealth=0
for i in accounts:
            temp=0
            for j in i:
                temp+=j
                if temp>wealth:
                    wealth=temp
print(wealth)