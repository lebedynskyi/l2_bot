from app.handlers.BaseHandler import BaseHandler

import cv2
import numpy as np


class WarnDialogHandler(BaseHandler):
    def __init__(self, env_path, warning_template, debug=False):
        super().__init__(env_path, debug)
        self.template = cv2.cvtColor(warning_template, cv2.COLOR_RGB2GRAY)

    def parse_image(self, image_rgb):
        image_rgb = image_rgb.copy()
        image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)

        match = cv2.matchTemplate(image, self.template, cv2.TM_CCORR_NORMED)

        thresh_hold = 0.89
        loc = np.where(match >= thresh_hold)

        # draw matches
        hh, ww = self.template.shape[:2]
        warning_points = list(zip(*loc[::-1]))
        if warning_points:
            print("WarnDialog: Match found")
            if self.debug:
                self.draw_square(image_rgb, warning_points, ww, hh)
                self.debug_show_im(image_rgb)
            return self.crop_dialog(image_rgb, warning_points)

        print("WarnDialog: No match found")
        return None

    def crop_dialog(self, image, warn_points):
        pt = warn_points[0]
        dialog_img = image[pt[1]-7:pt[1] + 120, pt[0]-10:pt[0] + 294]
        if self.debug:
            self.debug_show_im(dialog_img)
        return dialog_img
