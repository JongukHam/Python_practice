'''
#클래스 정의 부분

class Car:
    color=""
    speed=0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self,value):
        self.speed -=value

#메인 코드 부분

myCar1=Car()
myCar1.color="빨강"
myCar1.speed=0

myCar2=Car()
myCar2.color="파랑"
myCar2.speed=0

myCar3=Car()
myCar3.color="노랑"
myCar3.speed=0

myCar1.upSpeed(30)
print("자동차1의 색상은 %s 이며, 현재속도는 %d km 입니다."%(myCar1.color,myCar1.speed))

myCar2.upSpeed(60)
print("자동차2의 색상은 %s 이며, 현재속도는 %d km 입니다."%(myCar2.color,myCar2.speed))

myCar3.upSpeed(0)
print("자동차3의 색상은 %s 이며, 현재속도는 %d km 입니다."%(myCar3.color,myCar3.speed))
'''

#매개변수가 없는 생성자 추가

class Car:
    color=""
    speed=0

    
    #매개변수가 없는 생성자
    def __init__(self) :
        self.color ="빨강"
        self.speed = 30

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self,value):
        self.speed -=value

#메인 코드 부분

myCar1=Car()

myCar2=Car()


myCar3=Car()
myCar3.color="파랑"

#자동차 1,2는 색과 속도를 지정해주지 않았기 때문에 생성자가 호출됨
print("자동차1의 색상은 %s 이며, 현재속도는 %d km 입니다."%(myCar1.color,myCar1.speed))

print("자동차2의 색상은 %s 이며, 현재속도는 %d km 입니다."%(myCar2.color,myCar2.speed))
#자동차3만 파란색이된다.
print("자동차3의 색상은 %s 이며, 현재속도는 %d km 입니다."%(myCar3.color,myCar3.speed))

