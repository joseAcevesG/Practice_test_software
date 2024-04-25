import time


def perform_action_based_on_time():
    current_time = time.time()
    if current_time < 10:
        return "Action A"
    else:
        return "Action B"
