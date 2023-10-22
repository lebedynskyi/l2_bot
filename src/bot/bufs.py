import logging
from abc import ABC, abstractmethod

from src.bot.base import BaseHandler
from src.controller import BaseController


class ControllerUseBottles(BaseController, ABC):
    @abstractmethod
    def use_bottle(self):
        pass


class HandlerUseBottles(BaseHandler):
    logger = logging.getLogger("UseBottles")

    def __init__(self, controller: ControllerUseBottles):
        self.controller = controller

    def _on_tick(self, screen_rgb, screen_gray, delta):
        if delta > 1150:
            self.logger.info("Use bottle")
            self.controller.use_bottle()
            return True
        return False
