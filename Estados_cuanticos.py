import Libcplx as lc
import EspaVectCplx as lct

#  calcular la probabilidad de encontrar una partícula de confinada a un conjunto discreto en una posición en particular
def probParticleInLine(p, ket):
    res = (lc.cplxmod(ket[p][0])/lct.vectorNorm(ket))**2
    return res


# Probabilidad de transitar del primer vector al segundo.
def probTransition(ket1, ket2):
    bra = lct.adjMtx(ket2)
    lal = lct.ProdMtx(bra,ket1)[0][0]
    Nk1 = lct.vectorNorm(ket1)
    Nk2 = lct.vectorNorm(ket2)
    res = lc.cplxcoc(lal,lct.ProdMtx((Nk1,0),(Nk2,0)))
    return res


