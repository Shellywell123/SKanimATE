

import numpy as np

################################################################################
# begining of class
################################################################################

class PyBoard:

    def __init__(self):
        """
        class initaliser
        """

       # print('#'*55)
       # print(' PyBoard initalised '+self.ss.get_live_time())
      #  print('#'*55)

    ######################################################################################

    def use_test_board(self):
        """
        """

        board_width  = 8
        board_mid_length = 22
        board_nose_tail_length = 5

        board = []

        x = np.arange(-board_width/2,board_width/2,0.5)
        y = np.arange(0,board_nose_tail_length,1) + board_mid_length/2 -1

        x,y = np.meshgrid(x,y)

        z =  y*0.5 - board_mid_length/4 + 1.5
        z = z.reshape(x.shape)

        boardpart = {'x':x,'y':y,'z':z}
        board.append(boardpart)

        ##################

        x = np.arange(-board_width/2,board_width/2,0.5)
        y = np.arange(-board_mid_length/2,board_mid_length/2,1)

        x,y = np.meshgrid(x,y)

        z =  np.ones(x.shape)

        boardpart = {'x':x,'y':y,'z':z}
        board.append(boardpart)

        ####################

        x = np.arange(-board_width/2,board_width/2,0.5)
        y = np.arange(-board_nose_tail_length,0,0.5)- board_mid_length/2 +0.5

        x,y = np.meshgrid(x,y)

        z =  -y*0.5-board_mid_length/4 +1
        z = z.reshape(x.shape)

        boardpart = {'x':x,'y':y,'z':z}

        board.append(boardpart)
        ####################

        return board

    ######################################################################################

    def use_test_wheels(self):
        """
        """

        wheel_radius = 1
        truck_height = 1
        board_width  = 8

        wheel_width    = 2
        truck_width    = 6
        truck_position = 18 #/board_length

        wheels = []
        i = 1
        for center_x in [-truck_width/2,truck_width/2]:
            for center_y in [-truck_position/2,truck_position/2]:

                x = np.linspace(-wheel_width/2, wheel_width/2, 50) + center_x
                theta = np.linspace(0, 2*np.pi, 50)
                theta_grid, x_grid=np.meshgrid(theta, x)
                z_grid = wheel_radius*np.cos(theta_grid) - truck_height
                y_grid = wheel_radius*np.sin(theta_grid) + center_y

                wheel = {'x':x_grid,'y':y_grid,'z':z_grid}
                wheels.append(wheel)

        return wheels

    ######################################################################################

    def use_test_trucks(self):
        """
        """

        truck_height   = 1
        truck_radius   = 0.2
        wheel_width    = 2
        truck_width    = 6
        truck_position = 18 #/board_length

        trucks = []
        i = 1
        for center_y in [-truck_position/2,truck_position/2]:

	        x = np.linspace(-truck_width/2, truck_width/2, 50) 
	        theta = np.linspace(0, 2*np.pi, 50)
	        theta_grid, x_grid=np.meshgrid(theta, x)
	        z_grid = truck_radius*np.cos(theta_grid) - truck_height
	        y_grid = truck_radius*np.sin(theta_grid) + center_y

	        truck_axel = {'x':x_grid,'y':y_grid,'z':z_grid}
	        trucks.append(truck_axel)

        return trucks

################################################################################
# End of class
################################################################################
