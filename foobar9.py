from itertools import chain, combinations
def answer(g):
    return
i = set([n for n in range(16 )])
def powerset_generator(i):
    for subset in chain.from_iterable(combinations(i, r) for r in range(len(i) + 1)):
        yield set(subset)
cnt = 0
for i in powerset_generator(i):
    cnt += 1
print(cnt)
