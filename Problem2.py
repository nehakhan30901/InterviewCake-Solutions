'''Problem2.py
Purpose:You have a list of integers, and for each index you want to find the product of every integer 
		except the integer at that index
Author: Neha Khan
Copyright 2017 Neha Khan
Web site: https://Neha.Khan30901.github.io
'''


import numpy
import unittest

# lesson learned 
# If you have specific exception in mind, always create a specific except block for that solution and then for generic put EXCEPTION
def getProductList(inputList):

	try:
		deserter = inputList.index(0)
		return [0]*len(inputList)

	except ValueError:
		listProduct = numpy.prod(inputList)
		productList = []
		for index, element in enumerate(inputList):
			productList.append(listProduct/element)
		return productList

	except Exception:
		print 'some exception occured'


class testcases(unittest.TestCase):

	#@unittest.skip('skipping')
	def test_getProductList_WithZero(self):
		self.assertEqual(getProductList([1,2,3,0,5]),[0,0,0,0,0])

	#@unittest.skip('skipping')
	def test_getProductList_EmptyList(self):
		self.assertEqual(getProductList([]),[])

	#@unittest.skip('skipping')
	def test_getProductList_WithNegtives(self):
		self.assertEqual(getProductList([1,-2,3,6,5]),[-180, 90, -60, -30, -36])

	#@unittest.skip('skipping')
	def test_getProductList_WithTwoNegatives(self):
		self.assertEqual(getProductList([1,2,-3,-56,5]),[1680, 840, -560, -30, 336])

	#@unittest.skip('skipping')
	def test_getProductList_WithTwoValues(self):
		self.assertEqual(getProductList([101, -2]),[-2, 101])

	#@unittest.skip('skipping')
	def test_getProductList_WithSingleValue(self):
		self.assertEqual(getProductList([44]),[1])

if __name__ == '__main__':
	unittest.main()







