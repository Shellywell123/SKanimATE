
import matplotlib
matplotlib.use('TkAgg')
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import random
import os

from SKanimATE.board import PyBoard
from SKanimATE.transforms import PyTransforms

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
        # fig.subplots_adjust(left=0.0, right=1, bottom=0, top=1)
        ax = fig.gca(projection='3d',azim=20,elev=10)
        # ax.set_box_aspect(aspect = ((1,1,0.25)))
        # fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        # ax.set_xlabel('x')
        # ax.set_ylabel('y')
        # ax.set_zlabel('z')

        # ax.set_facecolor('white')
        # ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
        # ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
        # ax.w_zaxis.set_pane_color((0.4, 0.4, 0.4, 1.0))
        # ax.pbaspect = [1,1,0.25]

        # ax.set_xlim(-15,15)
        # ax.set_ylim(0,200)
        # ax.set_zlim(0,30)
        ax.set_axis_off()
        #plt.tight_layout()

        return ax

    ######################################################################################

    def post_trick(self,ax,board=None,wheels=None,trucks=None,bolts=None):
        """
        plot results of transformaition
        """
        max_lim = 15
        min_lim = -max_lim

        if board:
            for board_part in board:
                x = board_part['x']
                y = board_part['y']
                z = board_part['z']
                ax.plot_surface(x,y,z,zorder=3,alpha=1,color='burlywood') 

        if bolts:
            for bolt in bolts:
                x = bolt['x']
                y = bolt['y']
                z = bolt['z']
                ax.scatter(x,y,z+5,zorder=1,alpha=1,color='blue')                

        if wheels:
            for wheel in wheels:
                x = wheel['x']
                y = wheel['y']
                z = wheel['z']
                ax.plot_surface(x,y,z,zorder=1,alpha=1,color='red')

        if trucks:
            for trucks_part in trucks:
                x = trucks_part['x']
                y = trucks_part['y']
                z = trucks_part['z']
                ax.plot_surface(x,y,z,zorder=2,alpha=1,color='lightsteelblue')

            
             #   ax.plot_surface(x,y,z+1,zorder=3,alpha=0.5,color='black')


        ax.auto_scale_xyz([min_lim, max_lim],
                    [min_lim, max_lim], 
                    [0, 2*max_lim])   

    ######################################################################################

    def customflip(self,name,dtheta_x,dtheta_y,dtheta_z,theta_h,theta_r,n):
        """
        heavy duty function for computing a boards orientation
        """
        ax    = self.pre_trick()
        #ax.set_title(str(0)+' '+str(0)+' '+str(dtheta_z))

        #####################
        ax.set_title(name,fontsize=30,color='r',backgroundcolor='dimgray')
        board_  = b.use_test_board()
        board = []

        for board_part in board_:
            Bx = board_part['x']
            By = board_part['y']
            Bz = board_part['z']
            if dtheta_y != 0:
                Bx,By,Bz = tf.y_clockwise(Bx,By,Bz,dtheta_y)
            if dtheta_z != 0:
                Bx,By,Bz = tf.z_clockwise(Bx,By,Bz,dtheta_z)
            if dtheta_x != 0:
                Bx,By,Bz = tf.x_clockwise(Bx,By,Bz,dtheta_x)
            if theta_h != 0:
                Bx,By,Bz = tf.ollie_motion(Bx,By,Bz,theta_h,theta_r)

            # make trick no stationary
            Bx,By,Bz = tf.cruise_motion(Bx,By,Bz,n)

            board_part = {'x':Bx,'y':By,'z':Bz}
            board.append(board_part)

        # bolts_ = b.use_test_bolts()
        # bolts = []

        # for bolt in bolts_:
        #     bx = bolt['x']
        #     by = bolt['y']
        #     bz = bolt['z']
        #     if dtheta_y != 0:
        #         bx,by,bz = tf.y_clockwise(bx,by,bz,dtheta_y)
        #     if dtheta_z != 0:
        #         bx,by,bz = tf.z_clockwise(bx,by,bz,dtheta_z)
        #     if dtheta_x != 0:
        #         bx,by,bz = tf.x_clockwise(bx,by,bz,dtheta_x)
        #     if theta_h != 0:
        #         bx,by,bz = tf.ollie_motion(bx,by,bz,theta_h,theta_r)
        #     bolt = {'x':bx,'y':by,'z':bz}
        #     bolts.append(bolt)

        trucks_ = b.use_test_trucks()
        trucks = []

        for trucks_part in trucks_:
            Tx = trucks_part['x']
            Ty = trucks_part['y']
            Tz = trucks_part['z']
            if dtheta_y != 0:
                Tx,Ty,Tz = tf.y_clockwise(Tx,Ty,Tz,dtheta_y)
            if dtheta_z != 0:
                Tx,Ty,Tz = tf.z_clockwise(Tx,Ty,Tz,dtheta_z)
            if dtheta_x != 0:
                Tx,Ty,Tz = tf.x_clockwise(Tx,Ty,Tz,dtheta_x)
            if theta_h != 0:
                Tx,Ty,Tz = tf.ollie_motion(Tx,Ty,Tz,theta_h,theta_r)

            # make trick no stationary
            Tx,Ty,Tz = tf.cruise_motion(Tx,Ty,Tz,n)

            truck_part = {'x':Tx,'y':Ty,'z':Tz}
            trucks.append(truck_part)



        wheels_ = b.use_test_wheels()
        wheels = []

        for wheel in wheels_:
            Wx = wheel['x']
            Wy = wheel['y']
            Wz = wheel['z']
            if dtheta_y != 0:
                Wx,Wy,Wz = tf.y_clockwise(Wx,Wy,Wz,dtheta_y)
            if dtheta_z != 0:
                Wx,Wy,Wz = tf.z_clockwise(Wx,Wy,Wz,dtheta_z)
            if dtheta_x != 0:
                Wx,Wy,Wz = tf.x_clockwise(Wx,Wy,Wz,dtheta_x)
            if theta_h != 0:
                Wx,Wy,Wz = tf.ollie_motion(Wx,Wy,Wz,theta_h,theta_r)

            # make trick no stationary
            Wx,Wy,Wz = tf.cruise_motion(Wx,Wy,Wz,n)

            wheel = {'x':Wx,'y':Wy,'z':Wz}
            wheels.append(wheel)
            
        #####################

        for y in range(-50,60):
            ax.plot([-15,15],[y-n,y-n],[0,0], linewidth=10,c='dimgray') 
            if y%2==0:
                col='darkgray'
            else:
                col='k'
            ax.plot([-15,15],[y-n+0.5,y-n+0.5],[0,0], linewidth=10,c=col) 

        #####################

        self.post_trick(ax,board,wheels,trucks)    

    ######################################################################################

    def customnollieflip(self,name,dtheta_x,dtheta_y,dtheta_z,theta_h,theta_r,n):
        """
        heavy duty function for computing a boards orientation
        """
        ax    = self.pre_trick()
        #ax.set_title(str(0)+' '+str(0)+' '+str(dtheta_z))

        #####################
        ax.set_title(name,fontsize=30,color='r',backgroundcolor='dimgray')
        board_  = b.use_test_board()
        board = []

        for board_part in board_:
            Bx = board_part['x']
            By = board_part['y']
            Bz = board_part['z']
            if dtheta_y != 0:
                Bx,By,Bz = tf.y_clockwise(Bx,By,Bz,dtheta_y)
            if dtheta_z != 0:
                Bx,By,Bz = tf.z_clockwise(Bx,By,Bz,dtheta_z)
            if dtheta_x != 0:
                Bx,By,Bz = tf.x_clockwise(Bx,By,Bz,dtheta_x)
            if theta_h != 0:
                Bx,By,Bz = tf.nollie_motion(Bx,By,Bz,theta_h,theta_r)

        # make trick no stationary
            Bx,By,Bz = tf.cruise_motion(Bx,By,Bz,n)

            board_part = {'x':Bx,'y':By,'z':Bz}
            board.append(board_part)

        # bolts_ = b.use_test_bolts()
        # bolts = []

        # for bolt in bolts_:
        #     bx = bolt['x']
        #     by = bolt['y']
        #     bz = bolt['z']
        #     if dtheta_y != 0:
        #         bx,by,bz = tf.y_clockwise(bx,by,bz,dtheta_y)
        #     if dtheta_z != 0:
        #         bx,by,bz = tf.z_clockwise(bx,by,bz,dtheta_z)
        #     if dtheta_x != 0:
        #         bx,by,bz = tf.x_clockwise(bx,by,bz,dtheta_x)
        #     if theta_h != 0:
        #         bx,by,bz = tf.ollie_motion(bx,by,bz,theta_h,theta_r)
        #     bolt = {'x':bx,'y':by,'z':bz}
        #     bolts.append(bolt)

        trucks_ = b.use_test_trucks()
        trucks = []

        for trucks_part in trucks_:
            Tx = trucks_part['x']
            Ty = trucks_part['y']
            Tz = trucks_part['z']
            if dtheta_y != 0:
                Tx,Ty,Tz = tf.y_clockwise(Tx,Ty,Tz,dtheta_y)
            if dtheta_z != 0:
                Tx,Ty,Tz = tf.z_clockwise(Tx,Ty,Tz,dtheta_z)
            if dtheta_x != 0:
                Tx,Ty,Tz = tf.x_clockwise(Tx,Ty,Tz,dtheta_x)
            if theta_h != 0:
                Tx,Ty,Tz = tf.nollie_motion(Tx,Ty,Tz,theta_h,theta_r)

        # make trick no stationary
            Tx,Ty,Tz = tf.cruise_motion(Tx,Ty,Tz,n)

            truck_part = {'x':Tx,'y':Ty,'z':Tz}
            trucks.append(truck_part)

        wheels_ = b.use_test_wheels()
        wheels = []

        for wheel in wheels_:
            Wx = wheel['x']
            Wy = wheel['y']
            Wz = wheel['z']
            if dtheta_y != 0:
                Wx,Wy,Wz = tf.y_clockwise(Wx,Wy,Wz,dtheta_y)
            if dtheta_z != 0:
                Wx,Wy,Wz = tf.z_clockwise(Wx,Wy,Wz,dtheta_z)
            if dtheta_x != 0:
                Wx,Wy,Wz = tf.x_clockwise(Wx,Wy,Wz,dtheta_x)
            if theta_h != 0:
                Wx,Wy,Wz = tf.nollie_motion(Wx,Wy,Wz,theta_h,theta_r)

        # make trick no stationary
            Wx,Wy,Wz = tf.cruise_motion(Wx,Wy,Wz,n)
            
            wheel = {'x':Wx,'y':Wy,'z':Wz}
            wheels.append(wheel)

            
        #####################

        for y in range(-50,60):
            ax.plot([-15,15],[y-n,y-n],[0,0], linewidth=10,c='dimgray') 
            if y%2==0:
                col='darkgray'
            else:
                col='k'
            ax.plot([-15,15],[y-n+0.5,y-n+0.5],[0,0], linewidth=10,c=col) 

        #####################

        self.post_trick(ax,board,wheels,trucks)    

      ######################################################################################

    def no_trick(self):
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
