def change(**kwargs):
    total = 0
    for k, v in kwargs.items():
        total += int(k)*int(v)
    return total

dictionary = {"1": 3, "5": 2, "25": 13}

total = change(**dictionary)

print(total)