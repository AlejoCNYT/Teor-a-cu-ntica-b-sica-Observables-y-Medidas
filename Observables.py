import Estados_cuanticos as qs
import EspaVectCplx as lct
import Libcplx as lc

def S1():
    Ket = [[(-3, -1)], [(0, -2)], [(0, 1)], [(2, 0)]]
    ket1 = [[(1,0)], [(0,-1)]]
    ket2 = [[(0, 1)], [(1, 0)]]
    prob = qs.probParticleInLine(2, Ket)
    A = qs.probTransition(ket1, ket2)
    print(prob)
    print(lc.cplxtruncar(A, 2))
    print(qs.probabilidad(A))

def EX431a():
    sa = [[0,1],[1,0]]
    sb = [[(0,0),(1,0)],[(1,0),(0,0)]]
    s0 = [(1,0),(0,0)]
    values = qs.eigenValuesObs(sa)
    Sn = lct.MtxVec(sb, s0)
    l = len(final)
    for i in range(l):
        Sn[i] = [Sn[i]]
    print(values)
    print(Sn)
    