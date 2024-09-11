from random import randrange, choice
from turtle import *

from freegames import square, vector

# Definimos la comida, la serpiente, y la dirección en la que se mueve la serpiente
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Lista de colores permitidos (sin incluir rojo)
colors = ['blue', 'green', 'yellow', 'purple', 'orange']

# Elegimos colores diferentes para la serpiente y la comida
snake_color = choice(colors)
food_color = choice([color for color in colors if color != snake_color])

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    """Move food one random step within boundaries."""
    possible_moves = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    move_direction = choice(possible_moves)
    new_position = food + move_direction

    # Aseguramos que la comida no salga de los límites
    if inside(new_position):
        food.move(move_direction)

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        # Reposicionamos la comida aleatoriamente dentro de los límites
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    # Dibujamos el cuerpo de la serpiente
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    # Dibujamos la comida
    square(food.x, food.y, 9, food_color)
    
    update()
    
    # Mover la comida aleatoriamente
    move_food()
    
    # Ajustamos la velocidad de la serpiente
    ontimer(move, 100)

# Configuración inicial de la pantalla
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Asignamos las teclas de dirección para mover la serpiente
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Iniciar el movimiento del juego
move()
done()
