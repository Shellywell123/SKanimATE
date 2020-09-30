
import numpy as np

################################################################################
# begining of class
################################################################################

class PyData:
    """
    class containg dictionaires of flip data
    """

    def __init__(self,num_of_frames):
        """
        class initaliser
        """

        self.num_of_frames = num_of_frames
        self.list_of_zeros = [0]*(self.num_of_frames)

        #ollie/nollie motion

        self.d_theta_h  = list(np.linspace(0,180,self.num_of_frames))
        self.d_theta_r1 = list(np.linspace(0,np.pi,25))
        self.d_theta_r2 = [0]*(self.num_of_frames-len(self.d_theta_r1))
        self.d_theta_r3 = self.d_theta_r1+self.d_theta_r2
        self.d_theta_r  = []

        for i in range(0,self.num_of_frames):
            self.d_theta_r.append(60*np.sin(self.d_theta_r3[i]))

        self.explain_info = {
                'trick name'   : 'explaination',
                'x_rot_angles' : 'list of angles for rotation around the x axis',
                'y_rot_angles' : 'list of angles for rotation around the y axis',
                'z_rot_angles' : 'list of angles for rotation around the z axis',
                'h_rot_angles' : 'list of angles for h*sin(theta)',
                'r_rot_angles' : 'list of angles for ollie motion x rotation'
                }

        self.ollie_info = {
                'trick name'   : 'Ollie',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : self.list_of_zeros,
                'z_rot_angles' : self.list_of_zeros,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_info = {
                'trick name'   : 'Nollie',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : self.list_of_zeros,
                'z_rot_angles' : self.list_of_zeros,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.kickflip_info = {
                'trick name'   : 'Kickflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,-360,self.num_of_frames)),
                'z_rot_angles' : self.list_of_zeros,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_kickflip_info = {
                'trick name'   : 'Nollie Kickflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,-360,self.num_of_frames)),
                'z_rot_angles' : self.list_of_zeros,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.heelflip_info = {
                'trick name'   : 'Heelflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,360,self.num_of_frames)),
                'z_rot_angles' : self.list_of_zeros,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_heelflip_info = {
                'trick name'   : 'Nollie Heelflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,360,self.num_of_frames)),
                'z_rot_angles' : self.list_of_zeros,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.BS_360_pop_shuvit_info = {
                'trick name'   : 'BS 360 Pop Shuvit',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : self.list_of_zeros,
                'z_rot_angles' : list(np.linspace(0,360,self.num_of_frames)),
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_BS_360_pop_shuvit_info = {
                'trick name'   : 'Nollie BS 360 Pop Shuvit',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : self.list_of_zeros,
                'z_rot_angles' : list(np.linspace(0,-360,self.num_of_frames)),
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.FS_360_pop_shuvit_info = {
                'trick name'   : 'FS 360 Pop Shuvit',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : self.list_of_zeros,
                'z_rot_angles' : list(np.linspace(0,-360,self.num_of_frames)),
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_FS_360_pop_shuvit_info = {
                'trick name'   : 'Nollie FS 360 Pop Shuvit',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : self.list_of_zeros,
                'z_rot_angles' : list(np.linspace(0,360,self.num_of_frames)),
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.back_foot_impossible_info = {
                'trick name'   : 'Back Foot Impossible',
                'x_rot_angles' : list(np.linspace(0,360,self.num_of_frames)),
                'y_rot_angles' : self.list_of_zeros,
                'z_rot_angles' : self.list_of_zeros,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_back_foot_impossible_info = {
                'trick name'   : 'Nollie Back Foot Impossible',
                'x_rot_angles' : list(np.linspace(0,360,self.num_of_frames)),
                'y_rot_angles' : self.list_of_zeros,
                'z_rot_angles' : self.list_of_zeros,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.front_foot_impossible_info = {
                'trick name'   : 'Front Foot Impossible',
                'x_rot_angles' : list(np.linspace(0,-360,self.num_of_frames)),
                'y_rot_angles' : self.list_of_zeros,
                'z_rot_angles' : self.list_of_zeros,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_front_foot_impossible_info = {
                'trick name'   : 'Nolie Front Foot Impossible',
                'x_rot_angles' : list(np.linspace(0,-360,self.num_of_frames)),
                'y_rot_angles' : self.list_of_zeros,
                'z_rot_angles' : self.list_of_zeros,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.treflip_info = {
                'trick name'   : 'Treflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,-360,self.num_of_frames)),
                'z_rot_angles' : list(np.linspace(0,360,self.num_of_frames)),
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_treflip_info = {
                'trick name'   : 'Nollie Treflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,-360,self.num_of_frames)),
                'z_rot_angles' : list(np.linspace(0,-360,self.num_of_frames)),
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.lazerflip_info = {
                'trick name'   : 'Lazerflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,360,self.num_of_frames)),
                'z_rot_angles' : list(np.linspace(0,-360,self.num_of_frames)),
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_lazerflip_info = {
                'trick name'   : 'Nollie Lazerflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,360,self.num_of_frames)),
                'z_rot_angles' : list(np.linspace(0,360,self.num_of_frames)),
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.hardflip_info = {
                'trick name'   : 'Hardflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,-360,self.num_of_frames)),
                'z_rot_angles' : list(np.linspace(0,-180,self.num_of_frames)),
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_hardflip_info = {
                'trick name'   : 'Nollie Hardflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,-360,self.num_of_frames)),
                'z_rot_angles' : list(np.linspace(0,180,self.num_of_frames)),
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }
                
        self.inward_heelflip_info = {
                'trick name'   : 'Inward Heelflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,360,self.num_of_frames)),
                'z_rot_angles' : list(np.linspace(0,180,self.num_of_frames)),
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_inward_heelflip_info = {
                'trick name'   : 'Nollie Inward Heelflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,360,self.num_of_frames)),
                'z_rot_angles' : list(np.linspace(0,-180,self.num_of_frames)),
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.varial_heelflip_info = {
                'trick name'   : 'Varial Heelflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,360,self.num_of_frames)),
                'z_rot_angles' : list(np.linspace(0,-180,self.num_of_frames)),
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_varial_heelflip_info = {
                'trick name'   : 'Nollie Varial Heelflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,360,self.num_of_frames)),
                'z_rot_angles' : list(np.linspace(0,180,self.num_of_frames)),
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.varial_kickflip_info = {
                'trick name'   : 'Varial Kickflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,-360,self.num_of_frames)),
                'z_rot_angles' : list(np.linspace(0,180,self.num_of_frames)),
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_varial_kickflip_info = {
                'trick name'   : 'Nollie Varial Kickflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,-360,self.num_of_frames)),
                'z_rot_angles' : list(np.linspace(0,-180,self.num_of_frames)),
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.trick_list = [ self.ollie_info,
                            self.nollie_info,
                            self.kickflip_info,
                            self.nollie_kickflip_info,
                            self.heelflip_info,
                            self.nollie_heelflip_info,
                            self.BS_360_pop_shuvit_info,
                            self.nollie_BS_360_pop_shuvit_info,
                            self.FS_360_pop_shuvit_info,
                            self.nollie_FS_360_pop_shuvit_info,
                            self.front_foot_impossible_info,
                            self.nollie_front_foot_impossible_info,
                            self.back_foot_impossible_info,
                            self.nollie_back_foot_impossible_info,
                            self.treflip_info,
                            self.nollie_treflip_info,
                            self.lazerflip_info,
                            self.nollie_lazerflip_info,
                            self.hardflip_info,
                            self.nollie_hardflip_info,
                            self.inward_heelflip_info,
                            self.nollie_inward_heelflip_info,
                            self.varial_heelflip_info,
                            self.nollie_varial_heelflip_info,
                            self.varial_kickflip_info,
                            self.nollie_varial_kickflip_info]

################################################################################
# End of class
################################################################################
