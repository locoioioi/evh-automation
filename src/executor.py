
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.utils import is_game_running, capture_screenshot, tap
from src.task import *
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
        self.watching_ad = 0
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
                
                time.sleep(2)
                self.attendance = check_attendance()
                
                time.sleep(2)
                self.offline_reward = check_offline_reward()
                
                
        self.is_login = is_game_running()
        print("Login Success!")
        
    def do_colosseum(self):
        """
        Execute the colosseum task.
        """
        
        # TODO: Handle collect reward.
        # TODO: Handle start new season.
        new_season = True # Flag to check if the game start new season.
        # Access the colosseum.
        access_colosseum() 
        time.sleep(0.5)
        select_league()
        time.sleep(1)
                
        if (complete_colosseum() == True):
            print("Colosseum Task Complete!")
            self.colosseum = True
            return
        
        # Handle when the game start new league.
        if (collect_colosseum_reward() == True):
            new_season = True
            print("Collect reward successful! Let's start new season.")

        if (new_season == True):
            start_new_season = False
            end_new_season = False
            print("Start new season...")
            while start_new_season == False:
                start_new_season = start_colosseum_new_season() 
                time.sleep(2)
                                
            while end_new_season == False:
                end_new_season = end_colosseum_new_season()
                time.sleep(10)
                
            print("End new season...! Enter the league.")            
            time.sleep(5)
        
        # Handle standard colosseum task.
        auto_check()
        time.sleep(0.5)
        start_colosseum()
        
        while self.colosseum == False:
            time.sleep(30)
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
        
    def go_dungeon(self, times = 1):
        """
        Execute the dungeon task.
        
        Input:
        - times: int, default 1, the number of times the dungeon will be executed.
        
        Returns:
        - None but the task will be executed.
        """
        
        # TODO: Make this function more flexible. Currently it just support fixed level like 276.
        # TODO: Make it find the input level and choose that
        print("Dungeon Tasks Start!")
        for i in range(times):
            access_dungeon()
            time.sleep(0.5)
            start_dungeon()
            collect_dungeon_reward()
            print(f"Finish {i + 1} times dungeon.")
            time.sleep(60)
            print("Wait for 60 seconds before next dungeon.")
            
    def watch_ad(self) -> bool:
        """
        Execute the watching ad task.
        """
        # TODO: Check more variants of the elf
        find = find_elf_ad()
        
        if find == False:
            return False
        
        time.sleep(1)
        watch = watch_ad()
        
        if watch == False:
            return False
        
        return True