from turtle import *

bgcolor('yellow')
speed(10)
width(5)
right(90)

for i in range(2):
    fillcolor('green')
    begin_fill()

    for i in range(3):
        for i in range(6):
            forward(100)
            left(60)
        left(120)
    right(60)
end_fill()
mainloop()
