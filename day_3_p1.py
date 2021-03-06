report = open(r"./data/day_3.txt", "r").read().split("\n")[:-1]

base = [0] * 12
for num in report: base = [int(i) + j for i, j in zip(num, base)]

gamma = "".join(list(map(lambda x: "1" if x >= len(report) / 2 else "0", base)))
epsilon = "".join(list(map(lambda x: "1" if x < len(report) / 2 else "0", base)))

print(int(gamma, 2) * int(epsilon, 2))
