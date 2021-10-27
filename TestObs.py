import unittest
import Estados_cuanticos as qs
import Libcplx as lc

class TestRetos(unittest.TestCase):
    def test_reto1(self):
        ket1=[[(1,0)], [(0,-1)]]
        ket2 = [[(0, 1)], [(1, 0)]]
        Ket = [[(-3, -1)], [(0, -2)], [(0, 1)], [(2, 0)]]
        self.assertEqual(qs.probParticleInLine(2, Ket), 0.05263157894736841)
        self.assertEqual(lc.cplxtruncar.truncar(qs.probTransition(ket1, ket2), 2),(0.0, -1.0))
        self.assertEqual(qs.probabilidad(lc.cplxtruncar(qs.probTransition(ket1, ket2), 2)), 1.0)

    def test_reto2(self):
        o = [[(1, 0), (0, -1)], [(0, 1),(2, 0)]]
        o2 = [[(0, 0), (0, -1)], [(0, 1),(0, 0)]]
        ket = [[((2**0.5)/2, 0)], [(0, (2**0.5)/2)]]
        ket2 = [[(1/(2**0.5), 0)], [(0, 1/(2**0.5))]]
        self.assertEqual(qs.expVal(o, ket),((2.5000000000000004, 0.0), (0.25, 0.0)))
        self.assertEqual(lc.cplxtruncar(qs.expVal(o2, ket2)[0], 2),(1.0, 0.0))
        self.assertEqual(lc.cplxtruncar(qs.expVal(o2, ket2)[1], 2),(0.0, 0.0))

    def test_reto3(self):
        o = [[-1,-1j],[1j,1]]
        vecS = [[(1/2,0)],[(1/2,0)]]
        self.assertEqual(qs.eigenValuesObs(o),([(-1.414213562373095, 0.0), (1.4142135623730951, 0.0)], [[(0.9238795325112867, 0.0), (0.0, -0.3826834323650897)], [(0.0, -0.3826834323650898), (0.9238795325112867, 0.0)]]))
        self.assertEqual(qs.eigenProb(vecS, qs.eigenValuesObs(o)[1]), [(0.25, 0), (0.25, 0)])

    def test_reto4(self):
        n=[[(0,0),(1/(2**0.5),0),(1/(2**0.5),0),(0,0)],[(0,1/(2**0.5)),(0,0),(0,0),(1/(2**0.5),0)],[(1/(2**0.5),0),(0,0),(0,0),(0,1/(2**0.5))],[(0,0),(1/(2**0.5),0),(-1/(2**0.5),0),(0,0)]]
        q0 = [[(1,0)],[(0,0)],[(0,0)],[(0,0)]]
        self.assertEqual(qs.dinamic(3, n, q0),[(-0.49999999999999956, -0.49999999999999956), (0, 0), (0, 0), (0, 0)])

if __name__=='__main__':
    unittest.main()
