
def is_valid(state):
    """
    Checks if a given state consists of allowed values
    :param state: the state to be tested as a tuple
    :return: True if the tuple is valid, False otherwise
    """
    if (0 <= state[0] <= 3) and (0 <= state[1] <= 3) and (0 <= state[2] <= 1):  # Check values are valid
        if state[0] == 0 or state[0] >= state[1]:  # No Cowboys or the number of Cowboys <= Robots
            return True
    return False


class Node:
    def __init__(self, c_wrong_side=3, r_wrong_side=3, boat_wrong_side=1, parent=None):
        """
        Creates a node representing a state in the "game" with the given parameters
        :param c_wrong_side: Number of Cowboys on the wrong (left) side (maximum of 3 is allowed in either side)
        :param r_wrong_side: Number of Robots on the wrong (left) side (maximum of 3 is allowed in either side)
        :param boat_wrong_side: Whether the boat is on the wrong (left) side or not (1 - left, 0 - right)
        :param parent: the parent node (used to find the path taken to reach the current state)
        """
        self.state = (c_wrong_side, r_wrong_side, boat_wrong_side)  # Num of m, c, boat side
        self.parent = parent

    def __str__(self):
        """
        Creates the default string representation for a Node
        :return: A String representation of the current node
        """
        return str(self.state)

    def is_goal_state(self):
        """
        Checks whether or not a given node's state is a winning state (0,0,0)
        :return: True if it is a winning condition, False otherwise
        """
        return self.state == (0, 0, 0)

    def __eq__(self, other):
        """
        Compares two Node objects
        :param other: The node to be compared with the current one
        :return: True if the two nodes are equal, False otherwise
        """
        if other is None:
            return False
        for i in range(0, 3):
            if self.state[i] != other.state[i]:  # Check if all values in the states are equal
                return False
        return True  # All values matched

    def get_possible_actions(self):
        """
        Finds all the possible actions for the current node (state)
        :return: A list of all the possible actions
        """
        actions = [(1, 0, 1), (2, 0, 1), (1, 1, 1), (0, 1, 1), (0, 2, 1)]  # List of actions we can do
        possible_actions = []  # List of available (possible) actions
        for action in actions:  # Loop through all actions and check their validity (if they can be done)
            new_state_left = self.get_resulting_state(action)  # Get the wrong side state
            new_c_right = 3 - new_state_left[0]
            new_r_right = 3 - new_state_left[1]
            new_b_right = 1 - new_state_left[2]
            new_state_right = (new_c_right, new_r_right, new_b_right)  # Generate the right side state
            if is_valid(new_state_left) and is_valid(new_state_right):  # Check that both resulting states are valid
                possible_actions.append(action)
        return possible_actions

    def get_resulting_state(self, action):
        """
        Generates the resulting (wrong) state after an action
        :param action: The action to be carried out
        :return: The state after the resulting action
        """
        if self.state[2] == 1:  # Boat is going: left --> right (vector subtraction)
            new_c = self.state[0] - action[0]
            new_r = self.state[1] - action[1]
            new_b = self.state[2] - action[2]
        else:  # Boat is going: left <-- right (vector addition)
            new_c = self.state[0] + action[0]
            new_r = self.state[1] + action[1]
            new_b = self.state[2] + action[2]
        return new_c, new_r, new_b  # Return the resulting values as a tuple (state)

    def get_child_node(self, action):
        """
        Get the resulting node (state and parent) after an action is carried out
        :param action: The action to be carried out
        :return: A Node Object resulting from the action (The current object becomes the child's parent)
        """
        new_state = self.get_resulting_state(action)
        return self.__class__(new_state[0], new_state[1], new_state[2], parent=self)  # Return resulting node
