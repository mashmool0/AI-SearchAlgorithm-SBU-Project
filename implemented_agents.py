from agent import AbstractSearchAgent
import math


class BFSAgent(AbstractSearchAgent):
    def searching(self):
        ...  # TODO


class BiIDDFSAgent(AbstractSearchAgent):
    def searching(self):
        ...  # TODO


class AStarAgent(AbstractSearchAgent):
    def __init__(self, s_start, s_goal, environment, euclidean_cost=True):
        super().__init__(s_start, s_goal, environment, euclidean_cost)

        # should change some item because we are in A*
        self.euclidean_cost = True

    def calculate_heuristic(self, neighbors):
        heuristic = {}
        print(f"goal state : {self.s_goal}")
        x_s, y_s = self.s_goal[0], self.s_goal[1]
        print(f"x_sg : {x_s} , y_sg : {y_s}")
        print(f" x2 : {neighbors[0][0]} ,  y2 : {neighbors[0][1]}")
        print(f"neighbor test : {neighbors[0]}")
        for item in neighbors:
            heuristic[item] = math.sqrt(
                abs((x_s - item[0]) ** 2 + (y_s - item[1]) ** 2))

        return heuristic

    def calculate_f_n(self, h_n: dict, g_n: dict):
        # f(n) = g(n) + h(n)
        f_n = {}
        for item in g_n:
            f_n[item] = g_n[item] + h_n[item]

        return f_n

    def best_node_for_expand(self, f_n: dict):
        print("\nFind Best Node For Expand:\n")
        best_node = ()
        min_num = 999999
        for item in f_n:
            print(item)
            if f_n[item] < min_num:
                min_num = f_n[item]
                best_node = item

        return best_node

    def searching(self):
        print("Start A* Search Algorithm ")

        # find valid neighbors
        valid_neighbors = self.get_neighbors(self.current_state)

        #  TODO : Maybe should change it to another function
        g_n = self.NEIGHBOR_COSTS.get(self.current_state)

        h_n = self.calculate_heuristic(valid_neighbors)

        f_n = self.calculate_f_n(h_n, g_n)

        best_node = self.best_node_for_expand(f_n)

        # Updating Data
        self.VISITED.add(self.current_state)
        self.PARENT[best_node] = self.current_state
        self.current_state = best_node

        # Print Data
        print(f"im here : {self.current_state}")
        print(f"h(n)_s : {h_n}")
        print(f"g(n)_s : {g_n}")
        print(f"f(n)_s : {f_n}")
        print("valid neighbors : ", valid_neighbors)
        print(f"best node for expand : {best_node}")
        return [(1, 1)], [(5, 5)]


class UCSAgent(AbstractSearchAgent):
    def searching(self):
        ...  # TODO
