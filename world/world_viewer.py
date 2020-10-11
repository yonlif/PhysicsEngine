import matplotlib.pyplot as plt
import matplotlib.animation as animation

from world import World


class WorldViewer:
    def __init__(self, world: World, frame_delay=10, size=(0, 50)):
        self.world = world
        self.size = size
        self.frame_delay = frame_delay

    def run(self, save_to_file: str=None):
        fig = plt.figure()
        ax = plt.axes(xlim=self.size, ylim=self.size)
        plt.gca().set_aspect('equal', adjustable='box')

        def init():
            for body in self.world.bodies:
                for item in body.draw():
                    ax.add_patch(item)
            return sum([b.draw() for b in self.world.bodies], [])

        def animate(i):
            self.world.update()
            return sum([b.draw() for b in self.world.bodies], [])

        anim = animation.FuncAnimation(fig, animate, interval=self.frame_delay, init_func=init, blit=True)
        if save_to_file:
            anim.save(save_to_file)
        else:
            plt.show()
