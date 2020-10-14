from world.world_viewer import WorldViewer
from world.worlds import *


def main():
    my_world = spring_and_collision_test()
    viewer = WorldViewer(my_world, frame_delay=20)
    viewer.run()


if __name__ == '__main__':
    main()
