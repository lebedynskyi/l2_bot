from app.logic.BaseLogic import BaseLogic
import pyautogui

KEY_ALACRITY = "F10"


class BuffLogic(BaseLogic):
    def _on_tick(self, screen_rgb, current_time, last_action_delta):
        if last_action_delta > 1195:
            pyautogui.press(KEY_ALACRITY)
            self.last_action_time = current_time
            self.write_log("Buff", "use alacrity")
