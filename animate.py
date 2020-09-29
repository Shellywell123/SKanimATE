from skate import PySkate
import matplotlib.pyplot as plt
import numpy as np
import os

################################################################################
# begining of class
################################################################################

class PyAnimate:

    def __init__(self):
        """
        class initaliser
        """
        self.sb = PySkate()

       # print('#'*55)
       # print(' PyAnimate initalised '+self.ss.get_live_time())
      #  print('#'*55)

    ######################################################################################

    def frames_to_gif(self,gifname):
        """
        converts all images in frames dir to a gif
        """
        import imageio
        images = []
        for filename in os.listdir('Images/frames/'):
            images.append(imageio.imread('Images/frames/'+filename))
        filename = 'Images/gifs/{}.gif'.format(gifname)
        imageio.mimsave(filename, images)
        print('{} made'.format(filename))

    ######################################################################################

    def make_kickflip_gif(self,num_of_frames=50):
        """
        create a gif of the system spinning out radially
        """

        i = 1
        for d_theta in list(np.linspace(0,360,num_of_frames)):

            self.sb.kickflip(d_theta)

            if i <= 9:
                name_i = '0'+str(i)
            else:
                name_i = str(i)

            save_name = 'Images/frames/{}.png'.format(name_i)
            plt.savefig(save_name)
            plt.clf()
            i = i+1
            print('Frame ({}/{}) Saved.'.format(name_i,num_of_frames))

        self.frames_to_gif('kickflip')

    ######################################################################################

    def make_heelflip_gif(self,num_of_frames=50):
        """
        create a gif of the system spinning out radially
        """

        i = 1
        for d_theta in list(np.linspace(0,360,num_of_frames)):

            self.sb.heelflip(d_theta)

            if i <= 9:
                name_i = '0'+str(i)
            else:
                name_i = str(i)

            save_name = 'Images/frames/{}.png'.format(name_i)
            plt.savefig(save_name)
            plt.clf()
            i = i+1
            print('Frame ({}/{}) Saved.'.format(name_i,num_of_frames))

        self.frames_to_gif('heelflip')


    ######################################################################################

    def make_bs_360_shuv_gif(self,num_of_frames=50):
        """
        create a gif of the system spinning out radially
        """

        i = 1
        for d_theta in list(np.linspace(0,360,num_of_frames)):

            self.sb.bs_360_shuv(d_theta)

            if i <= 9:
                name_i = '0'+str(i)
            else:
                name_i = str(i)

            save_name = 'Images/frames/{}.png'.format(name_i)
            plt.savefig(save_name)
            plt.clf()
            i = i+1
            print('Frame ({}/{}) Saved.'.format(name_i,num_of_frames))

        self.frames_to_gif('bs_360_shuv')

    ######################################################################################


    def make_fs_360_shuv_gif(self,num_of_frames=50):
        """
        create a gif of the system spinning out radially
        """

        i = 1
        for d_theta in list(np.linspace(0,360,num_of_frames)):

            self.sb.fs_360_shuv(d_theta)

            if i <= 9:
                name_i = '0'+str(i)
            else:
                name_i = str(i)

            save_name = 'Images/frames/{}.png'.format(name_i)
            plt.savefig(save_name)
            plt.clf()
            i = i+1
            print('Frame ({}/{}) Saved.'.format(name_i,num_of_frames))

        self.frames_to_gif('fs_360_shuv')

    ######################################################################################

    def make_front_foot_impossible_gif(self,num_of_frames=50):
        """
        create a gif of the system spinning out radially
        """

        i = 1
        for d_theta in list(np.linspace(0,360,num_of_frames-1)):

            self.sb.front_foot_impossible(d_theta)

            if i <= 9:
                name_i = '0'+str(i)
            else:
                name_i = str(i)

            save_name = 'Images/frames/{}.png'.format(name_i)
            plt.savefig(save_name)
            plt.clf()
            i = i+1
            print('Frame ({}/{}) Saved.'.format(name_i,num_of_frames))

        self.frames_to_gif('front_foot_impossible')

    ######################################################################################
    
    def make_back_foot_impossible_gif(self,num_of_frames=50):
        """
        create a gif of the system spinning out radially
        """

        i = 1
        for d_theta in list(np.linspace(0,360,num_of_frames-1)):

            self.sb.back_foot_impossible(d_theta)

            if i <= 9:
                name_i = '0'+str(i)
            else:
                name_i = str(i)

            save_name = 'Images/frames/{}.png'.format(name_i)
            plt.savefig(save_name)
            plt.clf()
            i = i+1
            print('Frame ({}/{}) Saved.'.format(name_i,num_of_frames))

        self.frames_to_gif('back_foot_impossible')

    ######################################################################################


    def make_treflip_gif(self,num_of_frames=50):
        """
        create a gif of the system spinning out radially
        """

        i = 1
        d_theta_y = list(np.linspace(360,0,num_of_frames+1))
        d_theta_z = list(np.linspace(0,360,num_of_frames+1))

        for i in range(1,num_of_frames+1):

            self.sb.customflip('Treflip',0,d_theta_y[i],d_theta_z[i])

            if i <= 9:
                name_i = '0'+str(i)
            else:
                name_i = str(i)

            save_name = 'Images/frames/{}.png'.format(name_i)
            plt.savefig(save_name)
            plt.clf()
            i = i+1
            print('Frame ({}/{}) Saved.'.format(name_i,num_of_frames))

        self.frames_to_gif('treflip')

    ######################################################################################


    def make_lazerflip_gif(self,num_of_frames=50):
        """
        create a gif of the system spinning out radially
        """

        i = 1
        d_theta_y = list(np.linspace(0,360,num_of_frames+1))
        d_theta_z = list(np.linspace(0,-360,num_of_frames+1))

        for i in range(1,num_of_frames+1):

            self.sb.customflip('Lazerflip',0,d_theta_y[i],d_theta_z[i])

            if i <= 9:
                name_i = '0'+str(i)
            else:
                name_i = str(i)

            save_name = 'Images/frames/{}.png'.format(name_i)
            plt.savefig(save_name)
            plt.clf()
            i = i+1
            print('Frame ({}/{}) Saved.'.format(name_i,num_of_frames))

        self.frames_to_gif('lazerflip')

    ######################################################################################


    def make_hardflip_gif(self,num_of_frames=50):
        """
        create a gif of the system spinning out radially
        """

        i = 1
        d_theta_y = list(np.linspace(0,360,num_of_frames+1))
        d_theta_z = list(np.linspace(0,-180,num_of_frames+1))

        for i in range(1,num_of_frames+1):

            self.sb.customflip('Hardflip',0,d_theta_y[i],d_theta_z[i])

            if i <= 9:
                name_i = '0'+str(i)
            else:
                name_i = str(i)

            save_name = 'Images/frames/{}.png'.format(name_i)
            plt.savefig(save_name)
            plt.clf()
            i = i+1
            print('Frame ({}/{}) Saved.'.format(name_i,num_of_frames))

        self.frames_to_gif('hardflip')

    ######################################################################################


    def make_varial_kickflip_gif(self,num_of_frames=50):
        """
        create a gif of the system spinning out radially
        """

        i = 1
        d_theta_y = list(np.linspace(0,-360,num_of_frames+1))
        d_theta_z = list(np.linspace(0,180,num_of_frames+1))

        for i in range(1,num_of_frames+1):

            self.sb.customflip('Varial kickflip',0,d_theta_y[i],d_theta_z[i])

            if i <= 9:
                name_i = '0'+str(i)
            else:
                name_i = str(i)

            save_name = 'Images/frames/{}.png'.format(name_i)
            plt.savefig(save_name)
            plt.clf()
            i = i+1
            print('Frame ({}/{}) Saved.'.format(name_i,num_of_frames))

        self.frames_to_gif('varial_kickflip')

   ######################################################################################


    def make_varial_heelflip_gif(self,num_of_frames=50):
        """
        create a gif of the system spinning out radially
        """

        i = 1
        d_theta_y = list(np.linspace(0,360,num_of_frames+1))
        d_theta_z = list(np.linspace(0,-180,num_of_frames+1))

        for i in range(1,num_of_frames+1):

            self.sb.customflip('Varial Heelflip',0,d_theta_y[i],d_theta_z[i])

            if i <= 9:
                name_i = '0'+str(i)
            else:
                name_i = str(i)

            save_name = 'Images/frames/{}.png'.format(name_i)
            plt.savefig(save_name)
            plt.clf()
            i = i+1
            print('Frame ({}/{}) Saved.'.format(name_i,num_of_frames))

        self.frames_to_gif('varial_heelflip')
   ######################################################################################


    def make_inward_heelflip_gif(self,num_of_frames=50):
        """
        create a gif of the system spinning out radially
        """

        i = 1
        d_theta_y = list(np.linspace(0,360,num_of_frames+1))
        d_theta_z = list(np.linspace(0,180,num_of_frames+1))

        for i in range(1,num_of_frames+1):

            self.sb.customflip('Inward Heelflip',0,d_theta_y[i],d_theta_z[i])

            if i <= 9:
                name_i = '0'+str(i)
            else:
                name_i = str(i)

            save_name = 'Images/frames/{}.png'.format(name_i)
            plt.savefig(save_name)
            plt.clf()
            i = i+1
            print('Frame ({}/{}) Saved.'.format(name_i,num_of_frames))

        self.frames_to_gif('inward_heelflip')

################################################################################
# End of class
################################################################################
