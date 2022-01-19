from collections import Counter

def count_chars():
    with open("words.txt", 'r') as f:
        lines = f.readlines()

    lines = [l.strip().lower() for l in lines]
    chars = "".join(lines)

    counter = Counter(chars)
    counts = [(c,n) for c,n in counter.items()]
    counts = sorted(counts, key = lambda i: i[1])
    for c,n in counts:
        print(f"{c}: {n}")

count_chars()
