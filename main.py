from world.world_viewer import WorldViewer
from world.worlds import *


def main():
    my_world = advanced_bounce_house_test()
    viewer = WorldViewer(my_world, speed=2, frame_delay=20)
    viewer.run()


if __name__ == '__main__':
    main()
