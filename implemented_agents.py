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
        # should change some item because we are in  A*
        self.euclidean_cost = True

    def calculate_heuristic(self, neighbors):
        heuristic = {}
        x_s, y_s = self.s_goal[0], self.s_goal[1]
        for item in neighbors:
            if item in self.teleports.values():
                heuristic[item] = math.sqrt(
                    abs((x_s - item[0])**2 + (y_s - item[1])))
            else:
                heuristic[item] = math.sqrt(
                    abs((x_s - item[0]) ** 2 + (y_s - item[1]) ** 2))

        return heuristic

    def calculate_f_n(self, h_n: dict, g_n: dict, open_list: dict):
        # f(n) = g(n) + h(n)

        for item in g_n:
            if open_list.get(item) == None:
                open_list[item] = g_n[item] + h_n[item]

            elif open_list[item] > g_n[item] + h_n[item]:
                open_list[item] = g_n[item] + h_n[item]
        return open_list

    def best_node_for_expand(self, open_list: list, close_list: list):
        best_node_num = 10000
        best_node = ()

        for item in open_list:
            if item not in close_list:
                if open_list[item] < best_node_num:
                    best_node_num = open_list[item]
                    best_node = item

        return best_node

    def searching(self):
        open_list = {self.s_start: 0, }
        self.COST[self.s_start] = 0
        close_list = []

        while len(open_list) != 0:
            valid_neighbors_teleported = []
            g_n_neighbors = {}
            # let's find best f(n) in open list
            best_node = self.best_node_for_expand(open_list, close_list)
            open_list.pop(best_node)
            self.VISITED.append(best_node)
            close_list.append(best_node)
            if best_node == self.s_goal:
                break

            # Take Child of best node with their g(n) and h(n) and calculate f(n)

            valid_neighbors = self.get_neighbors(
                best_node)
            # Update g(n)
            for item in valid_neighbors:
                if self.COST.get(item) == None:
                    self.COST[item] = self.COST[best_node] + \
                        self.get_cost(best_node, item)
                    g_n_neighbors[item] = self.COST[item]
                    self.PARENT[item] = best_node

                else:
                    if self.COST[item] > self.COST[best_node] + self.get_cost(best_node, item):
                        self.COST[item] = self.COST[best_node] + \
                            self.get_cost(best_node, item)
                        g_n_neighbors[item] = self.COST[item]
                        self.PARENT[item] = best_node

            h_n_neighbors = self.calculate_heuristic(valid_neighbors)
            open_list = self.calculate_f_n(
                h_n_neighbors, g_n_neighbors, open_list)

        return self.extract_path(), self.VISITED


class UCSAgent(AbstractSearchAgent):
    def searching(self):
        ...  # TODO
