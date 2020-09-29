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

    def pre_trick(self,x_theta,y_theta,z_theta):
        """
        """
        fig = plt.figure(0,figsize=[8,8])
        ax = fig.add_subplot(111,projection='3d')
      #  fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        ax.set_xlabel('x')
        ax.set_ylabel('x')
        ax.set_zlabel('z')
        ax.set_title(str(x_theta)+' '+str(y_theta)+' '+str(z_theta))
        return ax

    def post_trick(self,ax,x,y,z):
        """
        """
        max_lim = 20
        min_lim = -max_lim

        ax.plot_surface(x,y,z)
        ax.auto_scale_xyz([min_lim, max_lim],
                    [min_lim, max_lim], 
                    [min_lim, max_lim])

    def kickflip(self,dtheta_y):
        """
        anticlock
        """
        ax    = self.pre_trick(0,dtheta_y,0)
        x,y,z = b.use_test_board()
        x,y,z = tf.y_anticlockwise(x,y,z,dtheta_y)
        self.post_trick(ax,x,y,z)

    def heelflip(self,dtheta_y):
        """
        anticlock
        """
        ax    = self.pre_trick(0,dtheta_y,0)
        x,y,z = b.use_test_board()
        x,y,z = tf.y_clockwise(x,y,z,dtheta_y)
        self.post_trick(ax,x,y,z)

    def bs_360_shuv(self,dtheta_z):
        """
        """
        ax    = self.pre_trick(0,0,dtheta_z)
        x,y,z = b.use_test_board()
        x,y,z = tf.z_clockwise(x,y,z,dtheta_z)
        self.post_trick(ax,x,y,z)	

    def fs_360_shuv(self,dtheta_z):
        """
        """
        ax    = self.pre_trick(0,0,dtheta_z)
        x,y,z = b.use_test_board()
        x,y,z = tf.z_anticlockwise(x,y,z,dtheta_z)
        self.post_trick(ax,x,y,z)	

    def front_foot_impossible(self,dtheta_x):
        """
        """
        ax    = self.pre_trick(dtheta_x,0,0)
        x,y,z = b.use_test_board()
        x,y,z = tf.x_anticlockwise(x,y,z,dtheta_x)
        self.post_trick(ax,x,y,z)	

    def back_foot_impossible(self,dtheta_x):
        """
        """
        ax    = self.pre_trick(dtheta_x,0,0)
        x,y,z = b.use_test_board()
        x,y,z = tf.x_clockwise(x,y,z,dtheta_x)
        self.post_trick(ax,x,y,z)	

    def stationary(self):
        """
        """
        ax    = self.pre_trick(0,0,0)
        x,y,z = b.use_test_board()
        self.post_trick(ax,x,y,z)
        plt.show()

################################################################################
# End of class
################################################################################
