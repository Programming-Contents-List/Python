#과제 제출시에 주석처리 꼭 할 것.
# forward = fd() / right = rt() / left= lt()
# dir = right

import turtle
t =turtle.Turtle()
t.shape("turtle")
'''
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

# dir = left
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
'''
#stamp() : 커서 모양 출력

#t.write("거북이(0,0)")
t.stamp()
t.write(t.position())
t.forward(100)
t.stamp()
t.write(t.position())
t.right(90)
t.forward(100)
t.stamp()
t.write(t.position())
t.right(90)
t.forward(100)
t.write(t.position())
t.stamp()
t.right(90)
t.forward(100)
t.write(t.position())
