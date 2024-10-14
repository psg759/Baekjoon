n = int(input())
drink = list(map(int, input().split()))


drink.sort(reverse = True)
energy = drink[0]

for i in range(1, n):
    energy += (drink[i]/2)

print(energy)