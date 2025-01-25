
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.utils import is_game_running, capture_screenshot, tap
from src.task import launch_game, access_game, is_in_screen, close_notification
import time

class Executor:
    def __init__(self):
        self.is_login = is_game_running()
        self.attendance = False
        self.close_notification = False
        self.offline_reward = False
    
        # Task flags
        self.colosseum = False
        self.world_boss = False
        self.watching_ad = False
        self.daily_quest = False
        self.tmv = False
        self.dungeon = False
        self.field_boss = False
        
    def login(self):
        """
        Open Evil Hunter Tycoon on LDPlayer using ADB.
        """
        launch_game()
        
        while self.is_login == False:
            self.is_login = access_game()
            
            if self.is_login == False:
                continue
            
            while self.close_notification == False:
                self.close_notification = close_notification()
                
                if self.close_notification == False:
                    continue
                
                print("Login Success!")
        
    def do_colosseum(self):
        """
        Execute the colosseum task.
        """
        