def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

print(rata_rata([80, 90, 70]))