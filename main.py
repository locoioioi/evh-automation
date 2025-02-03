import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.utils import *
from src.executor import Executor
import time

def main():
    print("Evil Hunter Tycoon Automation Start...")
    colosseum_path = capture_screenshot("screen5")
    # coords = is_in_screen("./src/image/setting_button.png", colosseum_path)
    # x, y = coords
    # tap(x, y)
    
    executor = Executor()

    # executor.login()
    # time.sleep(2)
    # executor.daily_quest_save_data()
    # time.sleep(2)
    # executor.do_colosseum()
    # time.sleep(2)
    # executor.go_dungeon(15)
    ad_watch = 0
    while ad_watch < 15:
        success = executor.watch_ad()
        if success:
            ad_watch += 1
            print(f"Watching AD {ad_watch}/12")
        time.sleep(20)
    
if __name__ == "__main__":
    main()