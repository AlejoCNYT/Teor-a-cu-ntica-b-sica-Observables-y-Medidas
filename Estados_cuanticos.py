from math import exp

import numpy
import Libcplx as lc
import EspaVectCplx as lct

# Probabilidad de encontrar una partícula de confinada a un conjunto discreto en una posición en particular
def probParticleInLine(p, ket):
    res = (lc.cplxmod(ket[p][0])/lct.vectorNorm(ket))**2
    return res


# Probabilidad de transitar de un ket a otro
def probTransition(ket1, ket2):
    bra = lct.adjMtx(ket2)
    lal = lct.ProdMtx(bra,ket1)[0][0]
    Nk1 = lct.vectorNorm(ket1)
    Nk2 = lct.vectorNorm(ket2)
    res = lc.cplxcoc(lal,lct.ProdMtx((Nk1,0),(Nk2,0)))
    return res

# Probabilidades como módulo cuadrado de un complejo
def probabilidad(a):
    return lc.cplxmod(a)**2


# Valor esperado 
def expVal(m, ket):
    try:
        if lct.hermMtx(m):
            bra = lct.adjMtx(lct.ProdMtx(m,ket))[0]
            for k in range(len(bra)):
                bra[k]=[(bra[k])]
            M = lct.ProdMtx(lct.trMtx(bra), ket)[0][0]
            return M
    except:
        return 'No es posible realizar esta operación'


# Varianza
def Var(m, ket):
    try:
        n = len(m)
        if lct.hermMtx(m):
            bra = lct.adjMtx(lct.ProdMtx(m,ket))[0]
            for k in range(len(bra)):
                bra[k]=[(bra[k])]
            a = lct.MultEscalarVector(expVal(m, ket),lct.idMtx(n))
            b = lct.sumaMatrix(m,lct.invAdMtx(a))
            var = lct.ProdMtx(lct.ProdMtx(lct.adjMtx(ket), lct.ProdMtx(b,b)),ket)[0][0]
            return var
    except:
        return 'No es posible realizar esta operación'


# Normalizar vectores
def normVec(o):
    m = numpy.array(o)
    e = numpy.linalg.eig(m)
    n = len(e[1])
    l = len(vectores)
    vectors = []
    for i in range(n):
        v = []
        for j in range(len(e[1][i])):
            v += [[(e[1][i][j].real,e[1][i][j].imag)]]
        vectors += [v]
    normaV = []
    for k in range(l):
        normaV += normaV(vectors[k])
    return normaV


# Valores propios de un observable
def eigenValuesObs(o):
    m = numpy.array(o)
    e = numpy.linalg.eig(m)
    values = []
    for k in range(len(e[0])):
        values += [(e[0][k].real,e[0][k].imag)]
    return values


# Probabilidad de transitar a un eigenvector
def eigenProb(v,e):
    probabilidades = []
    m = len(e)
    bra = lct.adjMtx(v)[0]
    n = len(bra)
    for i in range(n):
        bra[i]=[(bra[i])]
    for j in range(m):
        probabilidades += [((lc.cplxmod(lct.ProdMtx(lct.trMtx(bra), e)[0][0]))**2,0)]
    return probabilidades


# Valor medio
def meanValue(z,e):
    mean = []
    res = (0, 0)
    lz = len(z)
    lm = len(mean)
    for i in range(lz):
        mean += [lc.cplxproduct(z[i], e[i])]
    for j in range(lm):
        res = lc.cplxsum(mean[j],res)
    return res


# Estado final de una matriz unitaria
def dinamic(s,m,q0):
    if lct.unitaria(m):
        if s == 1:
            res = lct.ProdMtx(m,q0)[0]
        else:
            for i in range(s):
                m = lct.ProdMtx(m, m)
            res = lct.ProdMtx(m,q0)[0]
    return res

