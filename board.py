

import numpy as np

################################################################################
# begining of class
################################################################################

class PyBoard:

	def use_test_board(self):
		"""
		"""

		board_width  = 8
		board_length = 32

		x = np.arange(-board_width/2,board_width/2,0.5)
		y = np.arange(-board_length/2,board_length/2,0.5)

		x,y = np.meshgrid(x,y)

		z = np.zeros(x.shape)

		return x,y,z

################################################################################
# End of class
################################################################################
