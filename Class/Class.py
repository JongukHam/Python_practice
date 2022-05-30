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
'''
'''
#매개변수가 있는 생성자 추가
class Car:
    color=""
    speed=0

    
    #매개변수(value1,~2)가 있는 생성자
    def __init__(self,value1,value2) :
        self.color = value1
        self.speed = value2


#메인 코드 부분

myCar1=Car("빨강",10)

myCar2=Car("파랑",20)

myCar3=Car("노랑",30)



print("자동차1의 색상은 %s 이며, 현재속도는 %d km 입니다."%(myCar1.color,myCar1.speed))

print("자동차2의 색상은 %s 이며, 현재속도는 %d km 입니다."%(myCar2.color,myCar2.speed))

print("자동차3의 색상은 %s 이며, 현재속도는 %d km 입니다."%(myCar3.color,myCar3.speed))
'''
'''
#클래스 선언
class Car :
    color="" #인스턴스 변수
    speed=0 #인스턴스 변수
    count=0 #클래스 변수

    def __init__(self) :
        self.speed=0
        Car.count +=1 #인스턴스가 생성 될 때마다 생성된 인스턴스(차)의 갯수를 세어 줌

#변수 선언
myCar1,myCar2 = None, None

#메인 코드 부분

myCar1=Car()
myCar1.speed=30
print("자동차1의 현재 속도는 %dkm, 생산된 자동차 숫자는 총 %d대입니다."%(myCar1.speed, Car.count))

myCar2=Car()
myCar2.speed=60
print("자동차1의 현재 속도는 %dkm, 생산된 자동차 숫자는 총 %d대입니다."%(myCar2.speed, Car.count))
'''
'''

#클래스 상속

class Car:
    speed=0

    def upSpeed(self,value):
        self.speed = self.speed+value

    def downSpeed(self,value):
        self.speed=self.speed-value

class Sedan(Car) : #상속
    seatNum=0

    def getSeatNum(self) :
        return self.seatNum

class Truck(Car) :
    capacity=0

    def getCapacity(self):
        return self.capacity

sedan1, truck1 = None,None

sedan1=Sedan()
truck1=Truck()

sedan1.upSpeed(100)
truck1.upSpeed(80)

sedan1.seatNum=5
truck1.capacity=50

print("승용차의 속도는 %d km, 좌석수는 %d개입니다."%(sedan1.speed,sedan1.getSeatNum()))
print("트럭의 속도는 %d km, 총중량은 %d톤입니다."%(truck1.speed,truck1.getCapacity()))
'''

#오버라이딩


class Car:
    speed=0

    def upSpeed(self,value):
        self.speed = self.speed+value

        print("현재 속도(슈퍼 클래스) : %d" %self.speed)

class Sedan(Car) : 
    def upSpeed(self,value):
        self.speed +=value

        if self.speed>150:
            self.speed=150

        print("현재 속도(서브 클래스) : %d" %self.speed)

class Truck(Car):
    pass

sedan1,truck1 = None,None

truck1=Truck()
sedan1=Sedan()

print("트럭 -->", end="")
truck1.upSpeed(200)

print("승용차 -->", end="")
sedan1.upSpeed(200)


        
