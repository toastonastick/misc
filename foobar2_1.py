def answer(x):
    dictionized = {k: k[::-1] for k in set(x)}
    count = 0
    for v in dictionized.values():
        if (len(v) < 2) or (v == v[::-1]) or v not in dictionized:
            count += 1
    return (len(dictionized)+count)//2

xlists = ["foo", "bar", "oof", "bar"]
print(str(answer(xlists)))
xlists = ["x", "y", "xy", "yy", "", "yx"]
print(str(answer(xlists)))
