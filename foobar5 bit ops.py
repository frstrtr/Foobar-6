def answer(n):
    bin_str = bin(int(n))[2:]
    count = 0
    rev_str = bin_str[::-1]
    nodes = set([rev_str])
    temp_nodes = set()
    is_one = False

    while not is_one:
        count += 1
        nodes |= temp_nodes
        for node in nodes:
            next_one = rev_str.find("1",1) if rev_str.find("1",1) > 0 else 0
            if rev_str[0] == "1":
                if rev_str.count("0",1, next_one) > 0 or rev_str == "11":
                    if str(int(rev_str[::-1])-1)[::-1] not in nodes:
                        temp_nodes.add(str(int(rev_str[::-1])-1)[::-1])
                        #count += 1
                else:
                    if str(int(rev_str[::-1])+1)[::-1]:
                        temp_nodes.add(str(int(rev_str[::-1]) + 1)[::-1])
                        #count += 1
            else:
                count += node.count("0",0, next_one)
                temp_nodes.add(rev_str[next_one:])

            if node == "1":
                is_one = True
    ones = bin_str.count("1")
    zeros = bin_str.count("0")
    ops = 2 * (ones-1) + zeros
    print("n: ", n, " ", "count: ", count, "ops: ", ops)
    return count

answer("1")
answer("2")
answer("3")
answer("4")
answer("5")
answer("6")
answer("7")
answer("8")
answer("9")
answer("10")
answer("65")
answer("1000020100")
answer("9999999999")
answer("989898989898989")
answer("32")
answer("48112959837082048697")
answer("719077253944926363091722076315609893447190791576922629093720324630930703222003852530833909289630144084480455519485573430635159075257666489971389722557896497511071573699461941105208878404984376477812331808340023075352602729369851525895652442163308948653402042738345192959788983753918865219341425318496896548864")
answer("719077253944926363091722076315609893447190791576922629093720324630930703222003852530833909289630144084480455519485573430635159075257666489971389722557896497511071573699461941105208878404984376477812331808340023075352602729369851525895652442163308948653402042738345192959788983753918865219341425318496896548865")