from agent import AbstractSearchAgent
import math


class BFSAgent(AbstractSearchAgent):
    def __init__(self, s_start, s_goal, environment, euclidean_cost=False):
        super().__init__(s_start, s_goal, environment, euclidean_cost)

    def searching(self):
        q = [self.s_start]
        best_node = ()
        self.COST[self.s_start] = 0
        while best_node != self.s_goal:
            best_node = q.pop(0)

            valid_neighbors = self.get_neighbors(best_node)
            for item in valid_neighbors:
                if item not in self.VISITED:
                    q.append(item)
                    self.VISITED.append(item)
                    self.COST[item] = self.COST[best_node] + 1
                    if item not in self.PARENT:
                        self.PARENT[item] = best_node

        return self.extract_path(), self.VISITED


class BiIDDFSAgent(AbstractSearchAgent):
    def _dls_collect(self, node, limit, visited: list, parent, cost_dict):
        """
        Depth-first traversal to limit depth, collecting visited nodes, parents and costs
        """
        visited.append(node)

        if limit == 0:
            return

        for nbr in self.get_neighbors(node):
            move_cost = self.get_cost(node, nbr)
            total_cost = cost_dict[node] + move_cost

            # Update if first visit or cheaper path found
            if nbr not in cost_dict or total_cost < cost_dict[nbr]:
                parent[nbr] = node
                cost_dict[nbr] = total_cost
                self._dls_collect(nbr, limit - 1, visited, parent, cost_dict)

    def searching(self):
        depth_max = 50
        meet_point = None
        min_cost = float('inf')

        for depth in range(depth_max + 1):
            # Setup data structures
            nodes_fwd, nodes_bwd = list(), list()
            self.VISITED = list()
            parents_fwd, parents_bwd = {
                self.s_start: None}, {self.s_goal: None}
            costs_fwd, costs_bwd = {self.s_start: 0}, {self.s_goal: 0}

            # Collect nodes up to current depth
            self._dls_collect(self.s_start, depth, nodes_fwd,
                              parents_fwd, costs_fwd)
            self._dls_collect(self.s_goal, depth, nodes_bwd,
                              parents_bwd, costs_bwd)

            for n1, n2 in zip(nodes_bwd, nodes_fwd):
                if n1 not in self.VISITED:
                    self.VISITED.append(n1)
                if n2 not in self.VISITED:
                    self.VISITED.append(n2)

            # Find common nodes
            overlap = set(nodes_fwd) & set(nodes_bwd)
            if not overlap:
                continue

            # Find best meeting point
            for mid in overlap:
                sum_cost = costs_fwd[mid] + costs_bwd[mid]
                if sum_cost < min_cost:
                    min_cost = sum_cost
                    meet_point = mid
                    best_parents_fwd, best_parents_bwd = parents_fwd.copy(), parents_bwd.copy()
                    best_costs_fwd, best_costs_bwd = costs_fwd.copy(), costs_bwd.copy()

            # Construct path if meeting point found
            if meet_point is not None:
                # Path from start to meeting point
                path_start = []
                curr = meet_point
                while curr is not None:
                    path_start.append(curr)
                    curr = best_parents_fwd[curr]
                path_start.reverse()

                # Path from meeting point to goal
                path_end = []
                curr = best_parents_bwd[meet_point]
                while curr is not None:
                    path_end.append(curr)
                    curr = best_parents_bwd[curr]

                complete_path = path_start + path_end

                # Update final path info
                self.PARENT.clear()
                self.COST.clear()
                self.COST[self.s_start] = 0
                for i in range(1, len(complete_path)):
                    prev, curr = complete_path[i-1], complete_path[i]
                    self.PARENT[curr] = prev
                    self.COST[curr] = self.COST[prev] + \
                        self.get_cost(prev, curr)
                break

        return self.extract_path(), self.VISITED


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
                    self.COST[item] = self.COST[best_node] +\
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
    def __init__(self, s_start, s_goal, environment, euclidean_cost=True):
        super().__init__(s_start, s_goal, environment, euclidean_cost)

    def calculate_f_n(self, g_n, open_list):
        for item in g_n:
            if item in self.VISITED:
                continue
            if open_list.get(item) == None:
                open_list[item] = g_n[item]
            else:
                if g_n[item] < open_list[item]:
                    open_list[item] = g_n[item]

        return open_list

    def best_node_for_expand(self, open_list):
        best_node = ()
        best_node_num = 999999

        for item in open_list:
            if item not in self.VISITED:
                if open_list[item] < best_node_num:
                    best_node = item
                    best_node_num = open_list[item]

        return best_node

    def searching(self):
        best_node = ()
        open_list = {self.s_start: 0, }
        self.COST[self.s_start] = 0

        while best_node != self.s_goal:
            # Take Best Node For expand
            best_node = self.best_node_for_expand(open_list)
            self.VISITED.append(best_node)

            # Take Valid Neighbors
            valid_neighbors = self.get_neighbors(best_node)
            g_n_neighbors = {}

            # Update g(n)
            for item in valid_neighbors:
                if self.COST.get(item) == None:
                    self.COST[item] = self.COST[best_node] +\
                        self.get_cost(best_node, item)
                    g_n_neighbors[item] = self.COST[item]
                    self.PARENT[item] = best_node

                else:
                    if self.COST[item] > self.COST[best_node] + self.get_cost(best_node, item):
                        self.COST[item] = self.COST[best_node] +\
                            self.get_cost(best_node, item)
                        g_n_neighbors[item] = self.COST[item]
                        self.PARENT[item] = best_node

            open_list = self.calculate_f_n(g_n_neighbors, open_list)
            open_list.pop(best_node)
        print("visited list : `", self.VISITED)
        print("path : ", self.extract_path())
        return self.extract_path(), self.VISITED
