'''
Tengo cuatro enteros positivos, A, B, C y D, donde A < B < C < D. La entrada es una lista de los enteros A, B, C, D, AxB, BxC, CxD, DxA en algún orden.
Su tarea es devolver el valor de D.
'''

def alphabet(ns):
    sn = sorted(ns)
    print(sn)
    A   = sn.pop(0)
    print(sn)
    B   = sn.pop(0)
    print(sn)
    CxD = sn.pop()
    print(sn)
    AxB = sn.pop(sn.index(A * B))
    print(sn)
    C   = sn.pop(0)
    print(sn)
    BxC = sn.pop(sn.index(B * C))
    print(sn)
    DxA = sn.pop()
    print(sn)
    D   = sn.pop()
    return D