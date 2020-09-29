

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

        board = {'x':x,'y':y,'z':z}

        return board

    def use_test_wheels(self):
        """
        """

        wheel_radius = 1
        truck_height = 1
        board_width  = 8

        wheel_width    = 2
        truck_width    = 4
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





################################################################################
# End of class
################################################################################
