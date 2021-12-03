NUM_LEN, PATH = 12, r"./data/day_3.txt"
report = open(PATH, "r").read().split("\n")[:-1]

base = [0] * NUM_LEN
for num in report: base = [int(i) + j for i, j in zip(num, base)]

gamma = list(map(lambda x: 1 if x >= len(report) / 2 else 0, base)).__str__()[1:-1].replace(", ", "")
epsilon = list(map(lambda x: 1 if x < len(report) / 2 else 0, base)).__str__()[1:-1].replace(", ", "")

print(int(gamma, 2) * int(epsilon, 2))