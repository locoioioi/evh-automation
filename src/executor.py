
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.utils import is_game_running, capture_screenshot, tap
from src.task import launch_game, access_game, is_in_screen, close_notification, access_colosseum, select_league, auto_check, start_colosseum
from src.task import complete_colosseum, access_setting, save_data, collect_reward
import time

class Executor:
    def __init__(self):
        self.is_login = is_game_running()
        self.attendance = False
        self.close_notification = False
        self.offline_reward = False
        self.daily_quest = False
    
        # Task flags
        self.colosseum = False
        self.world_boss = False
        self.watching_ad = False
        self.tmv = False
        self.dungeon = False
        self.field_boss = False
        
    def login(self):
        """
        Open Evil Hunter Tycoon on LDPlayer using ADB.
        """
        # TODO: Implement attendance check.
        # TODO: offline reward check.
        launch_game()
        
        while self.is_login == False:
            self.is_login = access_game()
            
            if self.is_login == False:
                continue
            
            while self.close_notification == False:
                self.close_notification = close_notification()
                
                if self.close_notification == False:
                    continue
                
        self.is_login = is_game_running()
        print("Login Success!")
        
    def do_colosseum(self):
        """
        Execute the colosseum task.
        """
        
        # TODO: Handle collect reward.
        # TODO: Handle start new season.
        access_colosseum() 
        time.sleep(1)
        select_league()
        time.sleep(1)
        
        if (complete_colosseum() == True):
            print("Colosseum Task Complete!")
            self.colosseum = True
            return
        
        auto_check()
        time.sleep(0.5)
        start_colosseum()
        
        while self.colosseum == False:
            self.colosseum = complete_colosseum()
            
            if self.colosseum == False:
                continue
            
            print("Colosseum Task Complete!")
        
    def daily_quest_save_data(self):
        """
        There are 5 quest but 2 of them are the same everyday so 
        this task will accomplish the 2 same quests.
        """
        access_setting()
        time.sleep(0.5)
        save_data()
        time.sleep(0.5)
        collect_reward()
        
            