import numpy as np

################################################################################
# begining of class
################################################################################

class PyTransforms():
    def __init__(self):
       """
       class initaliser
       """
       pass

    ######################################################################################

    def degrees_to_radians(self,angle):
        """
        degrees to radians angle converter
        """
        angle = float(angle/180)*np.pi
        return angle

    ######################################################################################

    def x_clockwise(self,x,y,z,theta):
        """
        """
        theta = self.degrees_to_radians(theta)

        X =  x
        Y = -z*np.sin(theta)+y*np.cos(theta)
        Z =  z*np.cos(theta)+y*np.sin(theta)

        return X,Y,Z

    ######################################################################################

    def y_clockwise(self,x,y,z,theta):
        """
        heelflip
        """
        theta = self.degrees_to_radians(theta)

        X =  x*np.cos(theta)+z*np.sin(theta)
        Y =  y
        Z = -x*np.sin(theta)+z*np.cos(theta)

        return X,Y,Z

    ######################################################################################

    def z_clockwise(self,x,y,z,theta):
        """
        bs shuv
        """
        theta = self.degrees_to_radians(theta)

        X =  x*np.cos(theta)+y*np.sin(theta)
        Y = -x*np.sin(theta)+y*np.cos(theta)
        Z =  z

        return X,Y,Z

    ######################################################################################

    def x_anticlockwise(self,x,y,z,theta):
        """
        """
        X,Y,Z = self.x_clockwise(x,y,z,-theta)

        return X,Y,Z

    ######################################################################################

    def y_anticlockwise(self,x,y,z,theta):
        """
        kickflip
        """
        X,Y,Z = self.y_clockwise(x,y,z,-theta)

        return X,Y,Z

    ######################################################################################

    def z_anticlockwise(self,x,y,z,theta):
        """
        fs shuv
        """
        X,Y,Z = self.z_clockwise(x,y,z,-theta)

        return X,Y,Z

    ######################################################################################

    def custom(self,x,y,z,theta_x,theta_y,theta_z):
        """
        for multi dimensional rotations i.e tre flips
        """

        x,y,z = self.x_clockwise(x,y,z,theta_x)
        x,y,z = self.y_clockwise(x,y,z,theta_y)
        x,y,z = self.z_clockwise(x,y,z,theta_z)

        return x,y,z

    ######################################################################################

    def ollie_motion(self,x,y,z,theta_h,theta_r):
        """
        transforms board orientation in an ollie motion
        """

        max_ollie_height = 35

        x,y,z=self.x_clockwise(x,y,z,theta_r)

        theta_h = self.degrees_to_radians(theta_h)

        current_hieght = max_ollie_height*np.sin(theta_h)

        x = x
        y = y 
        z = z + current_hieght

        return x,y,z

    ######################################################################################

    def nollie_motion(self,x,y,z,theta_h,theta_r):
        """
        transforms board orientation in an nollie motion
        """

        max_nollie_height = 35

        x,y,z=self.x_anticlockwise(x,y,z,theta_r)

        theta_h = self.degrees_to_radians(theta_h)

        current_hieght = max_nollie_height*np.sin(theta_h)

        x = x
        y = y 
        z = z + current_hieght

        return x,y,z

    ######################################################################################

    def cruise_motion(self,x,y,z,n):
        """
        will make gif shift along y axis at a rate of 5 units per frame
        """
        orgin_adjust = 7

        x = x
        y = y + (0.5*n) - orgin_adjust
        z = z

        return x,y,z

################################################################################
# End of class
################################################################################
