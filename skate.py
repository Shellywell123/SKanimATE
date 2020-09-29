from board import PyBoard
import matplotlib
matplotlib.use('TkAgg')
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from transforms import PyTransforms
import numpy as np
import random
import os

tf = PyTransforms()
b = PyBoard()

################################################################################
# begining of class
################################################################################

class PySkate():

    def __init__(self):
        """
        class initaliser
        """

       # print('#'*55)
       # print(' PySkate initalised '+self.ss.get_live_time())
      #  print('#'*55)

    ######################################################################################

    def pre_trick(self):
        """
        load in components before tranformations happen
        """
        fig = plt.figure(0,figsize=[8,8])
        ax = fig.add_subplot(111,projection='3d')
      #  fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        return ax

    ######################################################################################

    def post_trick(self,ax,board=None,wheels=None,trucks=None):
        """
        plot results of transformaition
        """
        max_lim = 17
        min_lim = -max_lim

        if wheels:
            for wheel in wheels:
                x = wheel['x']
                y = wheel['y']
                z = wheel['z']
                ax.plot_surface(x,y,z,zorder=1,alpha=1,color='yellow')

        if trucks:
            for trucks_part in trucks:
                x = trucks_part['x']
                y = trucks_part['y']
                z = trucks_part['z']
                ax.plot_surface(x,y,z,zorder=2,alpha=1,color='blue')

        if board:
            for board_part in board:
                x = board_part['x']
                y = board_part['y']
                z = board_part['z']
                ax.plot_surface(x,y,z,zorder=3,alpha=1,color='r')
        
        ax.auto_scale_xyz([min_lim, max_lim],
                    [min_lim, max_lim], 
                    [min_lim, max_lim])   

    ######################################################################################

    def customflip(self,name,dtheta_x,dtheta_y,dtheta_z):
        """
        """
        ax    = self.pre_trick()
        #ax.set_title(str(0)+' '+str(0)+' '+str(dtheta_z))

        #####################
        ax.set_title(name,fontsize=40)
        board_  = b.use_test_board()
        board = []

        for board_part in board_:
            board_x = board_part['x']
            board_y = board_part['y']
            board_z = board_part['z']
            Bx,By,Bz = tf.z_clockwise(board_x,board_y,board_z,dtheta_z)
            Bx,By,Bz = tf.y_clockwise(Bx,By,Bz,dtheta_y)
            Bx,By,Bz = tf.x_clockwise(Bx,By,Bz,dtheta_x)

            board_part = {'x':Bx,'y':By,'z':Bz}
            board.append(board_part)

        trucks_ = b.use_test_trucks()
        trucks = []

        for trucks_part in trucks_:
            truck_x = trucks_part['x']
            truck_y = trucks_part['y']
            truck_z = trucks_part['z']
            Tx,Ty,Tz = tf.z_clockwise(truck_x,truck_y,truck_z,dtheta_z)
            Tx,Ty,Tz = tf.y_clockwise(Tx,Ty,Tz,dtheta_y)
            Tx,Ty,Tz = tf.x_clockwise(Tx,Ty,Tz,dtheta_x)
            truck_part = {'x':Tx,'y':Ty,'z':Tz}
            trucks.append(truck_part)

        wheels_ = b.use_test_wheels()
        wheels = []

        for wheel in wheels_:
            wheel_x = wheel['x']
            wheel_y = wheel['y']
            wheel_z = wheel['z']
            Wx,Wy,Wz = tf.z_clockwise(wheel_x,wheel_y,wheel_z,dtheta_z)
            Wx,Wy,Wz = tf.y_clockwise(Wx,Wy,Wz,dtheta_y)
            Wx,Wy,Wz = tf.x_clockwise(Wx,Wy,Wz,dtheta_x)
            wheel = {'x':Wx,'y':Wy,'z':Wz}
            wheels.append(wheel)
            
        #####################
        self.post_trick(ax,board,wheels,trucks)    

    ######################################################################################

    def stationary(self):
        """
        used for board development
        """
        ax    = self.pre_trick()
        #ax.set_title(str(0)+' '+str(0)+' '+str(0))
        ax.set_title('stationary',fontsize=40)
        board = b.use_test_board()
        wheels = b.use_test_wheels()
        trucks = b.use_test_trucks()
        self.post_trick(ax,board,wheels,trucks)
        plt.show()

################################################################################
# End of class
################################################################################
