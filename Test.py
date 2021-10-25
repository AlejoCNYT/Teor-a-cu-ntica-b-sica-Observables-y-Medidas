import Estados_cuanticos as qs
import math
import unittest

class TestCplxOperations(unittest.TestCase):

    def test_probParticleInLine(self):
        PPIL = qs.probParticleInLine(3, [(-3,-1),(0,-2),(0,1),(2,0)])
        self.assertEqual(PPIL, 1/19)

    def test_probTransition(self):
        pt = qs.probTransition([(1,0),(0,-1)],[(0,1),(1,0)])
        self.assertEqual(pt, (0,-2))

    

if __name__ == '__main__':
    unittest.main()
