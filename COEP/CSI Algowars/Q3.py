def sorted_k_partitions(seq, k):
    n = len(seq)
    groups = []  # a list of lists, currently empty

    def generate_partitions(i):
        if i >= n:
            yield list(map(tuple, groups))
        else:
            if n - i > k - len(groups):
                for group in groups:
                    group.append(seq[i])
                    yield from generate_partitions(i + 1)
                    group.pop()

            if len(groups) < k:
                groups.append([seq[i]])
                yield from generate_partitions(i + 1)
                groups.pop()

    result = generate_partitions(0)

    result = [sorted(ps, key = lambda p: (len(p), p)) for ps in result]
    # Sort partitions by the length of each part, then lexicographically.
    result = sorted(result, key = lambda ps: (*map(len, ps), ps))

    return result


n, k = map(int, input().split())
a = [int(x) for x in input().split()]
counter = 0
for i in range(1,n+1):
    results = sorted_k_partitions(a,i)
    score = 0
    for ele1 in results:
        for ele in ele1:

            score += max(ele) - min(ele)
        if score <= k:
            counter += 1
print(counter + 1)

