#!/usr/bin/python3

def nouvelle_matrice(n,m):
    M = []
    for i in range(n):
        L = []
        for j in range(m):
            L.append(False)
        M.append(L)
    return M


def dimensions(M):
    return (len(M), len(M[0]))
