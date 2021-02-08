import Node


def generate_final_path(node):
    """
    Generate the path taken to reach the destination. Makes use of the node's parent attribute to find the path.
    :param node: The destination node
    :return: The path taken from the source to reach the destination, as a list of nodes.
    """
    final_path = []
    while node is not None:
        final_path.append(node)  # Add the current node to the list
        node = node.parent  # Move to parent node
    return final_path


def print_path(path, spec_char=""):
    """
    Print the path taken to reach a node.
    :param path: List of the nodes leading to the destination
    :param spec_char: Special character added at the beginning of prints (for better structuring of output)
    :return: None
    """
    for node in path:  # Loop through each node in the path and print it
        print(spec_char + "Exploring: ", node)


class Game:
    def __init__(self):
        """
        Creates a default Node object - the starting state condition
        """
        self.initial_node = Node.Node()

    def breadth_first_search(self):
        """
        Uses the Breadth-First Search algorithm to find a solution to the problem.
        :return: The path taken to reach the solution if it exists (in the form of a list), None otherwise
        """
        frontier = [self.initial_node]  # Queue
        explored = []
        generated = 0  # Keeps track of how many states we generated

        current_state = frontier.pop(0)  # Dequeue first element from queue
        while not current_state.is_goal_state():
            explored.append(current_state)  # Add the current element to the explored list
            actions = current_state.get_possible_actions()  # Get all possible actions
            for action in actions:
                generated += 1
                new_state = current_state.get_child_node(action)
                if new_state not in explored and new_state not in frontier and new_state is not None:
                    frontier.append(new_state)  # If the action is not in the explored list or already in the frontier, add it

            if len(frontier) == 0:  # If the frontier is empty, return failure - no solution
                print("No solution found")
                return None

            current_state = frontier.pop(0)  # Move on to the next state

        print("Solution found! " + f"Explored {len(explored)} states. " + f"Generated {generated} states")

        return reversed(generate_final_path(current_state))  # Return the final path taken to reach the destination

    def depth_first_search(self):
        """
        Uses the Depth-First Search algorithm to find a solution to the problem.
        :return: The path taken to reach the solution if it exists (in the form of a list), None otherwise
        """
        frontier = [self.initial_node]  # Stack
        explored = []
        generated = 0  # Keeps track of how many states we generated

        current_state = frontier.pop()  # Pop element from the stack
        while not current_state.is_goal_state():
            explored.append(current_state)  # Add the current element to the explored list
            actions = current_state.get_possible_actions()  # Get all possible actions
            for action in actions:
                generated += 1
                new_state = current_state.get_child_node(action)
                if new_state not in explored and new_state not in frontier and new_state is not None:
                    frontier.append(new_state)  # If the action is not in the explored list or already in the frontier, add it

            if len(frontier) == 0:  # If the frontier is empty, return failure - no solution
                print("No solution found")
                return None

            current_state = frontier.pop()  # Move on to the next state

        print("Solution found! " + f"Explored {len(explored)} states. " + f"Generated {generated} states")

        return reversed(generate_final_path(current_state))  # Return the final path taken to reach the destination

    def depth_limited_search(self, current_state, depth=0):
        """
        Uses Depth-limited Search algorithm to find a solution to the problem, in the given depth.
        :param current_state: The node to start searching from (source)
        :param depth: The depth limit for the current search (searches up to the depth value)
        :return: The goal state, if it exists in the given depth, None otherwise
        """
        if current_state.is_goal_state():
            return current_state  # The current state is a goal state (destination)

        if depth <= 0:  # Check to see if we reached the maximum depth
            return None

        actions = current_state.get_possible_actions()
        for action in actions:
            new_state = self.depth_limited_search(current_state.get_child_node(action), depth - 1)  # Repeat until depth (limit) reaches 0
            if new_state is not None:
                return new_state  # If the generated state is a goal state, return it

        return None

    def iterative_deepening_search(self):
        """
         Uses the Depth-First Search algorithm to find an optimal solution to the problem.
        :return: The path taken to reach an optimal solution if it exists (in the form of a list), None otherwise
        """
        for max_depth in range(12):  # An optimal solution to the problem takes 11 moves
            state = self.depth_limited_search(self.initial_node, max_depth)  # Use depth-limited search with the current max depth (limit)
            if state is not None:  # Then a solution was found
                print("Solution found!")
                return reversed(generate_final_path(state))  # Return the final path taken to reach the destination

        print("No solution at given cutoff!")

        return None


if __name__ == '__main__':
    g = Game()
    print("Breadth-First Search:")
    path = g.breadth_first_search()
    print_path(path, "\t")
    print("\nDepth-First Search: ")
    path = g.depth_first_search()
    print_path(path, "\t")
    print("\nIterative Deepening (Depth-First) Search:")
    path = g.iterative_deepening_search()
    print_path(path, "\t")
