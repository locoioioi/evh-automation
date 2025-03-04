import subprocess
import os
import cv2 as cv
import numpy as np
from numpy import unravel_index 
from matplotlib import pyplot as plt

# Define the path to adb.exe
ADB_PATH = os.path.join(os.path.dirname(__file__), "..", "adb.exe")
PACKAGE_NAME="com.superplanet.evilhunter"

def execute_shell_command(command: str, use_adb: bool = False) -> str:
    """
    Execute a shell command.
    If 'use_adb' is True, prepend the local adb.exe path.
    """
    try:
        # If use_adb is True, prepend adb.exe
        full_command = f'"{ADB_PATH}" {command}' if use_adb else command
        
        result = subprocess.run(full_command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {full_command}\nError Message: {e.stderr.strip()}")
        return ""

def launch_game():
    """ 
    Launch Evil Hunter Tycoon after LDPlayer starts 
    
    return: None but the game should be launched
    """
    execute_shell_command("shell monkey -p com.superplanet.evilhunter -c android.intent.category.LAUNCHER 1", use_adb=True)
    
def is_game_running() -> bool:
    """
    Check if Evil Hunter Tycoon is running 
    
    return: True if the game is running, False otherwise
    """
    output = execute_shell_command(f"shell dumpsys activity activities | grep {PACKAGE_NAME}", use_adb=True)
    return PACKAGE_NAME in output 

import os

def capture_screenshot(name: str = "screenshot") -> str:
    """
    Capture the screen of the emulator and save it in the cache folder.
    
    Returns:
        str: The relative path to the screenshot in the cache folder.
    """
    cache_dir = ".cache"
    screenshot_path = os.path.join(cache_dir, name + ".png")

    os.makedirs(cache_dir, exist_ok=True)

    execute_shell_command("shell screencap -p /sdcard/screen.png", use_adb=True)

    execute_shell_command(f"pull /sdcard/screen.png {screenshot_path}", use_adb=True)
    
    execute_shell_command("shell rm /sdcard/screen.png", use_adb=True)

    return screenshot_path

def is_in_screen(screen_path: str, template_path: str, confidence: float = 0.8):
    """
    Detects a template inside a screen image using OpenCV's template matching.
    Uses TM_CCOEFF_NORMED for best accuracy.

    Args:
        screen_path (str): Path to the screen image.
        template_path (str): Path to the template image.
        display_scale (float): Scaling factor for displaying images (default: 0.5 for 50% size).

    Returns:
        tuple[int, int] | None: Middle X, Y coordinates of the detected template,
                                or None if the template is not found.
    """
    match_method = cv.TM_CCOEFF_NORMED 
    
    # Load Images
    screen = cv.imread(screen_path, cv.IMREAD_UNCHANGED)
    template = cv.imread(template_path, cv.IMREAD_UNCHANGED)

    if screen is None or template is None:
        return None

    if screen.shape[-1] == 4:
        screen = cv.cvtColor(screen, cv.COLOR_BGRA2GRAY)
    else:
        screen = cv.cvtColor(screen, cv.COLOR_BGR2GRAY)

    if template.shape[-1] == 4:
        template = cv.cvtColor(template, cv.COLOR_BGRA2GRAY)
    else:
        template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

    if template.shape[0] > screen.shape[0] or template.shape[1] > screen.shape[1]:
        screen, template = template, screen

    w, h = template.shape[::-1]

    result = cv.matchTemplate(screen, template, match_method)

    result_norm = np.zeros(result.shape, dtype=np.float32)
    cv.normalize(result, result_norm, alpha=0, beta=1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)

    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    match_loc = max_loc

    # Get center of detected region
    center_x = int(match_loc[0] + w // 2)
    center_y = int(match_loc[1] + h // 2)

    if max_val < confidence:
        return None
    
    return center_x, center_y

def tap(x: int, y: int):
    """
    Tap on the screen at the given X, Y coordinates.
    """
    execute_shell_command(f"shell input tap {x} {y}", use_adb=True)
    
def is_in_screen_v2(screen_path: str, template_path: str):
    """
    Have the same functionality with is_in_screen but utilize feature matching for detect object that has too much variants.
    
    Args:
        screen_path (str): Path to the screen image.
        template_path (str): Path to the template image.
        
    Returns:
        tuple[int, int] | None: Middle X, Y coordinates of the detected template,
                                or None if the template is not found.
    """
    screen = cv.imread(screen_path, cv.IMREAD_GRAYSCALE)
    template = cv.imread(template_path, cv.IMREAD_GRAYSCALE)

    if screen is None or template is None:
        print("❌ Error: One or both images could not be loaded!")
        return None

    # Initiate SIFT detector
    sift = cv.SIFT_create()

    # Find keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(screen, None)
    kp2, des2 = sift.detectAndCompute(template, None)

    if des1 is None or des2 is None:
        print("❌ Not enough keypoints detected!")
        return None

    # BFMatcher with default params
    bf = cv.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    # Apply Lowe’s ratio test
    good = []
    for m, n in matches:
        if m.distance < 0.65 * n.distance:  # Stricter ratio test
            good.append(m)  # Store as flat list (not list of lists)

    if len(good) < 10:
        print("❌ Not enough good matches")
        return None

    # Select the best match based on the lowest distance
    best_match = min(good, key=lambda x: x.distance)

    coords = kp2[best_match.trainIdx].pt  # (x, y)

    print(f"✅ Best keypoint selected: {coords} (lowest distance = {best_match.distance:.2f})")
    return coords