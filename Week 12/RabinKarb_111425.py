def rabin_karp(text, pattern):

    d = 256
    q = 101

    n = len(text)
    m = len(pattern)

    if m > n:
        return []

    p = 0
    t = 0
    h = 1

    for _ in range(m - 1):
        h = (h * d) % q

        for i in range(m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i])) % q

    occurrences = []

    for s in range(n - m + 1):
        if p == t:
            match = True

            for j in range(m):
                if text[s + j] != pattern[j]:
                    match = False
                    break
            if match:
                occurrences.append(s)

        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q

            if t < 0:
                t += q
    return occurrences

# Demo
if __name__ == "__main__":
    T = "ABABDABACDABABCABAB"
    P = "ABABCABAB"

    result = rabin_karp(T, P)
    print("Pattern found at indices: ", result)