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

    def make_ollie_gif(self,num_of_frames=50):
        """
        """ 
        i = 1
        for theta_h in list(np.linspace(0,180,num_of_frames)):
            
            self.sb.customflip('Ollie',0,0,0,theta_h=theta_h)

            if i <= 9:
                name_i = '0'+str(i)
            else:
                name_i = str(i)

            save_name = 'Images/frames/{}.png'.format(name_i)
            plt.savefig(save_name)
            plt.clf()
            i = i+1
            print('Frame ({}/{}) Saved.'.format(name_i,num_of_frames))

        self.frames_to_gif('ollie')

    ######################################################################################

    def make_kickflip_gif(self,num_of_frames=50):
        """
        create a gif of a kickflip
        """

        i = 1

        d_theta_y = list(np.linspace(0,-360,num_of_frames+1))
        d_theta_h = list(np.linspace(0,180,num_of_frames+1))

        for i in range(1,num_of_frames+1):

            self.sb.customflip('Kickflip',0,d_theta_y[i],0,theta_h=d_theta_h[i])

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
        create a gif of a heelflip
        """

        i = 1

        d_theta_y = list(np.linspace(0,360,num_of_frames+1))
        d_theta_h = list(np.linspace(0,180,num_of_frames+1))

        for i in range(1,num_of_frames+1):


            self.sb.customflip('Heelflip',0,d_theta_y[i],0,theta_h=d_theta_h[i])

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
        create a gif of a bs 360 shuv
        """

        i = 1

        d_theta_z = list(np.linspace(0,360,num_of_frames+1))
        d_theta_h = list(np.linspace(0,180,num_of_frames+1))

        for i in range(1,num_of_frames+1):

            self.sb.customflip('BS 360 Shuvit',0,0,d_theta_z[i],theta_h=d_theta_h[i])


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
        create a gif of a fs 360 shuv
        """

        i = 1

        d_theta_z = list(np.linspace(0,-360,num_of_frames+1))
        d_theta_h = list(np.linspace(0,180,num_of_frames+1))

        for i in range(1,num_of_frames+1):

            self.sb.customflip('FS 360 Shuvit',0,0,d_theta_z[i],theta_h=d_theta_h[i])

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
        create a gif of a front foot impossible
        """

        i = 1
        d_theta_x = list(np.linspace(0,-360,num_of_frames+1))
        d_theta_h = list(np.linspace(0,180,num_of_frames+1))

        for i in range(1,num_of_frames+1):

            self.sb.customflip('Front Foot Impossible',d_theta_x[i],0,0,theta_h=d_theta_h[i])

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
        create a gif of a back foor impossible
        """

        i = 1
        d_theta_x = list(np.linspace(0,360,num_of_frames+1))
        d_theta_h = list(np.linspace(0,180,num_of_frames+1))

        for i in range(1,num_of_frames+1):

            self.sb.customflip('Back Foot Impossible',d_theta_x[i],0,0,theta_h=d_theta_h[i])

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
        create a gif of a treflip
        """

        i = 1
        d_theta_y = list(np.linspace(360,0,num_of_frames+1))
        d_theta_z = list(np.linspace(0,360,num_of_frames+1))
        d_theta_h = list(np.linspace(0,180,num_of_frames+1))

        for i in range(1,num_of_frames+1):

            self.sb.customflip('Treflip',0,d_theta_y[i],d_theta_z[i],theta_h=d_theta_h[i])

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
        create a gif of a lazerflip
        """

        i = 1
        d_theta_y = list(np.linspace(0,360,num_of_frames+1))
        d_theta_z = list(np.linspace(0,-360,num_of_frames+1))
        d_theta_h = list(np.linspace(0,180,num_of_frames+1))

        for i in range(1,num_of_frames+1):

            self.sb.customflip('Lazerflip',0,d_theta_y[i],d_theta_z[i],theta_h=d_theta_h[i])

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
        create a gif of a hardflip
        """

        i = 1
        d_theta_y = list(np.linspace(0,-360,num_of_frames+1))
        d_theta_z = list(np.linspace(0,-180,num_of_frames+1))
        d_theta_h = list(np.linspace(0,180,num_of_frames+1))

        for i in range(1,num_of_frames+1):

            self.sb.customflip('Hardflip',0,d_theta_y[i],d_theta_z[i],theta_h=d_theta_h[i])

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
        create a gif of a varial kickflip
        """

        i = 1
        d_theta_y = list(np.linspace(0,-360,num_of_frames+1))
        d_theta_z = list(np.linspace(0,180,num_of_frames+1))
        d_theta_h = list(np.linspace(0,180,num_of_frames+1))

        for i in range(1,num_of_frames+1):

            self.sb.customflip('Varial kickflip',0,d_theta_y[i],d_theta_z[i],theta_h=d_theta_h[i])

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
        create a gif a varial heelflip
        """

        i = 1
        d_theta_y = list(np.linspace(0,360,num_of_frames+1))
        d_theta_z = list(np.linspace(0,-180,num_of_frames+1))
        d_theta_h = list(np.linspace(0,180,num_of_frames+1))

        for i in range(1,num_of_frames+1):

            self.sb.customflip('Varial Heelflip',0,d_theta_y[i],d_theta_z[i],theta_h=d_theta_h[i])

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
        create a gif of an inward heelflip
        """

        i = 1
        d_theta_y = list(np.linspace(0,360,num_of_frames+1))
        d_theta_z = list(np.linspace(0,180,num_of_frames+1))
        d_theta_h = list(np.linspace(0,180,num_of_frames+1))

        for i in range(1,num_of_frames+1):

            self.sb.customflip('Inward Heelflip',0,d_theta_y[i],d_theta_z[i],theta_h=d_theta_h[i])

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
