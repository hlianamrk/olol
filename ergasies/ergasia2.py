print("Type 20 numbers")
x = [int(i) for i in input().split()]

top5 = x[:5]
max5=max(top5)


next51=x[5:10]
max51=max(next51)


next52=x[10:15]
max52=max(next52)


last5=x[15:20]
maxlast5=max(last5)


print(('4:00pm', max5), ('5:00pm', max51), ('6:00pm', max52), ('7:00pm', maxlast5))