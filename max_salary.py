accounts = [
    [1, 5],
    [7, 3],
    [3, 5]
]
wealth=0
for i in accounts:
            temp=0
            for j in i:
                temp+=j
                if temp>wealth:
                    wealth=temp
print(wealth)