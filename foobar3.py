def answer(s):
    salute_sum = 0
    s = s.replace("-", "")
    #print(s," ", len(s))
    for i, c in enumerate(s):
        #print(c, i)
        if c == ">":
            #print (i, s.count("<", i))
            salute_sum += 2*s.count("<", i)
    return salute_sum


print(answer(">----<"))
print(answer("<<>><"))