import sys
import os
import time
from utils import launch_game, capture_screenshot, is_in_screen, tap, execute_shell_command
import random

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

def access_game() -> bool:
    """
    Wait for the game to load and click on the screen to start the game.
    
    Returns:
        bool: True if the game is loaded and the screen is clicked, False otherwise.
    """
    loading_screen_path = capture_screenshot("loading_screen")
    coords = is_in_screen("./src/image/touch-to-start.png",loading_screen_path)
        
    # Wait for the game to load 
    time.sleep(random.uniform(2, 4))
    
    if coords is None:
        print("failed to login!")
        return False
    
    x, y = coords
    tap(x, y)
    
    execute_shell_command(f"rm {loading_screen_path}", use_adb=False)
    return True

def close_notification() -> bool:
    """
    After the game is loaded, a notification screen will appear. Close the notification screen.
    
    Returns:
        bool: True if the notification is closed, False otherwise.
    """
    notification_screen_path = capture_screenshot("close-notification")
    coords = is_in_screen("./src/image/close-notification-button.png", notification_screen_path)
    
    time.sleep(15)
    if coords is None:
        print("failed to close notification!")
        return False
    
    x, y = coords
    tap(x, y)
    
    execute_shell_command(f"rm {notification_screen_path}", use_adb=False)
    return True