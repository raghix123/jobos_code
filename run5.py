import pybricks

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from bob import Bob

def execute(bob: Bob):

    #yield from bob.turn_front_motor(degree=-45, speed=100)
    # # Ready
    yield from bob.foreward(500,500)

    yield from bob.turn(28, 250)

    yield from bob.run_front_motor_until_stalled(10000, Stop.HOLD, 40)

    yield from bob.turn(-40, 250)

    yield from bob.turn(20, 300)

    yield from bob.foreward(500, 1000)

    yield from bob.arc(2000,-25,1000)
    return
    yield from bob.arc(radius= 310,angle= -75, speed= 80)
    
    yield from bob.run_front_motor_until_stalled(speed=100, then=Stop.HOLD, duty_limit=40)

    return
    yield from bob.foreward(distance=260, speed=200)

    yield from bob.run_front_motor_until_stalled(speed=100, then=Stop.HOLD, duty_limit=40)

    #yield from bob.foreward(distance=35, speed=200)

    yield from bob.turn_front_motor(degree=-100, speed=200)   


    yield from bob.turn(degree=-45, speed=75, then=Stop.BRAKE)
    # Marketwares solved

    yield from bob.foreward(distance=160,speed=100)
    yield from bob.turn(degree=26, speed=100)

    yield from bob.turn_front_motor(degree=60, speed=100)
    yield from bob.turn(degree=-45, speed=75, then=Stop.HOLD)
    wait(500)
    yield from bob.turn(degree=15, speed=75, then=Stop.HOLD)
    # Tip the scales B done

    yield from bob.foreward(distance=400, speed=800)
    yield from bob.turn(-20,60)
    yield from bob.foreward(650,800)
    # # Back home
    return
    yield from bob.arc(radius= 1400,angle=15,speed=100)
    # yield from bob.turn(degree=45, speed=75, then=Stop.BRAKE)
    # yield from bob.foreward(distance=-100,speed=100)
    # yield from bob.turn(degree=-45, speed=75, then=Stop.BRAKE)
    # yield from bob.foreward(distance=365, speed=200)
    yield from bob.turn_back_motor(degree=-300, speed=1000)
    yield from bob.turn_back_motor(degree=300, speed=1000)
    # Tip the scales A done

    yield from bob.foreward(distance=-210, speed=200)
    yield from bob.turn(degree=32, speed=75, then=Stop.BRAKE)
    yield from bob.turn_front_motor(degree=60, speed=100)
    yield from bob.turn(degree=-45, speed=75, then=Stop.HOLD)
    wait(500)
    # Tip the scales B done

    # yield from bob.foreward(distance=400, speed=800)
    # yield from bob.arc(radius=-1500, angle= 60, speed= 800, then= Stop.COAST)
    # # Back home
    
