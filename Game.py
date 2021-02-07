import Node


def generate_final_path(node):
    final_path = []
    while node is not None:
        final_path.append(node)
        node = node.parent
    return final_path


def print_path(path, reverse=False, spec_char=""):
    if reverse:
        path = reversed(path)
    for node in path:
        print(spec_char + "Exploring: ", node)


class Game:
    def __init__(self):
        """

        """
        self.initial_node = Node.Node()

    def breadth_first_search(self):
        """

        :return:
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

        return generate_final_path(current_state)

    def depth_first_search(self):
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

        return generate_final_path(current_state)


if __name__ == '__main__':
    g = Game()
    print("Breadth-First Search:")
    path = g.breadth_first_search()
    print_path(path, True, "\t")
    print("\nDepth-First Search: ")
    path = g.depth_first_search()
    print_path(path, True, "\t")
