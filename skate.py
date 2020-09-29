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

    def post_trick(self,ax,board,wheels=None):
        """
        plot results of transformaition
        """
        max_lim = 20
        min_lim = -max_lim


        if board:
            x = board['x']
            y = board['y']
            z = board['z']
            ax.plot_surface(x,y,z)
        
        if wheels:
            for wheel in wheels:
                x = wheel['x']
                y = wheel['y']
                z = wheel['z']
                ax.plot_surface(x,y,z)

        ax.auto_scale_xyz([min_lim, max_lim],
                    [min_lim, max_lim], 
                    [min_lim, max_lim])

    def kickflip(self,dtheta_y):
        """
        anticlock
        """
        ax    = self.pre_trick()
        #ax.set_title(str(0)+' '+str(dtheta_y)+' '+str(0))

        #####################
        ax.set_title('Kickflip',fontsize=40)
        board  = b.use_test_board()

        board_x = board['x']
        board_y = board['y']
        board_z = board['z']
        Bx,By,Bz = tf.y_anticlockwise(board_x,board_y,board_z,dtheta_y)
        board = {'x':Bx,'y':By,'z':Bz}

        wheels_ = b.use_test_wheels()
        wheels = []

        for wheel in wheels_:
            wheel_x = wheel['x']
            wheel_y = wheel['y']
            wheel_z = wheel['z']
            Wx,Wy,Wz = tf.y_anticlockwise(wheel_x,wheel_y,wheel_z,dtheta_y)
            wheel = {'x':Wx,'y':Wy,'z':Wz}
            wheels.append(wheel)

        #####################
        
        self.post_trick(ax,board,wheels)

    def heelflip(self,dtheta_y):
        """
        anticlock
        """
        ax    = self.pre_trick()
        #ax.set_title(str(0)+' '+str(dtheta_y)+' '+str(0))

        #####################
        ax.set_title('Heelflip',fontsize=40)
        board  = b.use_test_board()

        board_x = board['x']
        board_y = board['y']
        board_z = board['z']
        Bx,By,Bz = tf.y_clockwise(board_x,board_y,board_z,dtheta_y)
        board = {'x':Bx,'y':By,'z':Bz}

        wheels_ = b.use_test_wheels()
        wheels = []

        for wheel in wheels_:
            wheel_x = wheel['x']
            wheel_y = wheel['y']
            wheel_z = wheel['z']
            Wx,Wy,Wz = tf.y_clockwise(wheel_x,wheel_y,wheel_z,dtheta_y)
            wheel = {'x':Wx,'y':Wy,'z':Wz}
            wheels.append(wheel)
            
        #####################

        self.post_trick(ax,board,wheels)

    def bs_360_shuv(self,dtheta_z):
        """
        """
        ax    = self.pre_trick()
        #ax.set_title(str(0)+' '+str(0)+' '+str(dtheta_z))

        #####################
        ax.set_title('BS 360 Shuvit',fontsize=40)
        board  = b.use_test_board()

        board_x = board['x']
        board_y = board['y']
        board_z = board['z']
        Bx,By,Bz = tf.z_clockwise(board_x,board_y,board_z,dtheta_z)
        board = {'x':Bx,'y':By,'z':Bz}

        wheels_ = b.use_test_wheels()
        wheels = []

        for wheel in wheels_:
            wheel_x = wheel['x']
            wheel_y = wheel['y']
            wheel_z = wheel['z']
            Wx,Wy,Wz = tf.z_clockwise(wheel_x,wheel_y,wheel_z,dtheta_z)
            wheel = {'x':Wx,'y':Wy,'z':Wz}
            wheels.append(wheel)
            
        #####################
        self.post_trick(ax,board,wheels)	

    def fs_360_shuv(self,dtheta_z):
        """
        """
        ax    = self.pre_trick()
        #ax.set_title(str(0)+' '+str(0)+' '+str(dtheta_z))

        #####################
        ax.set_title('FS 360 Shuvit',fontsize=40)
        board  = b.use_test_board()

        board_x = board['x']
        board_y = board['y']
        board_z = board['z']
        Bx,By,Bz = tf.z_anticlockwise(board_x,board_y,board_z,dtheta_z)
        board = {'x':Bx,'y':By,'z':Bz}

        wheels_ = b.use_test_wheels()
        wheels = []

        for wheel in wheels_:
            wheel_x = wheel['x']
            wheel_y = wheel['y']
            wheel_z = wheel['z']
            Wx,Wy,Wz = tf.z_anticlockwise(wheel_x,wheel_y,wheel_z,dtheta_z)
            wheel = {'x':Wx,'y':Wy,'z':Wz}
            wheels.append(wheel)

        #####################
        
        self.post_trick(ax,board,wheels)

    def front_foot_impossible(self,dtheta_x):
        """
        """
        ax    = self.pre_trick()
        #ax.set_title(str(dtheta_x)+' '+str(0)+' '+str(0))
    
        #####################
        ax.set_title('Front Foot Impossible',fontsize=40)
        board  = b.use_test_board()

        board_x = board['x']
        board_y = board['y']
        board_z = board['z']
        Bx,By,Bz = tf.x_anticlockwise(board_x,board_y,board_z,dtheta_x)
        board = {'x':Bx,'y':By,'z':Bz}

        wheels_ = b.use_test_wheels()
        wheels = []

        for wheel in wheels_:
            wheel_x = wheel['x']
            wheel_y = wheel['y']
            wheel_z = wheel['z']
            Wx,Wy,Wz = tf.x_anticlockwise(wheel_x,wheel_y,wheel_z,dtheta_x)
            wheel = {'x':Wx,'y':Wy,'z':Wz}
            wheels.append(wheel)

        #####################
        
        self.post_trick(ax,board,wheels)

    def back_foot_impossible(self,dtheta_x):
        """
        """
        ax    = self.pre_trick()
        #ax.set_title(str(dtheta_x)+' '+str(0)+' '+str(0))

        #####################
        ax.set_title('Back Foot Impossible',fontsize=40)
        board  = b.use_test_board()

        board_x = board['x']
        board_y = board['y']
        board_z = board['z']
        Bx,By,Bz = tf.x_clockwise(board_x,board_y,board_z,dtheta_x)
        board = {'x':Bx,'y':By,'z':Bz}

        wheels_ = b.use_test_wheels()
        wheels = []

        for wheel in wheels_:
            wheel_x = wheel['x']
            wheel_y = wheel['y']
            wheel_z = wheel['z']
            Wx,Wy,Wz = tf.x_clockwise(wheel_x,wheel_y,wheel_z,dtheta_x)
            wheel = {'x':Wx,'y':Wy,'z':Wz}
            wheels.append(wheel)
            
        #####################
        self.post_trick(ax,board,wheels)    

    # def treflip(self,dtheta_y,dtheta_z):
    #     """
    #     """
    #     ax    = self.pre_trick()
    #     #ax.set_title(str(0)+' '+str(0)+' '+str(dtheta_z))

    #     #####################
    #     ax.set_title('Treflip')
    #     board  = b.use_test_board()

    #     board_x = board['x']
    #     board_y = board['y']
    #     board_z = board['z']
    #     Bx,By,Bz = tf.z_clockwise(board_x,board_y,board_z,dtheta_z)
    #     Bx,By,Bz = tf.y_clockwise(Bx,By,Bz,dtheta_y)

    #     board = {'x':Bx,'y':By,'z':Bz}

    #     wheels_ = b.use_test_wheels()
    #     wheels = []

    #     for wheel in wheels_:
    #         wheel_x = wheel['x']
    #         wheel_y = wheel['y']
    #         wheel_z = wheel['z']
    #         Wx,Wy,Wz = tf.z_clockwise(wheel_x,wheel_y,wheel_z,dtheta_z)
    #         Wx,Wy,Wz = tf.y_clockwise(Wx,Wy,Wz,dtheta_y)
    #         wheel = {'x':Wx,'y':Wy,'z':Wz}
    #         wheels.append(wheel)
            
    #     #####################
    #     self.post_trick(ax,board,wheels)    

    # def lazerflip(self,dtheta_y,dtheta_z):
    #     """
    #     """
    #     ax    = self.pre_trick()
    #     #ax.set_title(str(0)+' '+str(0)+' '+str(dtheta_z))

    #     #####################
    #     ax.set_title('Treflip')
    #     board  = b.use_test_board()

    #     board_x = board['x']
    #     board_y = board['y']
    #     board_z = board['z']
    #     Bx,By,Bz = tf.z_clockwise(board_x,board_y,board_z,dtheta_z)
    #     Bx,By,Bz = tf.y_clockwise(Bx,By,Bz,dtheta_y)

    #     board = {'x':Bx,'y':By,'z':Bz}

    #     wheels_ = b.use_test_wheels()
    #     wheels = []

    #     for wheel in wheels_:
    #         wheel_x = wheel['x']
    #         wheel_y = wheel['y']
    #         wheel_z = wheel['z']
    #         Wx,Wy,Wz = tf.z_clockwise(wheel_x,wheel_y,wheel_z,dtheta_z)
    #         Wx,Wy,Wz = tf.y_clockwise(Wx,Wy,Wz,dtheta_y)
    #         wheel = {'x':Wx,'y':Wy,'z':Wz}
    #         wheels.append(wheel)
            
    #     #####################
    #     self.post_trick(ax,board,wheels)    

    def customflip(self,name,dtheta_x,dtheta_y,dtheta_z):
        """
        """
        ax    = self.pre_trick()
        #ax.set_title(str(0)+' '+str(0)+' '+str(dtheta_z))

        #####################
        ax.set_title(name,fontsize=40)
        board  = b.use_test_board()

        board_x = board['x']
        board_y = board['y']
        board_z = board['z']
        Bx,By,Bz = tf.z_clockwise(board_x,board_y,board_z,dtheta_z)
        Bx,By,Bz = tf.y_clockwise(Bx,By,Bz,dtheta_y)
        Bx,By,Bz = tf.x_clockwise(Bx,By,Bz,dtheta_x)

        board = {'x':Bx,'y':By,'z':Bz}

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
        self.post_trick(ax,board,wheels)    

    def stationary(self):
        """
        used for board development
        """
        ax    = self.pre_trick()
        #ax.set_title(str(0)+' '+str(0)+' '+str(0))
        ax.set_title('stationary',fontsize=40)
        board = b.use_test_board()
        wheels = b.use_test_wheels()
        self.post_trick(ax,board,wheels)
        plt.show()

################################################################################
# End of class
################################################################################
