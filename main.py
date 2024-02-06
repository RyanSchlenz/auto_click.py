import time
import pyautogui

def auto_click(duration_in_seconds=14400):  # 4 hours by default
    try:
        # Give some time to switch to the target application
        time.sleep(3)

        # Get the start time
        start_time = time.time()

        while time.time() - start_time < duration_in_seconds:
            # Perform a left mouse click
            pyautogui.click()

            # Set the sleep time to 5 seconds for a click every 5 seconds
            time.sleep(10)

        print("Auto-clicking stopped after 4 hours.")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    auto_click()
