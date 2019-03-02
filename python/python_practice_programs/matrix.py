# mat = []
# for x in range(5):
#     for y in range(5):
#         mat.append([x,y])
# print(x,y)

mat = [[x,y] for x in range(5) for y in range(5)]
print(mat)
print(len(mat))
for m in range(4):
    print(m)

# x = [int(x) for x in input().split(',')]
# print(x),