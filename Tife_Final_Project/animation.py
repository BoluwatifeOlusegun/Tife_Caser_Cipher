#Required Modules for animation
import sys
import time

# ========================================= LOADING ANIMATION =========================================
#Defining a function for animation
def loading_animation():
    # Define the animation characters.
    animation = "|/-\\"
    
    for _ in range(10):  # Repeat the animation 10 times (adjust as needed).
        for char in animation:
            # Print the animation character, overwrite the previous character with '\r'.
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)  # Adjust the sleep duration for the desired speed.
            sys.stdout.write('\r')  # Move the cursor back to the beginning of the line.

# Calling the loading_animation function to display the loading animation.
loading_animation()
print("Loading complete!")

print("\n")
# =========================================================================================================
