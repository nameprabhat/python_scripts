import turtle
poke=turtle.Turtle()
poke.shape('turtle')
poke.color('red')


def create_shape(para1):
    for i in range(5):
        para1.forward(100)
        para1.right(144)


create_shape(poke)





###print('length of square is',length)
turtle.mainloop()
