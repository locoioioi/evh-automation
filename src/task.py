import sys
import os
import time
from utils import launch_game, capture_screenshot, is_in_screen, tap, execute_shell_command
import random

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# =================================================LOGIN TASKS===================================================
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
    
    time.sleep(10)
    if coords is None:
        print("failed to close notification!")
        return False
    
    x, y = coords
    tap(x, y)
    
    execute_shell_command(f"rm {notification_screen_path}", use_adb=False)
    return True

# =================================================COLOSSEUM TASKS=================================================== 

def access_colosseum() -> bool:
    colosseum_path = capture_screenshot("colosseum_screen")
    coords = is_in_screen("./src/image/colosseum_button.png", colosseum_path)
    
    if coords is None:
        print("Colosseum button not found!")
        return False
    
    x, y = coords
    tap(x, y)
    execute_shell_command(f"rm {colosseum_path}", use_adb=False)
    return True

def select_league() -> bool:
    league_path = capture_screenshot("league_colosseum_screen")
    coords = is_in_screen("./src/image/select_league_colosseum_button.png", league_path)
    
    if coords is None:
        print("League button not found!")
        return False
    
    x, y = coords
    tap(x, y)
    execute_shell_command(f"rm {league_path}", use_adb=False)
    return True

def auto_check() -> bool:
    colosseum_path = capture_screenshot("colosseum_screen")
    coords = is_in_screen("./src/image/auto_colosseum_check.png", colosseum_path)
    
    if coords is None:
        print("Auto colosseum check button not found!")
        return False

    x, y = coords
    tap(x, y)
    execute_shell_command(f"rm {colosseum_path}", use_adb=False)
    return True

def start_colosseum() -> bool:
    colosseum_path = capture_screenshot("colosseum_screen")
    coords = is_in_screen("./src/image/start_colosseum_button.png", colosseum_path)
    
    if coords is None:
        print("Start colosseum button not found!")
        return False
    
    x, y = coords
    tap(x, y)
    
    execute_shell_command(f"rm {colosseum_path}", use_adb=False)

def complete_colosseum() -> bool:
    colosseum_path = capture_screenshot("colosseum_finish")
    coords = is_in_screen("./src/image/colosseum_finish.png", colosseum_path)
    
    if coords is None:
        print("Colosseum complete button not found!")
        return False
    
    close_button_path = capture_screenshot("close_colosseum")
    coords2 = is_in_screen("./src/image/close_colosseum_button.png", close_button_path)
        
    if coords2 is None:
        print("Close colosseum button not found!")
        return False
    
    x, y = coords2
    tap(x, y)
    
    execute_shell_command(f"rm {close_button_path}", use_adb=False)
    execute_shell_command(f"rm {colosseum_path}", use_adb=False)
    return True