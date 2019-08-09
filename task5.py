# Frequency analysis #


def freq_analysis(line):
    from string import ascii_lowercase
    freq = dict(zip(ascii_lowercase, [0] * len(ascii_lowercase)))
    for char in line:
        if char in freq:
            freq[char] += 1

    items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return items


if __name__ == "__main__":
    line = input().lower()
    items = freq_analysis(line)
    print(f"{items[0][0]} {items[0][1] / len(line) * 100 : .3f}%")
    print(f"{items[1][0]} {items[1][1] / (len(line)) * 100 : .3f}%")
