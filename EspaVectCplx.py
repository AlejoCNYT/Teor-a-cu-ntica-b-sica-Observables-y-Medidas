import Libcplx as lc


# 1.Adición de vectores complejos
def adVector(v, w):
    n = len(v)
    r = []
    for k in range(n):
        r += [lc.cplxsum(v[k], w[k])]
    return r


# 2.Inverso (aditivo) de un vector complejo
def invVector(v):
    n = len(v)
    r = []
    for k in range(n):
        r += [lc.cplxproduct((-1, 0), v[k])]
    return r


# 3.Multiplicación de un escalar complejo
def MultEscalarVector(v, w):
    n = len(w)
    r = []
    for k in range(n):
        r += [lc.cplxproduct(v, w[k])]
    return r



# 4.Adición de matrices complejas
def sumaMatrix(v, w):
    try:
        m = len(w)
        n = len(v[0])
        fila = []
        r = [fila] * m
        for j in range(m):
            fila = []
            r[j] = fila
            for k in range(n):
                r += [lc.cplxsum(v[j][k], w[j][k])]
        return r
    except:
        return 'No es posible realizar la operación'


# 5.Inversa (aditiva) de una matriz compleja
def invAdMtx(v):
    m = len(v)
    n = len(v[0])
    r = [n] * m
    for j in range(m):
        fila = []
        r[j] = fila
        for k in range(n):
            r[j] += [lc.cplxproduct((-1,0), v[j][k])]
    return r


# 6. Multiplicación de un escalar por una matriz compleja
def MultEscMtx(v, w):
    m = len(w)
    n = len(w[0])
    r = [n] * m
    for j in range(n):
        fila = []
        r[j] = fila
        for k in range(m):
            r[j] += [lc.cplxproduct(v, w[j][k])]
    return r


# 7. Transpuesta de una matriz/vector
def trMtx(v):
    m = len(v)
    n = len(v[0])
    r = [n] * m
    for j in range(n):
        fila = []
        r[j] = fila
        for k in range(m):
            r[j] += [v[k][j]]
    return r


# 8. Conjugada de una matriz/vector
def conjMtx(A):
    m = len(A)
    n = len(A[0])
    r = [n] * m
    for j in range(n):
        fila = []
        r[j] = fila
        for k in range(m):
            r[j] += [lc.cplxconj((-1,0), A[j][k])]
    return r


# 9.Adjunta (daga) de una matriz/vector
def adjMtx(A):
    return trMtx(conjMtx(A))


# 10.Producto de dos matrices (de tamaños compatibles)
def ProdMtx(A, B):
    try:
        m = len(A)
        n = len(A[0])
        fila = [(0, 0)] * n
        r = [fila] * m
        for j in range(m):
            fila = [(0, 0)] * n
            r[j] = fila
            for k in range(n):
                r[j][k] = lc.cplxproduct(A[j][k], B[j][k])
        return r
    except:
        return 'No es posible realizar la operación'


# 11. Función para calcular la "acción" de una matriz sobre un vector
def MtxVec(A, B):
    try:
        m = len(A)
        n = len(A[0])
        fila = [(0, 0)] * n
        r = [fila] * m
        for j in range(m):
            fila = [(0, 0)] * n
            r[j] = fila
            for k in range(n):
                r[j][k] = lc.cplxproduct(A[j][k], B[j][k])
        return r
    except:
        return 'No es posible realizar la operación'


# 12. Producto interno de dos vectores
def vectorPrInt(v,w):
    r = ProdMtx(adjMtx(v),w)[0][0]
    return r


# 13. Norma de un vector
def vectorNorm(v):
    r = sqrt(vectorPrInt(v,v)[0])
    return r


# 14. Distancia entre dos vectores
def disV(v,w):
    ele = 0
    s = 0
    for i in range(len(v)):
        ele = v[i]-w[i]
        ele = ele**2
        s += ele
    len(v)
    n = [(adVector(v,invVector(w))[k])] for k in range (l) ]
    return vectorNorm(n)


# Genera matriz identidad nxn
def idMtx(v):
    for k in range(v):
        m[k][k] = (1.0,0.0)
    return m


# 15. Revisar si una matriz es unitaria
def unitaria(m1, conjMtx(trMtx(m1))):
    if ProdMtx(a,adjMtx(a)) == idMtx(len(a)):
        ans = True
    else:
        ans = False
    return ans


# 16. Revisar si una matriz es Hermitiana
def hermMtx(v):
    if adjMtx(v) == v:
        return True
    else:
        return False


# 17. Producto tensor de dos matrices/vectores
def vectorTsorProduct(A, B):
    l1 = len(A)
    l2 = len(B)
    m = [[[[]]for j in range(len(A[0])*len(B[0]))]for i in range(l1*l2))]
    for i in range(l1*l2):
        for j in range(len(A[0])*len(b[0])):
            x, y = i//l2, j//len(b[0])
            res = MultEscMtx(A[x][y],B)
            x1, y1 = i%l2, j%len(b[0])
            m[i][j] = res[x1][y1]
    return m

