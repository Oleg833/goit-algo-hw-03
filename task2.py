import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)

def draw_complete_snowflake(turtle, order, size):
    for _ in range(3):
        koch_snowflake(turtle, order, size)
        turtle.right(120)

def main():
    try:
        recursion_level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.color("blue")
    snowflake_turtle.width(2)
    snowflake_turtle.speed(7)

    snowflake_turtle.penup()
    snowflake_turtle.goto(-300, 180)
    snowflake_turtle.pendown()

    draw_complete_snowflake(snowflake_turtle, recursion_level, 150*recursion_level)

    window.exitonclick()

if __name__ == "__main__":
    main()
