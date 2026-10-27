def status_lulus(nilai):
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


test_case = [
    (75, "Lulus"),
    (60, "Lulus"),
    (59, "Tidak lulus"),
]

for nilai, expected in test_case:
    actual = status_lulus(nilai)

    if actual == expected:
        print("PASS", nilai)
    else:
        print("FAIL", nilai, "Expected:", expected, "Actual:", actual)