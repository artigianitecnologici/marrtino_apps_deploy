from robot_cmd_ros import *


begin(use_desired_cmd_vel=True)

enableObstacleAvoidance(True)

forward(1)

enableObstacleAvoidance(False)

end()
