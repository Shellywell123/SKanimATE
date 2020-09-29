

import numpy as np

################################################################################
# begining of class
################################################################################

class PyBoard:

    def __init__(self):
        """
        class initaliser
        """
        # deck dimensions
        self.board_width            = 8
        self.board_mid_length       = 22
        self.board_nose_tail_length = 5

        # truck dimensions
        self.truck_width    = 6
        self.truck_position = 18 #/board_length(32)
        self.axel_radius    = 0.2
        self.truck_height   = 1

        # wheel dimensions
        self.wheel_radius = 1
        self.wheel_width  = 2

    ######################################################################################

    def use_test_board(self):
        """
        deck development
        """

        board = []

        r = int(self.board_width  /2)

        u = np.linspace(0  , np.pi, 15)
        r = np.linspace(0, r   ,2)

        u_inds = np.linspace(0, 15 - 1, 15).round().astype(int)
        r_inds = np.linspace(0, 2 - 1, 15).round().astype(int)

        u = u[u_inds]   
        r = r[r_inds]

        x = np.outer(r, np.cos(u))
        y = np.outer(r, np.sin(u)) + self.board_mid_length/2

        z =  y*0.5 - self.board_mid_length/4. +1
        z = z.reshape(x.shape)


        boardpart = {'x':x,'y':y,'z':z}
        board.append(boardpart)

        ##################

        x = np.arange(-self.board_width  /2,(self.board_width  +1)/2,2)
        y = np.arange(-self.board_mid_length/2,(self.board_mid_length+1)/2,1)

        x,y = np.meshgrid(x,y)

        z =  np.ones(x.shape)

        boardpart = {'x':x,'y':y,'z':z}
        board.append(boardpart)

        ####################

        r = int(self.board_width  /2)

        u = np.linspace(0  , -np.pi, 15)
        r = np.linspace(0, r   ,2)

        u_inds = np.linspace(0, 15 - 1, 15).round().astype(int)
        r_inds = np.linspace(0, 2 - 1, 15).round().astype(int)

        u = u[u_inds]   
        r = r[r_inds]

        x = np.outer(r, np.cos(u))
        y = np.outer(r, np.sin(u)) - self.board_mid_length/2

        z =  -y*0.5-self.board_mid_length/4 +1
        z = z.reshape(x.shape)

        boardpart = {'x':x,'y':y,'z':z}
        board.append(boardpart)

        ####################

        return board

    ######################################################################################

    def use_test_wheels(self):
        """
        wheels development
        """

        wheels = []
        i = 1
        for center_x in [-self.truck_width/2,self.truck_width/2]:
            for center_y in [-self.truck_position/2,self.truck_position/2]:

                x = np.linspace(-self.wheel_width/2, self.wheel_width/2, 50) + center_x
                theta = np.linspace(0, 2*np.pi, 50)
                theta_grid, x_grid=np.meshgrid(theta, x)
                z_grid = self.wheel_radius*np.cos(theta_grid) - self.truck_height
                y_grid = self.wheel_radius*np.sin(theta_grid) + center_y

                wheel = {'x':x_grid,'y':y_grid,'z':z_grid}
                wheels.append(wheel)

        return wheels

    ######################################################################################

    def use_test_trucks(self):
        """
        trucks development
        """

        trucks = []
        i = 1
        for center_y in [-self.truck_position/2,self.truck_position/2]:

	        x = np.linspace(-self.truck_width/2, self.truck_width/2, 50) 
	        theta = np.linspace(0, 2*np.pi, 50)
	        theta_grid, x_grid=np.meshgrid(theta, x)
	        z_grid = self.axel_radius*np.cos(theta_grid) - self.truck_height
	        y_grid = self.axel_radius*np.sin(theta_grid) + center_y

	        truck_axel = {'x':x_grid,'y':y_grid,'z':z_grid}
	        trucks.append(truck_axel)

        return trucks

################################################################################
# End of class
################################################################################
