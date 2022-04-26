name = ''
for s in "121: Best Time to Buy and Sell Stock":
    if s.isalnum():
        name += s
    if s == ' ':
        name += '_'

print(name)
