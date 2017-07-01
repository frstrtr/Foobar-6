def answer(n):
    count = 0
    nodes = set([int(n)])
    temp_nodes = set()
    is_one = 0


    if int(n) == 1:
        return 0
    if int(n) == 3:
        return 2

    while not is_one:
        count += 1
        nodes |= temp_nodes
        two_pwr = 0
        for node in nodes:
            if not node % 2:
                if (node // 2**two_pwr) not in nodes:
                    if node // 2**two_pwr == 1:
                        is_one = 1
                        count += two_pwr
                    temp_nodes.add(node // 2**two_pwr)
                if (node // 2) not in nodes:
                    if node // 2 == 1:
                        is_one = 1
                    temp_nodes.add(node // 2)
            if node % 2:
                plus_cnt = 0
                minus_cnt = 0
                for p in range (1, 1027):
                    if not (node + 1) % 2**p:
                        plus_cnt += 1
                    if not (node - 1) % 2**p:
                        minus_cnt += 1
                    elif (node - 1) % 2**p:
                        break
                    two_pwr = p

                if (node + 1) not in nodes and plus_cnt > minus_cnt:
                    temp_nodes.add(node+1)

                elif (node - 1) not in nodes and minus_cnt > plus_cnt:
                        temp_nodes.add(node-1)

    return count




print(answer(1), end=", ")
print(answer(2), end=", ")
print(answer(3), end=", ")
print(answer(4), end=", ")
print(answer(5), end=", ")
print(answer(6), end=", ")
print(answer(7), end=", ")
print(answer(8), end=", ")
print(answer(9), end=", ")
print(answer(10), end=", ")
print(answer(11), end=", ")
print(answer(12), end=", ")
print(answer(13), end=", ")
print(answer(14), end=", ")
print(answer(15), end=", ")
print(answer(16), end=", ")
print(answer(17), end=", ")
print(answer(18), end=", ")
print(answer(19), end=", ")
print(answer(20), end=", ")
print(answer(21), end=", ")
print(answer(22), end=", ")
print(answer(23), end=", ")
print(answer(24), end=", ")
print(answer(25), end=", ")
print(answer(26), end=", ")
print(answer(27), end=", ")
print(answer(28), end=", ")
print(answer(29), end=", ")
print(answer(30), end=", ")
print(answer(31), end=", ")
print(answer(32), end=", ")
print(answer(65), end=", ")
print(answer(9999999999), end=", ")
print(answer(48112959837082048697 ), end=", ")
#print(answer(719077253944926363091722076315609893447190791576922629093720324630930703222003852530833909289630144084480455519485573430635159075257666489971389722557896497511071573699461941105208878404984376477812331808340023075352602729369851525895652442163308948653402042738345192959788983753918865219341425318496896548865))