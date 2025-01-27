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
    
    time.sleep(5)
    if coords is None:
        print("failed to close notification!")
        return False
    
    x, y = coords
    tap(x, y)
    
    execute_shell_command(f"rm {notification_screen_path}", use_adb=False)
    return True

def check_attendance() -> bool:
    """
    Check the attendance in the game.
    
    Returns:
        bool: True if the attendance is checked, False otherwise.
    """
    attendance_path = capture_screenshot("attendance")
    coords = is_in_screen("./src/image/login/attendance_button.png", attendance_path)
    
    if coords is None:
        print("Attendance has been checked!")
        execute_shell_command(f"rm {attendance_path}", use_adb=False)
        return False
    
    x, y = coords
    tap(x, y)
    
    execute_shell_command(f"rm {attendance_path}", use_adb=False)
    return True

def check_offline_reward() -> bool:
    """
    Check the offline reward in the game.
    
    Returns:
        bool: True if the offline reward is checked, False otherwise.
    """
    offline_reward_path = capture_screenshot("offline_reward")
    coords = is_in_screen("./src/image/login/get-offline-reward-button.png", offline_reward_path)
    
    if coords is None:
        print("Offline reward has been collected!")
        execute_shell_command(f"rm {offline_reward_path}", use_adb=False)
        return False
    
    x, y = coords
    tap(x, y)
    
    execute_shell_command(f"rm {offline_reward_path}", use_adb=False)
    
    close_reward_path = capture_screenshot("close_reward")
    coords2 = is_in_screen("./src/image/login/close-offline-reward-button.png", close_reward_path)
    
    if coords2 is None:
        print("Close offline reward button not found!")
        return False
    
    x, y = coords2
    tap(x, y)
    execute_shell_command(f"rm {close_reward_path}", use_adb=False)
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
    time.sleep(4)
    
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
        execute_shell_command(f"rm {quest_path}", use_adb=False)
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

def collect_colosseum_reward() -> bool:
    reward_path = capture_screenshot("colosseum_reward")
    coords = is_in_screen("./src/image/colosseum/colosseum_reward.png", reward_path)
    
    if coords != None:
        x, y = coords
        tap(x, y)
        execute_shell_command(f"rm {reward_path}", use_adb=False)
        return True
    
    return False

def start_colosseum_new_season() -> bool:
    check = auto_check()
    if check == False:
        return False
    
    new_season_path = capture_screenshot("new_season_colosseum")
    coords = is_in_screen("./src/image/colosseum/colosseum_new_season_start.png", new_season_path)
    
    if coords is None:
        print("New season button not found!")
        return False
    
    x, y = coords
    tap(x, y)
    execute_shell_command(f"rm {new_season_path}", use_adb=False)
    return True

def end_colosseum_new_season() -> bool:
    start_league_path = capture_screenshot("start_league_colosseum")
    coords = is_in_screen("./src/image/colosseum/start_colosseum_button.png", start_league_path)
    
    if coords is None:
        print("Start league button not found!")
        return False
    
    return True
# ================================================= DUNGEON ===================================================

def access_dungeon() -> bool:
    print("Accessing dungeon...")
    home_path = capture_screenshot("home_screen")
    coords = is_in_screen("./src/image/dungeon/dungeon_btn.png", home_path)
    
    if coords is None:
        print("Dungeon button not found!")
        return False
    
    x, y = coords
    tap(x, y)
    execute_shell_command(f"rm {home_path}", use_adb=False)
    return True 

def start_dungeon() -> bool:
    start_dungeon_path = capture_screenshot("start_dungeon")
    coords = is_in_screen("./src/image/dungeon/dungeon_start.png", start_dungeon_path)
    
    if coords is None:
        print("Start dungeon button not found!")
        return False
    
    x, y = coords
    tap(x, y)
    execute_shell_command(f"rm {start_dungeon_path}", use_adb=False)
    time.sleep(1.3)
    
    select_stage_path = capture_screenshot("select_stage")
    coords2 = is_in_screen("./src/image/dungeon/select_stage.png", select_stage_path)
    
    if coords2 is None:
        print("Select stage button not found!")
        return False
    
    x, y = coords2
    tap(x, y)
    execute_shell_command(f"rm {select_stage_path}", use_adb=False)
    time.sleep(0.5)
    
    enter_dungeon_path = capture_screenshot("enter_dungeon")
    coords3 = is_in_screen("./src/image/dungeon/enter_dungeon.png", enter_dungeon_path)
    
    if coords3 is None:
        print("Enter dungeon button not found!")
        return False
    
    x, y = coords3
    tap(x, y)
    execute_shell_command(f"rm {enter_dungeon_path}", use_adb=False)
    time.sleep(0.5)
    
    for i in range(5):
        index = i + 1
        hunter_path = capture_screenshot(f"select_hunter_{index}")
        coords3 = is_in_screen(f"./src/image/dungeon/hunter_{index}.png", hunter_path)
        
        if coords3 is None:
            print(f"Select hunter {index} button not found!")
            return False
        
        x, y = coords3
        tap(x, y)
        execute_shell_command(f"rm {hunter_path}", use_adb=False)
        
    depart_path = capture_screenshot("depart_dungeon")
    coords4 = is_in_screen("./src/image/dungeon/dungeon_departure.png", depart_path)
    
    if coords4 is None:
        print("Depart dungeon button not found!")
        return False
    
    x, y = coords4
    tap(x, y)
    execute_shell_command(f"rm {depart_path}", use_adb=False)
    return True

