num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

# ----- RANGES -----
# The range() function creates integer iterables
print(list(range(0, 5)))

# You can define step
print(list(range(0, 10, 2)))

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])