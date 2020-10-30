from world.world_viewer import WorldViewer
from world.worlds import *


def main():
    my_world = ball_and_floor()
    viewer = WorldViewer(my_world, speed=0.1, frame_delay=20)
    viewer.run()


if __name__ == '__main__':
    main()
