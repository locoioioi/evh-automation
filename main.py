import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.utils import is_game_running
from src.executor import Executor

def main():
    print("Evil Hunter Tycoon Automation Start...")
    executor = Executor()
    
    executor.login()
    
    
if __name__ == "__main__":
    main()