import math
from controller import Robot

TIME_STEP = 16

robot = Robot()

timestep = int(robot.getBasicTimeStep())

steering = [
    robot.getDevice('left_steer'),
    robot.getDevice('right_steer')
]

wheels = [
    robot.getDevice('rear_right_wheel'),
    robot.getDevice('rear_left_wheel'),
    robot.getDevice('front_right_wheel'),
    robot.getDevice('front_left_wheel')
]


def wheel_set_speed(wheel, speed):
    if speed >= 0.0:
        wheel.setPosition(float('inf'))
        wheel.setVelocity(speed)
    else:
        wheel.setPosition(-float('inf'))
        wheel.setVelocity(-speed)


def wheels_set_speed(speed):
    for wheel in wheels:
        wheel_set_speed(wheel, speed)


wheels_set_speed(2.0)

time = 0.0
while robot.step(timestep) != -1:
    time += timestep / 1000.0

    direction = 0.5 * math.sin(time)
    steering[0].setPosition(direction)
    steering[1].setPosition(direction)

    pass
