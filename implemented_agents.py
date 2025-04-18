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
        print(environment)
        # should change some item because we are in  A*
        self.euclidean_cost = True

    def calculate_heuristic(self, neighbors):
        heuristic = {}
        x_s, y_s = self.s_goal[0], self.s_goal[1]
        for item in neighbors:
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
        print("updated open list : ", open_list)
        return open_list

    def best_node_for_expand(self, open_list: list):
        print("\nFind Best Node For Expand:\n")
        best_node_num = 10000
        best_node = ()

        for item in open_list:
            if open_list[item] < best_node_num:
                best_node_num = open_list[item]
                best_node = item

        return best_node

    def searching(self):
        print("Start A* Search Algorithm ")
        open_list = {self.s_start: 0, }
        self.COST[self.s_start] = 0

        close_list = []
        while len(open_list) != 0:
            # let's find best f(n) in open list
            best_node = self.best_node_for_expand(open_list)
            close_list.append(open_list.pop(best_node))
            if best_node == self.s_goal:
                break

            # Take Child of best node with their g(n) and h(n) and calculate f(n)
            valid_neighbors = self.get_neighbors(best_node)

            # Update g(n)
            for item in valid_neighbors:
                if self.COST.get(item) == None:
                    self.COST[item] = self.COST[best_node] + \
                        self.get_cost(best_node, item)
                else:
                    if self.COST[item] > self.COST[best_node] + self.get_cost(best_node, item):
                        self.COST[item] = self.COST[best_node] + \
                            self.get_cost(best_node, item)

                open_list[item]
            h_n_neighbors = self.calculate_heuristic(valid_neighbors)
            open_list = self.calculate_f_n(
                h_n_neighbors, self.COST, open_list)

            print("g(n) : ", self.COST)
            print("h(n) : ", h_n_neighbors)
            print(f"open list: {open_list}")
            # # while self.current_state != self.s_goal:
            #     # find valid neighbors
            #     valid_neighbors = self.get_neighbors(self.current_state)

            #     #  TODO : Maybe should change it to another function
            #     g_n = self.NEIGHBOR_COSTS.get(self.current_state)

            #     h_n = self.calculate_heuristic(valid_neighbors)

            #     # will return self.f_n in Agent Abstract
            #     f_n = self.calculate_f_n(h_n, g_n)

            #     best_node = self.best_node_for_expand(f_n)

            #     # Updating Data
            #     self.VISITED.append(self.current_state)
            #     self.PARENT[best_node] = self.current_state
            #     self.COST[best_node] = f_n[best_node]
            #     self.current_state = best_node

            #     # Print Data
            #     print(f"im here : {self.current_state}")
            #     print(f"f_n : {self.f_n}")
            #     print(f"g(n) : {g_n}")
            #     print(f"h(n) : {h_n}")
            #     print(f"best node for expand : {best_node}")

        return self.extract_path(), self.VISITED


class UCSAgent(AbstractSearchAgent):
    def searching(self):
        ...  # TODO
