import time
import sys
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def bouncing_ball():
    width = 40
    height = 10
    balls = [ '🏀', '🏐', '🎱', '⚾', '🥎', '🏈', '🏉', '🎾', '🥏']  # 10 different balls!
    ball = random.choice(balls)  # Pick a random ball each run
    x = random.randint(1, width-1)
    y = random.randint(1, height-1)
    dx = random.choice([-1, 1])
    dy = random.choice([-1, 1])
    
    try:
        while True:
            clear_screen()
            
            # Update position
            x += dx
            y += dy
            
            # Bounce off walls
            if x <= 0 or x >= width:
                dx = -dx
                ball = random.choice(balls)  # Change ball on wall hit
            if y <= 0 or y >= height:
                dy = -dy
                ball = random.choice(balls)  # Change ball on wall hit
            
            # Draw the ball
            for row in range(height + 1):
                for col in range(width + 1):
                    if row == y and col == x:
                        print(ball, end='')
                    else:
                        print(' ', end='')
                print()
            
            time.sleep(0.05)
    
    except KeyboardInterrupt:
        print("\nAnimation stopped!")
        sys.exit(0)

if __name__ == "__main__":
    print("Multi-Ball Animation - Press Ctrl+C to stop")
    time.sleep(1)
    bouncing_ball()