"""
File: project.py
-----------------
The monster tries to catch as many berries as it can and not let them touch the ground,
by moving left or right, following the player's mouse. The aim of this game is to catch
as many berries as you can until three of them touch the ground and the game ends.
"""

from graphics import Canvas
import random
import time

RED_BALL_DIAMETER = 20
BALL_DIAMETER = 30
ANIMATION_DELAY_SECONDS = 0.01
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
MONSTER_HEIGHT = 120
MONSTER_WIDTH = 100


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Final Project")
    canvas.set_canvas_background_color('lightskyblue')
    falling_black_balls = []
    falling_red_balls = []
    monster = create_monster(canvas)
    LIVES = 3
    lives = show_lives(canvas, LIVES)
    SCORE = 0
    score = create_score(canvas, SCORE)
    while LIVES > 0:
        canvas.set_text(score, "Score: " + str(SCORE))
        canvas.set_text(lives, "Lives: " + str(LIVES))
        mouse_x = canvas.get_mouse_x()
        if CANVAS_WIDTH - MONSTER_WIDTH > mouse_x > 0:
            canvas.moveto(monster, mouse_x, CANVAS_HEIGHT - MONSTER_HEIGHT)

        if random.random() < 0.01:
            black_ball = create_black_ball(canvas)
            falling_black_balls.append(black_ball)
        if random.random() < 0.001:
            red_ball = create_red_ball(canvas)
            falling_red_balls.append(red_ball)

        for black_ball in falling_black_balls:
            canvas.move(black_ball, 0, 3)
            if canvas.get_top_y(black_ball) + BALL_DIAMETER > canvas.get_canvas_height():
                falling_black_balls.remove(black_ball)
                canvas.delete(black_ball)
                LIVES -= 1
        for red_ball in falling_red_balls:
            canvas.move(red_ball, 0, 4)
            if canvas.get_top_y(red_ball) + BALL_DIAMETER > canvas.get_canvas_height():
                falling_red_balls.remove(red_ball)
                canvas.delete(red_ball)
                LIVES -= 1

        monster_coords = canvas.coords(monster)
        x_1 = monster_coords[0]
        y_1 = monster_coords[1]
        x_2 = x_1 + MONSTER_WIDTH
        y_2 = y_1 + MONSTER_HEIGHT
        colliding_list = canvas.find_overlapping(x_1, y_1, x_2, y_2)
        for collider in colliding_list:
            if collider == monster:
                pass
            elif collider in falling_black_balls:
                falling_black_balls.remove(collider)
                canvas.delete(collider)
                SCORE += 1
            elif collider in falling_red_balls:
                falling_red_balls.remove(collider)
                canvas.delete(collider)
                SCORE += 2

        canvas.update()
        time.sleep(ANIMATION_DELAY_SECONDS)
    canvas.set_text(lives, "Lives: " + str(LIVES))
    canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, "You Lost!")
    canvas.mainloop()


def create_black_ball(canvas):
    y_coord = 0
    x_coord = random.randint(0, CANVAS_WIDTH - BALL_DIAMETER)
    black_ball = canvas.create_oval(x_coord, y_coord, x_coord + BALL_DIAMETER, y_coord + BALL_DIAMETER)
    canvas.set_fill_color(black_ball, 'black')
    return black_ball


def create_red_ball(canvas):
    y_coord = 0
    x_coord = random.randint(0, CANVAS_WIDTH - BALL_DIAMETER)
    red_ball = canvas.create_oval(x_coord, y_coord, x_coord + BALL_DIAMETER, y_coord + BALL_DIAMETER)
    canvas.set_fill_color(red_ball, 'red')
    canvas.set_outline_color(red_ball, 'red')
    return red_ball


def create_monster(canvas):
    top_x = CANVAS_WIDTH/2 - MONSTER_WIDTH/2
    top_y = CANVAS_HEIGHT - MONSTER_HEIGHT
    monster = canvas.create_image_with_size(top_x, top_y, MONSTER_WIDTH, MONSTER_HEIGHT, 'monster.png')
    return monster


def create_score(canvas, SCORE):
    score = canvas.create_text(40, 30, "Score: " + str(SCORE))
    return score


def show_lives(canvas, LIVES):
    lives = canvas.create_text(40, 60, "Lives: " + str(LIVES))
    return lives


if __name__ == '__main__':
    main()
