from pybricks.parameters import Stop
from actions import (
    ForewardAction,
    TurnAction,
    WaitAction,
    TogetherAction,
    MotorAction,
    MotorKind,
    MotorMode,
    RepeatAction,
)

steps = [
    TogetherAction(
        ForewardAction(distance=660, speed=500),
        MotorAction(motor=MotorKind.FRONT, degree=395, speed=500, then=Stop.HOLD),
    ),
    # Ready

    # Repeat the hit/return sequence 5 times
    RepeatAction(
        times=5,
        steps=[
            MotorAction(motor=MotorKind.BACK, mode=MotorMode.DC, dc=80, time=200),
            MotorAction(motor=MotorKind.BACK, mode=MotorMode.RUN_TARGET, speed=500, target_angle=0),
        ],
    ),
    # Silo done

    ForewardAction(distance=70, speed=200),
    TurnAction(degree=-24, speed=250, then=Stop.COAST),
    WaitAction(ms=200),
    # Who lived here done

    TurnAction(degree=105, speed=100),
    TurnAction(degree=-65, speed=100),
    TurnAction(degree=65, speed=100),
    # Forge releases

    ForewardAction(distance=120, speed=100),
    # Boulders recovered

    MotorAction(motor=MotorKind.FRONT, degree=60, speed=100),
    MotorAction(motor=MotorKind.FRONT, degree=10, speed=20, then=Stop.HOLD),
    ForewardAction(distance=210, speed=300),
    # Heavy lifting done

    MotorAction(motor=MotorKind.FRONT, degree=-90, speed=100),
    # Lifting the arm

    ForewardAction(distance=-250, speed=300),
    TurnAction(degree=90, speed=200),
    ForewardAction(distance=740, speed=500),
    # Home
]


