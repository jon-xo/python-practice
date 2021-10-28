# classes_challenge.py

# Robot class

class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0
    
    def __init__(self, motor_speed=0, direction=180, sensor_range=10) -> None:
        
        self.motor_speed = motor_speed
        self.sensor_range = sensor_range
        self.direction = direction
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range





robot_1 = DriveBot()

# robot_1.motor_speed = 5
# robot_1.sensor_range = 10
# robot_1.direction = 90

# Robot logic

# Added control_bot and adjust_sensor methods

robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

#  Enhanced Constructor

# Modified constructor and added parameters

robot_2 = DriveBot(35,75,25)

print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)

# Robot Control

robot_3 = DriveBot(20, 60, 10)

DriveBot.all_disabled = True
DriveBot.latitude = -50.0
DriveBot.longitude = 50

print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)

# Identify Robots

# ------------
# Advanced

# Robot Inheritence

class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed = 0, direction = 180, sensor_range = 10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def __add__(self, num):
        self.speed += num
    
    def __sub__(self, num):
        self.speed -= num

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False

class DriveBot(Robot):
    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        super().__init__(speed=motor_speed, direction=direction, sensor_range=sensor_range)

    def __add__(self, num):
        super().__add__(num)
        self.speed += num
        self.sensor_range += num
    
    def __sub__(self, num):
        super().__sub__(num)
        self.speed -= num
        self.sensor_range -= num

class WalkBot(Robot):
    walk_bot_count = 0
    def __init__(self, steps_per_minute=0, direction=180, sensor_range=10, step_length=5):
        super().__init__(speed=steps_per_minute, direction=direction, sensor_range=sensor_range)
        self.step_length = step_length
        WalkBot.walk_bot_count += 1
        self.walk_id = WalkBot.walk_bot_count
        
        if super().robot_count >= 10 and WalkBot.walk_bot_count >= 5:
            Robot.all_disabled = True


    def adjust_sensor(self, new_sensor_range):
        super().adjust_sensor(new_sensor_range)
        self.obstacle_found = False
        self.step_length = 5

    def avoid_obstacles(self):
        if self.obstacle_found:
            if self.speed <= 60:
                super().avoid_obstacles()
            else:
                if (self.direction + 90) % 360 != 0:
                    self.direction = (self.direction + 90) % 360
                else:
                    self.direction + 90
                self.obstacle_found = False
        self.step_length = self.step_length / 2
        self.speed = self.speed / 2
    
    def __add__(self, num):
        super().__add__(num)
        self.step_length += self.step_length / 2

    def __sub__(self, num):
        super().__sub__(num)
        self.step_length -= self.step_length / 2


robot_1 = DriveBot()
robot_2 = WalkBot()
robot_3 = WalkBot(20, 90, 15, 10)
robot_3.adjust_sensor()

print(robot_2.id)
print(robot_3.step_length)
print(robot_1.speed)


# Prevent a Robot Takeover







