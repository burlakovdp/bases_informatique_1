def est_permutation(L):
    mem_list =[]
    for e in L:
        if e not in mem_list:
            mem_list.append(e)
        else:
            return False
    return True
