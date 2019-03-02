d1 = {x: x**2 for x in (2,4,6)}
print(d1)

d2 = {x: x**2*x for x in (2,4,6)}

li = ['apple','bat','cat','mat']
d3 = {x[0]: x[-1] for x in li}
print(d3)