from pybricks.parameters import Port, Direction, Stop

from bob import Bob

def execute(bob: Bob):
    # R TO L
    bob.foreward(250, 1200)
    bob.turn(-90, 500)
    bob.foreward(1500, 1200)
    bob.foreward(200,200)
    bob.turn(-90,150)
    # bob.arc(radius=-230, angle=90, then=Stop.COAST)
    # bob.foreward_and_front_motor(foreward_distance=240, foreward_speed=250, turn_degree=240, turn_speed=300)
    # for hit in range(6):
    #     bob.turn_front_motor_until_stalled(speed=200, duty_limit=90)
    #     bob.turn_front_motor_dc(dc=-40, time=300)
    # bob.foreward(distance=500, speed=500)
    # return
    # #bob.foreward(100,100)
    # for hit in range(6):
    #     bob.turn_front_motor(-100,150, Stop.COAST)
    #     bob.turn_front_motor(100,150, Stop.COAST) 
    # bob.turn_front_motor(-250,100)
    # bob.foreward(800,300)
    