def collect_dungeon_reward() -> bool:
    print("Check dungeon reward...")
    while True:
        time.sleep(15)
        dungeon_reward_path = capture_screenshot("dungeon_reward")
        coords = is_in_screen("./src/image/dungeon/dungeon_reward.png", dungeon_reward_path)
        
        if (coords is None):
            continue
        
        print("Collecting dungeon reward...")
        x, y = coords
        tap(x, y)
        execute_shell_command(f"rm {dungeon_reward_path}", use_adb=False)
        
        while True:
            time.sleep(2)
            dungeon_exit = capture_screenshot("dungeon_exit")
            coords2 = is_in_screen("./src/image/dungeon/exit_dungeon.png", dungeon_exit)

            if coords2 is None:
                continue
            
            x, y = coords2
            tap(x, y)
            execute_shell_command(f"rm {dungeon_exit}", use_adb=False)
            break
        
        while True:
            time.sleep(2)
            close_dungeon = capture_screenshot("close_dungeon")
            coords3 = is_in_screen("./src/image/dungeon/close_dungeon_btn.png", close_dungeon)
            
            if coords3 is None:
                continue
            
            x, y = coords3
            tap(x, y)
            execute_shell_command(f"rm {close_dungeon}", use_adb=False)
            break

        return True
    
    
# =================================================WATCH AD===================================================
def find_elf_ad() -> bool:
    print("Detecting ad available...")
    home_path = capture_screenshot("home_screen")
    coords = is_in_screen("./src/image/watch_ad/ad_btn.png", home_path)
    
    if coords is None:
        print("Elf ad button not found!")
        return False
    
    print("Ad is available!")
    x, y = coords
    tap(x, y)
    execute_shell_command(f"rm {home_path}", use_adb=False)
    
    print("Finding the elf ad...")
    while True:
        home_path = capture_screenshot("home_screen")
        coords = is_in_screen("./src/image/watch_ad/ad_elf_1.png", home_path)
        
        if (coords != None):
            x, y = coords
            tap(x, y) 
            print("Elf ad found!")
            execute_shell_command(f"rm {home_path}", use_adb=False)
            break
        
        coords2 = is_in_screen("./src/image/watch_ad/ad_elf_2.png", home_path)
        
        if (coords2 != None):
            x, y = coords2
            tap(x, y)
            print("Elf ad found!")
            execute_shell_command(f"rm {home_path}", use_adb=False)    
            break
            
        coords3 = is_in_screen("./src/image/watch_ad/ad_elf_3.png", home_path)
        
        if (coords3 != None):
            x, y = coords3
            tap(x, y)
            print("Elf ad found!")
            execute_shell_command(f"rm {home_path}", use_adb=False)
            break
    return True
        
        
def watch_ad() -> bool:
    """
    Watch the ad.
    """
    reward_selection_path = capture_screenshot("reward_selection")
    coords = is_in_screen("./src/image/watch_ad/watch_ad_btn.png", reward_selection_path)
    
    if coords is None:
        print("Watch ad button not found!")
        return False
    
    x, y = coords
    tap(x, y)
    execute_shell_command(f"rm {reward_selection_path}", use_adb=False)
    
    while True:
        ad_path = capture_screenshot("ad_screen")
        
        # ad type 1
        coords2 = is_in_screen("./src/image/watch_ad/reward_granted_2.png", ad_path)
        
        if coords2 != None:
            coords3 = is_in_screen("./src/image/watch_ad/close_ad_2.png", ad_path)
            
            if coords3 != None:
                x, y = coords3
                tap(x, y)
                
                execute_shell_command(f"rm {ad_path}", use_adb=False)
                break
        
        # ad type 2
        coords3 = is_in_screen("./src/image/watch_ad/continue_3.png", ad_path)
        
        if coords3 != None:
            x, y = coords3
            tap(x, y)
            
            while True:
                close_ad = capture_screenshot("close_ad")
                coords4 = is_in_screen("./src/image/watch_ad/close_ad_3.png", close_ad)
                
                if coords4 != None:
                    x, y = coords4
                    tap(x, y)
                    
                    execute_shell_command(f"rm {ad_path}", use_adb=False)
                    execute_shell_command(f"rm {close_ad}", use_adb=False)
                    break
                time.sleep(1)

            break
        
        time.sleep(5)
    return True