import unittest 
import SegRestantes as seg

class TestCalcSeg(unittest.TestCase):    
	
	def setUp(self):        
		self.calc = seg.SegRestantes()
	
	def test_calc_method_returns_correct_result(self): 
		self.assertEqual(10, self.calc.calcSeg(50))
		
if __name__ == '__main__':   
	
	unittest.main()
