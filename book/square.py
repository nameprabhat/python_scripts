
import turtle
poke=turtle.Turtle()
poke.shape('turtle')
poke.color('red')


poke1=turtle.Turtle()
poke1.shape('turtle')
poke1.color('green')


def create_square(para1):
    for i in range(4):
        para1.forward(100)
        para1.right(90)
        
def create_spiral(para):
    for i in range(6):
        create_square(para)
        para.right(90)

#create_square(poke)
#poke1.right(45)
#create_square(poke1)

create_spiral(poke)
poke1.right(50)
create_spiral(poke1)



###print('length of square is',length)
turtle.mainloop()




    
