import turtle

WIDTH, HEIGHT = 1600, 900
DIS = turtle.Screen()
DIS.setup(WIDTH, HEIGHT)
DIS.screensize(3*WIDTH, 3*HEIGHT)
DIS.bgcolor("black")
DIS.delay(0)

# Turtle
leo = turtle.Turtle()
leo.pensize(4)
leo.speed(1)
leo.setpos(-WIDTH // 6, HEIGHT // 6) 
leo.color("green")

# L-sistem
gens = 5
axiom = "F++F++F"
chr_1, rule_1 = "F", "F-F++F-F"
step = 60
angle = 60

def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else chr for chr in axiom])

def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom

for gen in range(gens):
    turtle.pencolor("white")
    turtle.goto(-WIDTH // 2 + 60, -HEIGHT // 2 - 100)
    turtle.clear()
    turtle.write(f"gen: {gen}", font=("Arial", 60, "normal"))

    leo.setheading(0)
    leo.goto(0, 0)
    leo.clear()
    
    # axiom = get_result(gens, axiom)
    for chr in axiom:
        if chr == chr_1:
            leo.forward(step)
        elif chr == "+":
            leo.right(angle)
        elif chr == "-":
            leo.left(angle)
    axiom = apply_rules(axiom)
    
DIS.exitonclick()