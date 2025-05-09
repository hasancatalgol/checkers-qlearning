# --- game_ui.py ---
import pygame
from config import *
from utils import coord_to_label, manhattan

pygame.init()
FONT = pygame.font.SysFont("Arial", 24)
BIGFONT = pygame.font.SysFont("Arial", 28)

def draw_grid(screen, obstacles):
    for row in range(ROWS):
        for col in range(COLS):
            y = (ROWS - 1 - row) * CELL_SIZE + MARGIN
            x = col * CELL_SIZE + MARGIN
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            color = BLACK if (row, col) in obstacles else WHITE
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)

    for col in range(COLS):
        label = chr(ord('a') + col)
        x = col * CELL_SIZE + MARGIN + CELL_SIZE // 2 - 10
        screen.blit(FONT.render(label, True, BLACK), (x, 5))
        screen.blit(FONT.render(label, True, BLACK), (x, HEIGHT - MARGIN + 5))

    for row in range(ROWS):
        label = str(row + 1)
        y = (ROWS - 1 - row) * CELL_SIZE + MARGIN + CELL_SIZE // 2 - 10
        screen.blit(FONT.render(label, True, BLACK), (5, y))
        screen.blit(FONT.render(label, True, BLACK), (WIDTH - PANEL_WIDTH + 10, y))

def draw_agents(screen, positions):
    for name, (row, col) in positions.items():
        cx = col * CELL_SIZE + MARGIN + CELL_SIZE // 2
        cy = (ROWS - 1 - row) * CELL_SIZE + MARGIN + CELL_SIZE // 2
        color = GREEN if name == "R" else RED if name == "C1" else BLUE
        pygame.draw.circle(screen, color, (cx, cy), CELL_SIZE // 3)
        label = FONT.render(name, True, WHITE)
        screen.blit(label, label.get_rect(center=(cx, cy)))

def draw_panel(screen, button_rect, episode, step, score, positions, reward, q_metrics=None):
    pygame.draw.rect(screen, GRAY, (WIDTH - PANEL_WIDTH, 0, PANEL_WIDTH, HEIGHT))
    pygame.draw.rect(screen, DARK_GRAY, button_rect)
    screen.blit(BIGFONT.render("Start", True, WHITE), (button_rect.x + 20, button_rect.y + 5))

    info = [
        f"Episode: {episode}",
        f"Step: {step}",
        f"Score C1: {score['C1']:.2f}",
        f"Score C2: {score['C2']:.2f}",
        f"Runner Pos: {coord_to_label(positions['R'])}",
        f"C1 Dist: {manhattan(positions['C1'], positions['R'])}",
        f"C2 Dist: {manhattan(positions['C2'], positions['R'])}",
        f"Reward: {reward:.2f}"
    ]

    y_offset = 150
    for line in info:
        screen.blit(FONT.render(line, True, BLACK), (WIDTH - PANEL_WIDTH + 20, y_offset))
        y_offset += 35

    if q_metrics:
        screen.blit(FONT.render("Q-Learning", True, BLACK), (WIDTH - PANEL_WIDTH + 20, y_offset))
        y_offset += 30
        for line in q_metrics:
            screen.blit(FONT.render(line, True, BLACK), (WIDTH - PANEL_WIDTH + 20, y_offset))
            y_offset += 28