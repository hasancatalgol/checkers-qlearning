# --- main.py ---
import pygame
import sys
from config import *
from utils import get_static_obstacles
from game_ui import draw_grid, draw_agents, draw_panel
from agents import RunnerAgent, ChaserQLearningAgent
from rules import is_terminal_state, get_chaser_reward

positions = {"R": (7, 0), "C1": (0, 11), "C2": (0, 12)}
score = {"C1": 0, "C2": 0}
episode = 1
step = 0
reward = 0.0
game_active = False

runner = RunnerAgent()
chaser1 = ChaserQLearningAgent("C1")
chaser2 = ChaserQLearningAgent("C2")
obstacles = get_static_obstacles()

def main():
    global episode, step, reward, game_active
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chaser & Runner Modular")
    clock = pygame.time.Clock()
    button_rect = pygame.Rect(WIDTH - PANEL_WIDTH + 20, 40, 120, 40)

    runner.set_position(positions["R"])
    chaser1.set_position(positions["C1"])
    chaser2.set_position(positions["C2"])

    running = True
    while running:
        screen.fill(WHITE)
        draw_grid(screen, obstacles)

        q_metrics = []

        if game_active:
            step += 1

            runner_pos = runner.move(obstacles)
            positions["R"] = runner_pos

            c1_pos, s1, a1 = chaser1.move(runner_pos, obstacles)
            reward_c1 = get_chaser_reward(c1_pos, runner_pos)
            chaser1.update(s1, a1, reward_c1, chaser1.get_state(runner_pos))
            positions["C1"] = c1_pos

            c2_pos, s2, a2 = chaser2.move(runner_pos, obstacles)
            reward_c2 = get_chaser_reward(c2_pos, runner_pos)
            chaser2.update(s2, a2, reward_c2, chaser2.get_state(runner_pos))
            positions["C2"] = c2_pos

            reward = reward_c1 + reward_c2
            score["C1"] += reward_c1
            score["C2"] += reward_c2

            q_metrics = [
                f"C1 Act: {a1}, Q: {chaser1.q_table.get((s1, a1), 0):.2f}",
                f"C2 Act: {a2}, Q: {chaser2.q_table.get((s2, a2), 0):.2f}",
                f"C1 MaxQ: {max([chaser1.q_table.get((s1, a), 0) for a in chaser1.ACTIONS]):.2f}",
                f"C2 MaxQ: {max([chaser2.q_table.get((s2, a), 0) for a in chaser2.ACTIONS]):.2f}",
                f"Q-Size: {len(chaser1.q_table)}"
            ]

            if is_terminal_state(runner_pos, c1_pos, c2_pos):
                game_active = False

        draw_agents(screen, positions)
        draw_panel(screen, button_rect, episode, step, score, positions, reward, q_metrics)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    step = 0
                    episode += 1
                    reward = 0.0
                    game_active = True
                    positions["R"] = (7, 0)
                    positions["C1"] = (0, 11)
                    positions["C2"] = (0, 12)
                    runner.set_position(positions["R"])
                    chaser1.set_position(positions["C1"])
                    chaser2.set_position(positions["C2"])

        pygame.display.flip()
        clock.tick(5)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
