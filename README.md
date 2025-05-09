# 🧠 Chaser & Runner: Multi-Agent Reinforcement Learning

A simple 8x13 grid-based simulation game with two **chasers (C1, C2)** and one **runner (R)**, where the chasers use **Q-Learning** to learn how to catch the runner. Built with **Python 3.12** and **Pygame**, with modular code organization.

---

## 📦 Features

- ✅ Grid-based game environment with visual board
- ✅ Q-Learning for chasers
- ✅ Manual or random runner control
- ✅ RL metrics and telemetry panel (Q-values, actions, episode/step, etc.)
- ✅ Live reward feedback and terminal condition
- ✅ Q-table export after each episode (as JSON)

---

## 🎮 Game Rules

- Agents move in the order: **Runner → C1 → C2**
- Movement: one cell up/down/left/right or stay
- Black cells are **obstacles**
- **C1/C2 may occupy the same cell**
- The game ends if **R is caught** (i.e. chaser and runner on same cell)

**Scoring per turn:**
- `+2` if distance to R is 1
- `+1` if distance to R is 2
- `−0.1` penalty otherwise

---

## 🗂️ File Structure
CHECKERS-QLEARN/
│
├── agents.py # RL agents (Q-learning chasers, random runner)
├── config.py # Constants and display configuration
├── game_ui.py # Drawing grid, agents, info panel
├── main.py # Game loop + integration
├── rules.py # Game logic rules
├── utils.py # Grid math and obstacle definitions
├── assets/ # Button icons and other visuals
└── requirements.txt # Install dependencies