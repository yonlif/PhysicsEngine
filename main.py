from world.world_viewer import WorldViewer
from world.worlds import swing_spring_test


def main():
    my_world = swing_spring_test()
    viewer = WorldViewer(my_world)
    viewer.run()


if __name__ == '__main__':
    main()
