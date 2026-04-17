import tkinter as tk
import random

# Game settings
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
SPEED = 100

# Directions
direction = "Right"

# Initialize window
root = tk.Tk()
root.title("Snake Game")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Snake and food
snake = [(100, 100)]
food = (random.randrange(0, WIDTH, BLOCK_SIZE),
        random.randrange(0, HEIGHT, BLOCK_SIZE))

def draw():
    canvas.delete("all")

    # Draw snake
    for x, y in snake:
        canvas.create_rectangle(x, y, x + BLOCK_SIZE, y + BLOCK_SIZE, fill="green")

    # Draw food
    fx, fy = food
    canvas.create_rectangle(fx, fy, fx + BLOCK_SIZE, fy + BLOCK_SIZE, fill="red")

def move():
    global snake, food

    head_x, head_y = snake[0]

    if direction == "Up":
        head_y -= BLOCK_SIZE
    elif direction == "Down":
        head_y += BLOCK_SIZE
    elif direction == "Left":
        head_x -= BLOCK_SIZE
    elif direction == "Right":
        head_x += BLOCK_SIZE

    new_head = (head_x, head_y)

    # Collision with walls
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        game_over()
        return

    # Collision with self
    if new_head in snake:
        game_over()
        return

    snake.insert(0, new_head)

    # Food collision
    if new_head == food:
        food = (random.randrange(0, WIDTH, BLOCK_SIZE),
                random.randrange(0, HEIGHT, BLOCK_SIZE))
    else:
        snake.pop()

    draw()
    root.after(SPEED, move)

def change_direction(event):
    global direction
    key = event.keysym

    if key == "Up" and direction != "Down":
        direction = "Up"
    elif key == "Down" and direction != "Up":
        direction = "Down"
    elif key == "Left" and direction != "Right":
        direction = "Left"
    elif key == "Right" and direction != "Left":
        direction = "Right"

def game_over():
    canvas.create_text(WIDTH/2, HEIGHT/2, text="GAME OVER", fill="white", font=("Arial", 24))

root.bind("<Key>", change_direction)

draw()
move()

root.mainloop()