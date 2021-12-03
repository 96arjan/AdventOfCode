report = open(r"./data/day_3.txt", "r").read().split("\n")[:-1]

def do_recur(report, index, co2):
    if len(report) == 1: return report[0]
    ones, zeros, count = [], [], 0
    for num in report:
        if int(num[index]): count, ones = count + 1, ones + [num]
        else: count, zeros = count - 1, zeros + [num]
    if co2: count = - (count + 1)
    if count >= 0: report = ones
    else: report = zeros
    return do_recur(report, index + 1, co2)

print(int(do_recur(report, 0, True), 2) * int(do_recur(report, 0, False), 2))
