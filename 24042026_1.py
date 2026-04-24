import time
import random
import threading
import queue

# -------------------------------
# Topic simulation (Publisher/Subscriber)
# -------------------------------
topic = queue.Queue()

def sensor_publisher():
    """Simulates a sensor node publishing distance readings."""
    while True:
        distance = random.randint(10, 50)
        print(f"[Publisher] Distance: {distance} cm")
        topic.put(distance)
        time.sleep(1)

def motor_subscriber():
    """Simulates a motor controller reacting to sensor data."""
    while True:
        if not topic.empty():
            distance = topic.get()
            if distance < 30:
                print(f"[Subscriber] Obstacle at {distance} cm → STOP")
            else:
                print(f"[Subscriber] Clear path ({distance} cm) → MOVE")
        time.sleep(0.5)

# -------------------------------
# Service simulation
# -------------------------------
def add_two_ints_service(a, b):
    """Simulates a ROS2 service that adds two integers."""
    print(f"[Service] Adding {a} + {b}")
    return a + b

def service_client():
    """Client requesting the service."""
    result = add_two_ints_service(5, 7)
    print(f"[Client] Service response: {result}")

# -------------------------------
# Action simulation
# -------------------------------
def move_robot_to_goal(goal):
    """Simulates an action server moving to a goal with feedback."""
    print(f"[Action] Moving to {goal}...")
    for step in range(1, 6):
        print(f"[Action] Progress: {step*20}%")
        time.sleep(1)
    print(f"[Action] Goal {goal} reached!")

def action_client():
    """Client requesting a goal move."""
    move_robot_to_goal("(5,5)")

# -------------------------------
# Main simulation
# -------------------------------
if __name__ == "__main__":
    # Start publisher and subscriber threads
    threading.Thread(target=sensor_publisher, daemon=True).start()
    threading.Thread(target=motor_subscriber, daemon=True).start()

    # Run service and action clients
    time.sleep(3)  # let pub/sub run a bit
    service_client()
    action_client()
