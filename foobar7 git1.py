
def generate_combinations(q, n):
    answer = []
    i = 1
    while i <= n:
        answer.extend(generate_branch(q - n, i, q, [i]))
        i += 1

    return answer


def generate_branch(depth_left, current_branch_value, total_rabbits_available, items_so_far):
    if depth_left == 0:
        return [items_so_far]

    if depth_left > 0 and current_branch_value <= total_rabbits_available:
        i = current_branch_value + 1
        accumulated = []
        highest_branch_value = total_rabbits_available - depth_left + 1

        while i <= highest_branch_value:
            next_array = items_so_far[:]
            next_array.append(i)
            accumulated.extend(generate_branch(depth_left - 1, i, total_rabbits_available, next_array))
            i += 1

        return accumulated


def generate_key_holders(q, n):
    combinations = generate_combinations(q, n)
    minion_list = [[] for q in xrange(q)]
    for index, item in enumerate(combinations):
        for key in item:
            minion_list[key-1].append(index)

    return minion_list


def answer(num_buns, num_required):

    return generate_key_holders(num_buns, num_required)

# print(answer(4, 2))
print(answer(5, 1))
print(answer(5, 2))
print(answer(5, 3))
print(answer(5, 4))
print(answer(5, 5))
# print(answer(3, 1))
# print(answer(2, 2))
# print(answer(3, 2))
# print(answer(5, 3))
# print(answer(4, 4))
# print(answer(2, 1))