from shapes import Paper, Triangle, Rectangle, Oval

paper = Paper()
rect1 = Rectangle()
rect2 = Rectangle()
ov = Oval()
tri = Triangle(300,150,650,120,300,60)

rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")

rect2.set_width(50)
rect2.set_height(150)
rect2.set_color("yellow")
rect2.set_x(100)
rect2.set_y(100)

ov.set_width(50)
ov.set_height(150)
ov.set_color("red")
ov.randomize(125, 240)

tri.set_color("green")





rect1.draw()
rect2.draw()
ov.draw()
tri.draw()
paper.display()
