import turtle

# Set up the Turtle environment
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("white")
t.color("brown")


def draw_tree(branch_length, level):
    if level > 0:
        # Draw the base of the current branch
        t.forward(branch_length)

        # Draw right subtree
        t.right(45)
        draw_tree(branch_length * 0.707, level - 1)

        # Reset angle and draw left subtree
        t.left(90)
        draw_tree(branch_length * 0.707, level - 1)

        # Reset angle and go back to the base of the branch
        t.right(45)
        t.backward(branch_length)


# Function to initialize drawing
def init_tree(level):
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)
    draw_tree(100, level)


# Main program to draw the tree
if __name__ == "__main__":
    recursion_level = int(input("Enter the recursion level: "))
    init_tree(recursion_level)
    turtle.done()
