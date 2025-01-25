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
    coords = is_in_screen("./src/image/login/touch-to-start.png",loading_screen_path)
        
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
    coords = is_in_screen("./src/image/login/close-notification-button.png", notification_screen_path)
    
    time.sleep(10)
    if coords is None:
        print("failed to close notification!")
        return False
    
    x, y = coords
    tap(x, y)
    
    execute_shell_command(f"rm {notification_screen_path}", use_adb=False)
    return True

# =================================================DAILY TASKS===================================================

def access_setting() -> bool:
    """
    Save the data to cloud.
    """    
    home_path = capture_screenshot("home_screen")
    coords = is_in_screen("./src/image/daily_task/setting_button.png", home_path)
    
    if coords is None:
        print("Setting button not found!")
        return False
    
    x, y = coords
    tap(x, y)
    execute_shell_command(f"rm {home_path}", use_adb=False)
    return True

def save_data() -> bool:
    """
    Process all the steps to save the data to the cloud.
    Including: Open setting, choose save to google, choose google account, close setting.
    
    Returns:
        bool: True if the data is saved to the cloud, False otherwise.
    """
    # Open setting
    save_to_cloud_path = capture_screenshot("save_data")
    coords = is_in_screen("./src/image/daily_task/save_to_cloud.png", save_to_cloud_path)
    
    if coords is None:
        print("Save to cloud button not found!")
        return False
    
    x, y = coords
    tap(x, y)
    execute_shell_command(f"rm {save_to_cloud_path}", use_adb=False)
    time.sleep(0.5)
    
    # Save to google
    save_to_google_path = capture_screenshot("save_data_google")
    coords2 = is_in_screen("./src/image/daily_task/save_to_google.png", save_to_google_path)
    
    time.sleep(1)
    if coords2 is None:
        print("Save to google button not found!")
        return False
    
    x, y = coords2
    tap(x, y)
    execute_shell_command(f"rm {save_to_google_path}", use_adb=False)
    time.sleep(2)
    
    # Choose google account
    save_to_google_account_path = capture_screenshot("save_data_google_account")
    coords3 = is_in_screen("./src/image/daily_task/google_account.png", save_to_google_account_path)
    
    if coords3 is None:
        print("Google account button not found!")
        return False
    
    x, y = coords3
    tap(x, y)
    execute_shell_command(f"rm {save_to_google_account_path}", use_adb=False)
    time.sleep(2.5)
    
    # Close setting
    close_setting_path = capture_screenshot("close_setting")
    coords4 = is_in_screen("./src/image/daily_task/close_setting_button.png", close_setting_path)
    
    if coords4 is None:
        print("Close setting button not found!")
        return False
    
    x, y = coords4
    tap(x, y)
    
    execute_shell_command(f"rm {close_setting_path}", use_adb=False)
    return True

def collect_reward() -> bool:
    home_path = capture_screenshot("home_screen")
    coords = is_in_screen("./src/image/daily_task/daily_quest_button.png", home_path)
    
    if coords is None:
        print("Collect reward button not found!")
        return False
    
    x, y = coords
    tap(x, y)
    execute_shell_command(f"rm {home_path}", use_adb=False)
    
    time.sleep(0.5)
    quest_path = capture_screenshot("quest_screen")
    coords2 = is_in_screen("./src/image/daily_task/get_reward_save.png", quest_path)
    coords3 = is_in_screen("./src/image/daily_task/quest_screen_close.png", quest_path)
    
    if coords2 is None:
        print("Already collected reward!")
        x, y = coords3
        tap(x, y)
        return False
    
    x, y = coords2
    tap(x, y)
    
    time.sleep(0.5)    
    if coords3 is None:
        print("Close quest button not found!")
        return False
    
    x, y = coords3
    tap(x, y)
    
    execute_shell_command(f"rm {quest_path}", use_adb=False)
    return True

# =================================================COLOSSEUM TASKS=================================================== 

def access_colosseum() -> bool:
    colosseum_path = capture_screenshot("colosseum_screen")
    coords = is_in_screen("./src/image/colosseum/colosseum_button.png", colosseum_path)
    
    if coords is None:
        print("Colosseum button not found!")
        return False
    
    x, y = coords
    tap(x, y)
    execute_shell_command(f"rm {colosseum_path}", use_adb=False)
    return True

def select_league() -> bool:
    league_path = capture_screenshot("league_colosseum_screen")
    coords = is_in_screen("./src/image/colosseum/select_league_colosseum_button.png", league_path)
    
    if coords is None:
        print("League button not found!")
        return False
    
    x, y = coords
    tap(x, y)
    execute_shell_command(f"rm {league_path}", use_adb=False)
    return True

def auto_check() -> bool:
    colosseum_path = capture_screenshot("colosseum_screen")
    coords = is_in_screen("./src/image/colosseum/auto_colosseum_check.png", colosseum_path)
    
    if coords is None:
        print("Auto colosseum check button not found!")
        return False

    x, y = coords
    tap(x, y)
    execute_shell_command(f"rm {colosseum_path}", use_adb=False)
    return True

def start_colosseum() -> bool:
    colosseum_path = capture_screenshot("colosseum_screen")
    coords = is_in_screen("./src/image/colosseum/start_colosseum_button.png", colosseum_path)
    
    if coords is None:
        print("Start colosseum button not found!")
        return False
    
    x, y = coords
    tap(x, y)
    
    execute_shell_command(f"rm {colosseum_path}", use_adb=False)

def complete_colosseum() -> bool:
    colosseum_path = capture_screenshot("colosseum_finish")
    coords = is_in_screen("./src/image/colosseum/colosseum_finish.png", colosseum_path)
    
    if coords is None:
        print("Colosseum complete button not found!")
        return False
    
    close_button_path = capture_screenshot("close_colosseum")
    coords2 = is_in_screen("./src/image/colosseum/close_colosseum_button.png", close_button_path)
        
    if coords2 is None:
        print("Close colosseum button not found!")
        return False
    
    x, y = coords2
    tap(x, y)
    
    execute_shell_command(f"rm {close_button_path}", use_adb=False)
    execute_shell_command(f"rm {colosseum_path}", use_adb=False)
    return True