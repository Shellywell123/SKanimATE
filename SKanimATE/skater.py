import numpy as np

################################################################################
# begining of class
################################################################################

class PySkater:

    def __init__(self):
        """
        class initaliser
        """
        # deck dimensions
        self.board_width            = 8
        self.board_mid_length       = 22
        self.board_nose_tail_length = 5

        # truck dimensions
        self.truck_width    = 6
        self.truck_position = 18 #/board_length(32)
        self.axel_radius    = 0.5
        self.truck_height   = 1

        # wheel dimensions
        self.wheel_radius = 1
        self.wheel_width  = 2

     ######################################################################################

    def use_test_right_foot(self):
        """
        right foot dev
        """

    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    import numpy as np
    from itertools import product, combinations


    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # draw sphere

    l = 1
    w = 0.5
    h = 0.3

    #main-toe-top
    u, v = np.mgrid[0:np.pi:20j, 0:np.pi/2:10j]
    x = w*np.cos(u)*np.sin(v)
    y = l*np.sin(u)*np.sin(v)
    z = h*np.cos(v)
    ax.plot_surface(x, y, z, color="r")

    #main-toe-bot
    u, v = np.mgrid[0:np.pi:20j, np.pi/2:np.pi:10j]
    x = w*np.cos(u)*np.sin(v)
    y = l*np.sin(u)*np.sin(v)
    z = h*np.cos(v)
    ax.plot_surface(x, y, z, color="b")


    #heel-bot
    u, v = np.mgrid[0:-np.pi:20j, np.pi/2:np.pi:10j]
    x = w*np.cos(u)*np.sin(v)
    y = 0.5*l*np.sin(u)*np.sin(v)
    z = h*np.cos(v)
    ax.plot_surface(x, y, z, color="b")

    #ankle
    u, v = np.mgrid[0:-np.pi:20j, 0:np.pi/2:10j]
    x = w*np.cos(u)*np.sin(v)
    y = 0.5*l*np.sin(u)*np.sin(v)
    z = h*2*np.cos(v)
    ax.plot_surface(x, y, z, color="r")

    #shin
    u, v = np.mgrid[0:-np.pi:20j, 0:np.pi/2:10j]
    x = w*np.cos(u)*np.sin(v)
    y = np.zeros(x.shape)
    z = h*2*np.cos(v)
    ax.plot_surface(x, y, z, color="g")
    ax.set_title('test-shoe-model')

    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)

    plt.show()

     ######################################################################################


################################################################################
# End of class
################################################################################
