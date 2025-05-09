# agents.py
import random
import json
from utils import manhattan, get_static_obstacles

ACTIONS = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1),   # Right
    (0, 0)    # Stay
]

class ChaserQLearningAgent:
    ACTIONS = ACTIONS

    def __init__(self, name, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.name = name
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}  # (state, action) -> Q-value
        self.pos = None

    def set_position(self, pos):
        self.pos = pos

    def get_state(self, runner_pos):
        return (self.pos, runner_pos)

    def select_action(self, state, obstacles):
        if random.random() < self.epsilon:
            return random.choice(self.ACTIONS)
        
        q_vals = {action: self.q_table.get((state, action), 0.0) for action in self.ACTIONS}
        best_action = max(q_vals, key=q_vals.get)
        return best_action

    def update(self, state, action, reward, next_state):
        old_q = self.q_table.get((state, action), 0.0)
        next_max = max([self.q_table.get((next_state, a), 0.0) for a in self.ACTIONS])
        new_q = old_q + self.alpha * (reward + self.gamma * next_max - old_q)
        self.q_table[(state, action)] = new_q

    def move(self, runner_pos, obstacles):
        state = self.get_state(runner_pos)
        action = self.select_action(state, obstacles)
        new_pos = (self.pos[0] + action[0], self.pos[1] + action[1])

        if 0 <= new_pos[0] < 8 and 0 <= new_pos[1] < 13 and new_pos not in obstacles:
            self.pos = new_pos
        return self.pos, state, action

    def export_q_table(self, filepath):
        serializable_q = {
            f"{s}|{a}": q for (s, a), q in self.q_table.items()
        }
        with open(filepath, 'w') as f:
            json.dump(serializable_q, f, indent=2)

class RunnerAgent:
    def __init__(self):
        self.pos = None

    def set_position(self, pos):
        self.pos = pos

    def move(self, obstacles):
        valid_moves = [(self.pos[0] + dr, self.pos[1] + dc) for dr, dc in ACTIONS]
        valid_moves = [p for p in valid_moves if 0 <= p[0] < 8 and 0 <= p[1] < 13 and p not in obstacles]
        self.pos = random.choice(valid_moves) if valid_moves else self.pos
        return self.pos