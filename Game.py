import Node


class Game:
    def __init__(self):
        self.initial_node = Node.Node()

    def breadth_first_search(self):
        frontier = [self.initial_node]  # Queue
        explored = []
        generated = 0  # Keeps track of how many states we generated

        current_state = frontier.pop(0)  # Dequeue first element from queue
        while not current_state.is_goal_state():
            explored.append(current_state)  # Add the current element to the explored list
            print("Exploring: ", current_state)
            actions = current_state.get_possible_actions()  # Get all possible actions
            for action in actions:
                generated += 1
                new_state = current_state.get_child_node(action)
                if new_state not in explored and new_state not in frontier and new_state is not None:
                    frontier.append(
                        new_state)  # If the action is not in the explored list or already in the frontier, add it

            if len(frontier) == 0:  # If the frontier is empty, return failure - no solution
                print("No solution found")
                return None

            current_state = frontier.pop(0)  # Move on to the next state

        print("Solution found!")
        print(f"Explored {len(explored)} states")  # Number of explored states
        print(f"Generated {generated} states, \n")  # Number of states we generated
        # Generate the successful path:
        final_path = []
        while current_state is not None:
            final_path.append(current_state)
            current_state = current_state.parent
        for state in reversed(final_path):
            print("Exploring: ", state)

        return final_path[0]


if __name__ == '__main__':
    g = Game()
    goal_node = g.breadth_first_search()
    print("The goal node is ", goal_node)
