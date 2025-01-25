import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.utils import is_game_running, capture_screenshot, is_in_screen, tap
from src.executor import Executor

def main():
    print("Evil Hunter Tycoon Automation Start...")
    # colosseum_path = capture_screenshot("colosseum_finish")
    # coords = is_in_screen("./src/image/auto_colosseum_check.png", colosseum_path)
    # x, y = coords
    # tap(x, y)
    
    executor = Executor()
    
    executor.login()
    executor.do_colosseum()
    
    
if __name__ == "__main__":
    main()