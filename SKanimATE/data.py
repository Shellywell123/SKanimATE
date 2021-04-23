from SKanimATE.transforms import PyTransforms
tf = PyTransforms()
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

        ########################################################################
        # trick height calculations
        ########################################################################

        # height of trick
        self.d_theta_h  = list(np.linspace(0,180,self.num_of_frames))

        ########################################################################
        # lean angle of trick during pop to land
        ########################################################################

        # max angle of board at pop
        self.pop_lean_max = 60

        # bone lean angle
        self.bone_angle = 20
        # convert angle of bone as a percentage of pop lean max i.e 90 = 60
        self.bone_angle_per = (self.bone_angle/self.pop_lean_max)*90
        self.bone_angle_rad = tf.degrees_to_radians(self.bone_angle_per)

        # frame of ollie arch peak
        self.peak_frame     = int(0.5*self.num_of_frames)
        self.stomp_duration = self.num_of_frames-self.peak_frame
        
        # bone is different for nollie/ollie
        self.d_theta_r  = []
        self.d_theta_r_no_bone  = []
        self.d_theta_r_nollie  = []
        self.d_theta_r_nollie_no_bone  = []

        # pop to bone frames
        self.board_angle1       = list(np.linspace(0,np.pi+self.bone_angle_rad,self.peak_frame))
        self.board_angle1_no_bone = list(np.linspace(0,np.pi,self.peak_frame))
        self.board_angle1_nollie = list(np.linspace(0,np.pi-self.bone_angle_rad,self.peak_frame))
        self.board_angle1_nollie_no_bone = list(np.linspace(0,np.pi,self.peak_frame))
        for i in range(0,self.peak_frame):
            self.d_theta_r.append(self.pop_lean_max*np.sin(self.board_angle1[i]))
            self.d_theta_r_no_bone.append(self.pop_lean_max*np.sin(self.board_angle1_no_bone[i]))
            self.d_theta_r_nollie.append(self.pop_lean_max*np.sin(self.board_angle1_nollie[i]))
            self.d_theta_r_nollie_no_bone.append(self.pop_lean_max*np.sin(self.board_angle1_nollie_no_bone[i]))

        # bone to land frames
        self.board_angle2 = list(np.linspace(0,np.pi/2,self.stomp_duration))
        for i in range(0,self.stomp_duration):
            self.d_theta_r.append(-self.bone_angle_per*np.cos(self.board_angle2[i]))
            self.d_theta_r_no_bone.append(0)

        for i in range(0,self.stomp_duration):
            self.d_theta_r_nollie.append(self.bone_angle_per*np.cos(self.board_angle2[i]))
            self.d_theta_r_nollie_no_bone.append(0)

        ########################################################################
        # flip : catch duration calculations
        ########################################################################

        self.frame_of_catch = int(0.6*self.num_of_frames)
        self.post_catch     = self.num_of_frames = self.frame_of_catch
        self.catch_and_land = [0]*self.post_catch

        ########################################################################
        # flip data
        ########################################################################

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
                'r_rot_angles' : self.d_theta_r_nollie
                }

        self.kickflip_info = {
                'trick name'   : 'Kickflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,-360,self.frame_of_catch))+self.catch_and_land,
                'z_rot_angles' : self.list_of_zeros,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_kickflip_info = {
                'trick name'   : 'Nollie Kickflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,-360,self.frame_of_catch))+self.catch_and_land,
                'z_rot_angles' : self.list_of_zeros,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r_nollie
                }

        self.heelflip_info = {
                'trick name'   : 'Heelflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,360,self.frame_of_catch))+self.catch_and_land,
                'z_rot_angles' : self.list_of_zeros,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_heelflip_info = {
                'trick name'   : 'Nollie Heelflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,360,self.frame_of_catch))+self.catch_and_land,
                'z_rot_angles' : self.list_of_zeros,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r_nollie
                }

        self.BS_360_pop_shuvit_info = {
                'trick name'   : 'BS 360 Pop Shuvit',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : self.list_of_zeros,
                'z_rot_angles' : list(np.linspace(0,360,self.frame_of_catch))+self.catch_and_land,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_BS_360_pop_shuvit_info = {
                'trick name'   : 'Nollie BS 360 Pop Shuvit',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : self.list_of_zeros,
                'z_rot_angles' : list(np.linspace(0,-360,self.frame_of_catch))+self.catch_and_land,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r_nollie
                }

        self.FS_360_pop_shuvit_info = {
                'trick name'   : 'FS 360 Pop Shuvit',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : self.list_of_zeros,
                'z_rot_angles' : list(np.linspace(0,-360,self.frame_of_catch))+self.catch_and_land,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_FS_360_pop_shuvit_info = {
                'trick name'   : 'Nollie FS 360 Pop Shuvit',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : self.list_of_zeros,
                'z_rot_angles' : list(np.linspace(0,360,self.frame_of_catch))+self.catch_and_land,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r_nollie
                }

        self.back_foot_impossible_info = {
                'trick name'   : 'Back Foot Impossible',
                'x_rot_angles' : list(np.linspace(0,360,self.frame_of_catch))+self.catch_and_land,
                'y_rot_angles' : self.list_of_zeros,
                'z_rot_angles' : self.list_of_zeros,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r_no_bone
                }

        self.nollie_back_foot_impossible_info = {
                'trick name'   : 'Nollie Back Foot Impossible',
                'x_rot_angles' : list(np.linspace(0,360,self.frame_of_catch))+self.catch_and_land,
                'y_rot_angles' : self.list_of_zeros,
                'z_rot_angles' : self.list_of_zeros,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r_nollie_no_bone
                }

        self.front_foot_impossible_info = {
                'trick name'   : 'Front Foot Impossible',
                'x_rot_angles' : list(np.linspace(0,-360,self.frame_of_catch))+self.catch_and_land,
                'y_rot_angles' : self.list_of_zeros,
                'z_rot_angles' : self.list_of_zeros,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r_no_bone
                }

        self.nollie_front_foot_impossible_info = {
                'trick name'   : 'Nollie Front Foot Impossible',
                'x_rot_angles' : list(np.linspace(0,-360,self.frame_of_catch))+self.catch_and_land,
                'y_rot_angles' : self.list_of_zeros,
                'z_rot_angles' : self.list_of_zeros,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r_nollie_no_bone
                }

        self.treflip_info = {
                'trick name'   : 'Treflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,-360,self.frame_of_catch))+self.catch_and_land,
                'z_rot_angles' : list(np.linspace(0,360,self.frame_of_catch))+self.catch_and_land,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_treflip_info = {
                'trick name'   : 'Nollie Treflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,-360,self.frame_of_catch))+self.catch_and_land,
                'z_rot_angles' : list(np.linspace(0,-360,self.frame_of_catch))+self.catch_and_land,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r_nollie
                }

        self.lazerflip_info = {
                'trick name'   : 'Lazerflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,360,self.frame_of_catch))+self.catch_and_land,
                'z_rot_angles' : list(np.linspace(0,-360,self.frame_of_catch))+self.catch_and_land,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_lazerflip_info = {
                'trick name'   : 'Nollie Lazerflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,360,self.frame_of_catch))+self.catch_and_land,
                'z_rot_angles' : list(np.linspace(0,360,self.frame_of_catch))+self.catch_and_land,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r_nollie
                }

        self.hardflip_info = {
                'trick name'   : 'Hardflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,-360,self.frame_of_catch))+self.catch_and_land,
                'z_rot_angles' : list(np.linspace(0,-180,self.frame_of_catch))+self.catch_and_land,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_hardflip_info = {
                'trick name'   : 'Nollie Hardflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,-360,self.frame_of_catch))+self.catch_and_land,
                'z_rot_angles' : list(np.linspace(0,180,self.frame_of_catch))+self.catch_and_land,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r_nollie
                }
                
        self.inward_heelflip_info = {
                'trick name'   : 'Inward Heelflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,360,self.frame_of_catch))+self.catch_and_land,
                'z_rot_angles' : list(np.linspace(0,180,self.frame_of_catch))+self.catch_and_land,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_inward_heelflip_info = {
                'trick name'   : 'Nollie Inward Heelflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,360,self.frame_of_catch))+self.catch_and_land,
                'z_rot_angles' : list(np.linspace(0,-180,self.frame_of_catch))+self.catch_and_land,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r_nollie
                }

        self.varial_heelflip_info = {
                'trick name'   : 'Varial Heelflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,360,self.frame_of_catch))+self.catch_and_land,
                'z_rot_angles' : list(np.linspace(0,-180,self.frame_of_catch))+self.catch_and_land,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_varial_heelflip_info = {
                'trick name'   : 'Nollie Varial Heelflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,360,self.frame_of_catch))+self.catch_and_land,
                'z_rot_angles' : list(np.linspace(0,180,self.frame_of_catch))+self.catch_and_land,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r_nollie
                }

        self.varial_kickflip_info = {
                'trick name'   : 'Varial Kickflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,-360,self.frame_of_catch))+self.catch_and_land,
                'z_rot_angles' : list(np.linspace(0,180,self.frame_of_catch))+self.catch_and_land,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r
                }

        self.nollie_varial_kickflip_info = {
                'trick name'   : 'Nollie Varial Kickflip',
                'x_rot_angles' : self.list_of_zeros,
                'y_rot_angles' : list(np.linspace(0,-360,self.frame_of_catch))+self.catch_and_land,
                'z_rot_angles' : list(np.linspace(0,-180,self.frame_of_catch))+self.catch_and_land,
                'h_rot_angles' : self.d_theta_h,
                'r_rot_angles' : self.d_theta_r_nollie
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
