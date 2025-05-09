# rules.py

def is_terminal_state(runner_pos, c1_pos, c2_pos):
    return runner_pos == c1_pos or runner_pos == c2_pos

def get_chaser_reward(chaser_pos, runner_pos):
    dist = abs(chaser_pos[0] - runner_pos[0]) + abs(chaser_pos[1] - runner_pos[1])
    if dist == 1:
        return 2.0
    elif dist == 2:
        return 1.0
    return -0.1

def get_valid_actions(pos, obstacles):
    ROWS, COLS = 8, 13
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (0, 0)]
    valid = []
    for dr, dc in directions:
        new_pos = (pos[0] + dr, pos[1] + dc)
        if 0 <= new_pos[0] < ROWS and 0 <= new_pos[1] < COLS and new_pos not in obstacles:
            valid.append(new_pos)
    return valid