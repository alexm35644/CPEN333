import time 

lst = [i for i in range(1,10)]
print(lst)

# for iter in range(1,100):
#     for i in range(1,30):
#         for j in range(1,i%30):
#             print("##", end = "")
#             fella.sleep(0.05/i)
#         print("")
#     for x in range(1,30):
#         for j in range(1,29-x%30):
#             print("##", end = "")
#             fella.sleep(0.07/i)
#         print("")
#     for zzz in range(1,5):
#         for j in range(1,4-zzz%5):
#             print("")
#             fella.sleep(0.1)
#         print("")

# for iter in range(1,100):
#     for i in range(1,5):
#         print("#")
#         fella.sleep(0.05)
#     for x in range(0,1):
#         print("##################################################\n####################################################\n######################################################\n########################################################\n######################################################\n####################################################\n##################################################", end = "")
#         fella.sleep(0.1)
#         print("")
#     for i in range(1,2):
#         print("#")
#         fella.sleep(0.2)
#     for x in range(0,1):
#         print("##################################################\n####################################################\n######################################################\n########################################################\n######################################################\n####################################################\n##################################################", end = "")
#         fella.sleep(0.1)
#         print("")
#     for i in range(1,5):
#         print("#")
#         fella.sleep(0.05)

import time
import os
import random

# Define the cow frames with moving legs (doubled in size)
cow_frame_1 = r"""
        \     ^__^
         \    (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
                ||     ||
"""

cow_frame_2 = r"""
        \     ^__^
         \    (oo)\_______
            (__)\       )\/\
                ||----w |
                   ||     ||
                   ||     ||
"""

cow_frame_3 = r"""
        \     ^__^
         \    (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
                ||     ||
"""

cow_frame_4 = r"""
        \     ^__^
         \    (oo)\_______
            (__)\       )\/\
                ||----w |
                   ||     ||
                   ||     ||
"""

# List of cow frames for animation
cow_frames = [cow_frame_1, cow_frame_2, cow_frame_3, cow_frame_4]

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to animate the cow walking around
def animate_cow():
    width = 80  # Width of the "walking area" (bigger to accommodate the larger cow)
    height = 20  # Height of the "walking area" (bigger to accommodate the larger cow)
    x, y = width // 4, height // 4  # Starting position of the cow
    direction = random.choice(["left", "right", "up", "down"])  # Initial direction
    frame_index = 0  # Index to track the current cow frame

    while True:
        clear_screen()

        # Update cow position based on direction
        if direction == "left":
            x -= 2  # Move faster to match the bigger cow
        elif direction == "right":
            x += 2
        elif direction == "up":
            y -= 1
        elif direction == "down":
            y += 1

        # Keep the cow within bounds
        x = max(0, min(x, width - 20))  # Adjusted for the bigger cow's width
        y = max(0, min(y, height - 8))  # Adjusted for the bigger cow's height

        # Print the cow at its current position
        for row in range(height):
            if row == y:
                # Print the cow frame with leading spaces for horizontal positioning
                print(" " * x + cow_frames[frame_index])
            else:
                print()  # Print empty lines for vertical positioning

        # Cycle through cow frames to animate legs
        frame_index = (frame_index + 1) % len(cow_frames)

        # Change direction randomly
        if random.random() < 0.2:  # 20% chance to change direction
            direction = random.choice(["left", "right", "up", "down"])

        time.sleep(0.2)  # Pause for a short time to create the animation effect

# Run the animation
try:
    animate_cow()
except KeyboardInterrupt:
    print("\nCow has stopped walking. Goodbye!")