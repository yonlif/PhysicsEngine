import matplotlib.pyplot as plt
import matplotlib.animation as animation

from world.world import World


class WorldViewer:
    def __init__(self, world: World, speed=1, frame_delay=10, duration=None, size=(0, 50)):
        self.world = world
        self.size = size
        self.frame_delay = frame_delay
        self.duration = duration
        self.speed = speed

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
            self.world.update(timedelta=self.speed)
            return sum([b.draw() for b in self.world.bodies], [])

        anim = animation.FuncAnimation(fig,
                                       animate,
                                       interval=self.frame_delay,
                                       frames=self.duration,
                                       init_func=init, blit=True)
        if save_to_file:
            anim.save(save_to_file)
        else:
            plt.show()
