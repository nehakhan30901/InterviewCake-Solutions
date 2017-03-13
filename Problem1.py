'''Problem1.py
Purpose: Write an efficient function that takes an index from yesterday and returns the best profit I could have made from 1
 		 purchase and 1 sale of 1 Apple stock yesterday
Author: Neha Khan
Copyright 2017 Neha Khan
Web site: https://Neha.Khan30901.github.io
'''

import unittest

#good way, greedy way
def makeProfitTheGreedyWay(stockPricesYesterday):

	if len(stockPricesYesterday)<2:
		raise Exception('Need atleast 2 indexes for transaction')

	minPrice = stockPricesYesterday[0]
	profit   = stockPricesYesterday[1] - stockPricesYesterday[0]
	for currentPrice in stockPricesYesterday[1:]:
		potentialProfit = currentPrice - minPrice
		profit = max(profit, potentialProfit)
		minPrice = min(minPrice, currentPrice)
		

	return profit


class TestCases(unittest.TestCase):

	def test_makeProfitTheGreedyWay(self):

		# fluctuating prices.
		self.assertEqual(makeProfitTheGreedyWay([1, 4, 3, 7, 101, 42, 0, 21, 56, 92, 2, 93]), 100)

		# stock going down the whole day
		self.assertEqual(makeProfitTheGreedyWay([10, 9, 6, 5, 4, 3]), -1)

		# stock price stagnant
		self.assertEqual(makeProfitTheGreedyWay([2, 2, 2, 2, 2]),0)

		# erroneous input
		with self.assertRaises(Exception):
			makeProfitTheGreedyWay([10])


if __name__ == '__main__':
	unittest.main()








#test

