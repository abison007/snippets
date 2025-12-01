#!/usr/bin/env python3
"""
Moves the mouse every 2 minutes.
Randomly skips mouse movement for 5 minutes once every 20-minute cycle.
"""

import time
import random
from datetime import datetime
import pyautogui

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------
TOTAL_RUNTIME_MINUTES = int(input("Enter total run time in minutes: "))
MOVE_INTERVAL_MINUTES = 2
SKIP_DURATION_MINUTES = 5
CYCLE_DURATION_MINUTES = 20
WARP_COUNT = 50
SHIFT_PRESSES = 3

def perform_macro_action():
    start_x, start_y = pyautogui.position()
    print(f"🖱️  Moving mouse at {datetime.now().time()}")

    for step in range(WARP_COUNT):
        pyautogui.moveTo(start_x, start_y + step * 4, duration=0.01)

    for _ in range(SHIFT_PRESSES):
        pyautogui.press("shift")

    pyautogui.moveTo(start_x, start_y, duration=0.05)

def run_macro():
    pyautogui.FAILSAFE = False
    elapsed_minutes = 0
    cycle_no = 0

    print("\n🔄  Starting macro… Press Ctrl+C to stop manually.\n")

    try:
        while elapsed_minutes < TOTAL_RUNTIME_MINUTES:
            cycle_no += 1
            print(f"\n🌀  Starting 20-minute cycle {cycle_no} at {datetime.now().time()}")

            # Randomly choose a 5-minute block to skip
            skip_start_minute = random.randint(0, CYCLE_DURATION_MINUTES - SKIP_DURATION_MINUTES)
            skip_range = range(skip_start_minute, skip_start_minute + SKIP_DURATION_MINUTES)

            for minute_in_cycle in range(CYCLE_DURATION_MINUTES):
                if elapsed_minutes >= TOTAL_RUNTIME_MINUTES:
                    break

                if minute_in_cycle in skip_range:
                    print(f"⏸️  Skipping mouse movement at minute {elapsed_minutes + 1}")
                elif minute_in_cycle % MOVE_INTERVAL_MINUTES == 0:
                    perform_macro_action()

                time.sleep(60)
                elapsed_minutes += 1

            print(f"✅  Finished cycle {cycle_no} at {datetime.now().time()}")

        print(f"\n🏁  Macro completed. Total runtime: {elapsed_minutes} minutes.")

    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user. Exiting…")

# ------------------------------------------------------------
if __name__ == "__main__":
    run_macro()
