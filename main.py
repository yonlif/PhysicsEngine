from world.world_viewer import WorldViewer
from world.worlds import spring_and_collision_test


def main():
    my_world = spring_and_collision_test()
    viewer = WorldViewer(my_world)
    viewer.run()


if __name__ == '__main__':
    main()
