def is_valid(state):
    if (0 <= state[0] <= 3) and (0 <= state[1] <= 3) and (0 <= state[2] <= 1):  # Check values are valid
        if state[0] == 0 or state[0] >= state[1]:
            # No missionaries or the number of missionaries is greater than or equal to cannibals
            return True
    return False


class Node:
    def __init__(self, m_wrong_side=3, c_wrong_side=3, boat_wrong_side=1, parent=None):
        self.state = (m_wrong_side, c_wrong_side, boat_wrong_side)  # Num of m, c, boat side
        self.parent = parent

    def __str__(self):
        return str(self.state)

    def is_goal_state(self):
        return self.state == (0, 0, 0)

    def __eq__(self, other):
        if other is None:
            return False
        for i in range(0, 3):
            if self.state[i] != other.state[i]:
                return False
        return True

    def get_possible_actions(self):
        """""
        move one M (1,0,1): do - to go from left to right and + tp gp from right to left
        move two M (2,0,1): do - to go right and + to go left
        move one M and one C (1,1,1): do - to go right and + to go left
        move one C (0,1,1)
        move two C (0,2,1)
        """""
        actions = [(1, 0, 1), (2, 0, 1), (1, 1, 1), (0, 1, 1), (0, 2, 1)]
        possible_actions = []
        for action in actions:
            new_state_left = self.get_resulting_state(action)
            new_m_right = 3 - new_state_left[0]
            new_c_right = 3 - new_state_left[1]
            new_b_right = 1 - new_state_left[2]
            new_state_right = (new_m_right, new_c_right, new_b_right)
            if is_valid(new_state_left) and is_valid(new_state_right):  # Check both the left and right banks
                possible_actions.append(action)
        return possible_actions

    def get_resulting_state(self, action):
        if self.state[2] == 1:
            new_m = self.state[0] - action[0]
            new_c = self.state[1] - action[1]
            new_b = self.state[2] - action[2]
        else:
            new_m = self.state[0] + action[0]
            new_c = self.state[1] + action[1]
            new_b = self.state[2] + action[2]
        return new_m, new_c, new_b

    def get_child_node(self, action):
        new_state = self.get_resulting_state(action)
        return self.__class__(new_state[0], new_state[1], new_state[2], parent=self)  # Return resulting node (Node after the action)
