import time

from env import Env
from plotting import Plotting

from implemented_agents import BFSAgent, BiIDDFSAgent, AStarAgent, UCSAgent


def which_one_you_want(start, goal, environment):
    wh = 0
    while True:
        print("Enter number Between 1,4:")
        print("1.A* Algorithm")
        print("2.BFS Algorithm")
        print("3.UCS Algorithm")
        print("4.BiIDFS Algorithm")
        wh = int(input())
        print(wh)
        if wh == 1 or wh == 2 or wh == 3 or wh == 4:
            break
        else:
            print("Wrong Input!!! please enter True input")

    if wh == 1:
        agent = AStarAgent(start, goal, environment, True)
        return agent, True
    if wh == 2:
        agent = BFSAgent(start, goal, environment, False)
        return agent, False
    if wh == 3:
        agent = UCSAgent(start, goal, environment, True)
        return agent, True
    if wh == 4:
        agent = BiIDDFSAgent(start, goal, environment, False)
        return agent, False


def main():
    map_name = "default"  # Choose the map file
    use_random_teleports = False  # Change to True to use random teleports
    num_pairs = 2  # Number of random teleport gates if enabled
    FPS = 60  # Frames per second for animation

    start = (5, 5)  # Start position
    goal = (45, 25)  # Goal position

    environment = Env(map_name, use_random_teleports, num_pairs)

    agent, euclidean_cost = which_one_you_want(
        start, goal, environment)

    print(f"euclidean_cost is {euclidean_cost}")
    start_time = time.time()
    path, visited = agent.searching()
    end_time = time.time()
    run_time = end_time - start_time
    print(f"Search completed in {run_time:.5f} seconds")

    plot = Plotting(start, goal, environment, FPS)
    plot.animation(path, visited, agent.COST)


if __name__ == "__main__":
    main()
