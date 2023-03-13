import os
current_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.abspath(os.path.join(current_path, '..'))

import numpy as np
import sys
sys.path.insert(0, os.path.abspath(os.path.join(project_path, 'Control')))
from controllers.purepursuit_controller import Purepursuit


def Cruise(vertical_pid, horizontal_pid, truck, speed_limit, nav_line, info):
    vertical_pid.update_e(speed_limit + 4 - truck.speed)
    acc = vertical_pid.get_a() + 0.5
    # horizontal_pid.update_e(float(np.average(nav_line.pts_x[-5:])) - 400)
    # ang = horizontal_pid.get_u() / np.pi + 0.5
    ang = Purepursuit(truck, nav_line.pts)

    # delta_ang = abs(ang - truck.ang)
    # if delta_ang > 0.1 and info.activeAP:
    #     info.AP_exit_reason = 1
    #     info.activeAP = False

    if acc > 1: acc = 1
    elif acc < 0: acc = 0
    return acc, ang