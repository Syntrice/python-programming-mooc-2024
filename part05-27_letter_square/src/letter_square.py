# Write your solution here
layers = int(input("Layers:"))

grid = [[chr(64 + layers) for col in range(layers*2-1)] for row in range(layers*2-1)]

for i in range(1, layers):
    for row in range(i, len(grid)-i):
        for col in range(i, len(grid[0])-i):
            grid[row][col] = chr(64 + layers - i)
    
for row in range(len(grid)):
    for col in range(len(grid[0])):
        print(grid[row][col], end="")
    print()