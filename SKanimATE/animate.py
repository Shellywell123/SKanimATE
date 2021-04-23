from SKanimATE.skate import PySkate
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
        print('#'*55)
        print(' PyAnimate initalised ')#+self.time.get_live_time())
        print('#'*55)

    ######################################################################################

    def frames_to_gif_old(self,gifname):
        """
        converts all images in frames dir to a gif
        """
        import imageio
        images = []
        for filename in os.listdir('Images/frames/'):
            images.append(imageio.imread('Images/frames/'+filename, format='GIF-PIL'))
        filename = 'Images/gifs/{}.gif'.format(gifname)
        imageio.mimsave(filename, images)
        print('{} made'.format(filename))

    ######################################################################################

    def frames_to_gif(self,gifname):
        """
        same functionality as frames_to_gif_old(), but makes gif cropped and transparent
        """
        from PIL import Image

        def gen_frame(path):
            im = Image.open(path)
            alpha = im.getchannel('A')
            

            # Convert the image into P mode but only use 255 colors in the palette out of 256
            im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE, colors=255)

            # Set all pixel values below 128 to 255 , and the rest to 0
            mask = Image.eval(alpha, lambda a: 255 if a <=128 else 0)

            # Paste the color of index 255 and use alpha as a mask
            im.paste(255, mask)

            # The transparency index is 255
            im.info['transparency'] = 255


            #crop image
            # Setting the points for cropped image

            width, height = im.size

            left = 102
            top = 0
            right = 718
            bottom = 616
              
            # Cropped image of above dimension
            # (It will not change orginal image)
            im = im.crop((left, top, right, bottom))

            return im

        images = []
        for filename in os.listdir('Images/frames/'):
            images.append(gen_frame('Images/frames/'+filename))
        filename = 'Images/gifs/{}.gif'.format(gifname)
        images[0].save(filename, save_all=True, append_images=images[1:], loop=0, duration=150,disposal=3,format='GIF',)
        print('{} made'.format(filename))


    ######################################################################################

    def make_all_gifs(self,num_of_frames=25):
        """
        create a gifs of all skate tricks
        """
        from SKanimATE.data import PyData
        d = PyData(num_of_frames)

        for trick_info in d.trick_list:

            trick_name = trick_info['trick name']
            d_theta_x  = trick_info['x_rot_angles']
            d_theta_y  = trick_info['y_rot_angles']
            d_theta_z  = trick_info['z_rot_angles']
            d_theta_h  = trick_info['h_rot_angles']
            d_theta_r  = trick_info['r_rot_angles']

            for i in range(0,num_of_frames):

                if trick_name[:6] == 'Nollie':
                    self.sb.customnollieflip(
                        name     = trick_name,
                        dtheta_x = d_theta_x[i],
                        dtheta_y = d_theta_y[i],
                        dtheta_z = d_theta_z[i],
                        theta_h  = d_theta_h[i],
                        theta_r  = d_theta_r[i],
                        n=i)
                else:
                    self.sb.customflip(
                        name     = trick_name,
                        dtheta_x = d_theta_x[i],
                        dtheta_y = d_theta_y[i],
                        dtheta_z = d_theta_z[i],
                        theta_h  = d_theta_h[i],
                        theta_r  = d_theta_r[i],
                        n=i)

                if i <= 8:
                    name_i = '0'+str(i+1)
                else:
                    name_i = str(i+1)

                save_name = 'Images/frames/{}.png'.format(name_i)
                plt.savefig(save_name, transparent=True)
                plt.clf()
                print('Frame ({}/{}) Saved.'.format(name_i,num_of_frames))

            self.frames_to_gif(trick_name)

 ######################################################################################

    def make_single_gif(self,trick_name,num_of_frames=25):
        """
        create a gifs of a skate trick
        """
        from SKanimATE.data import PyData
        d = PyData(num_of_frames)

        trick_name = trick_name.lower()
        trick_info = eval('d.{}_info'.format(trick_name.replace(' ','_')))

        trick_name = trick_info['trick name']
        d_theta_x  = trick_info['x_rot_angles']
        d_theta_y  = trick_info['y_rot_angles']
        d_theta_z  = trick_info['z_rot_angles']
        d_theta_h  = trick_info['h_rot_angles']
        d_theta_r  = trick_info['r_rot_angles']

        for i in range(0,num_of_frames):

            if trick_name[:6] == 'Nollie':
                self.sb.customnollieflip(
                    name     = trick_name,
                    dtheta_x = d_theta_x[i],
                    dtheta_y = d_theta_y[i],
                    dtheta_z = d_theta_z[i],
                    theta_h  = d_theta_h[i],
                    theta_r  = d_theta_r[i],
                    n=i)
            else:
                self.sb.customflip(
                    name     = trick_name,
                    dtheta_x = d_theta_x[i],
                    dtheta_y = d_theta_y[i],
                    dtheta_z = d_theta_z[i],
                    theta_h  = d_theta_h[i],
                    theta_r  = d_theta_r[i],
                    n=i)

            if i <= 8:
                name_i = '0'+str(i+1)
            else:
                name_i = str(i+1)

            save_name = 'Images/frames/{}.png'.format(name_i)
            plt.savefig(save_name, transparent=True)
            plt.clf()
            print('Frame ({}/{}) Saved.'.format(name_i,num_of_frames))

        self.frames_to_gif(trick_name)

################################################################################
# End of class
################################################################################
