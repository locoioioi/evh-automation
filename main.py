import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.utils import is_game_running, capture_screenshot, is_in_screen, tap
from src.executor import Executor
import time

def main():
    print("Evil Hunter Tycoon Automation Start...")
    # colosseum_path = capture_screenshot("screen")
    # coords = is_in_screen("./src/image/setting_button.png", colosseum_path)
    # x, y = coords
    # tap(x, y)
    
    executor = Executor()
    
    executor.login()
    # time.sleep(2)
    # executor.daily_quest_save_data()
    time.sleep(2)
    # executor.do_colosseum()
    # time.sleep(2)
    # executor.go_dungeon(15)
    executor.watch_ad()
    
    
if __name__ == "__main__":
    main()