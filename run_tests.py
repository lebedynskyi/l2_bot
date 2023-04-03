import os
import unittest

import cv2

import app.core.templates as templates
from app.parsers.classic.ui import WarnDialogParser
from app.parsers.flauron.ui import QuizStartDialogParser, QuizContinueDialogParser
from app.parsers.text import TextParser
from app.solver.CaptchaSolver import CaptchaSolver

env_path = os.path.dirname(os.path.realpath(__file__))


#
# class TestParsers(unittest.TestCase):
#
#     def setUp(self):
#         self.templates = load_templates("res/template/classic")
#
#     def test_target_window_parser(self):
#         parser = TargetWindowParser(env_path, self.templates.farm.target, debug=False)
#
#         screen = cv2.imread("res/input/classic/target/Shot00002.bmp")
#         assert len(screen) > 0
#
#         result = parser.parse_image(screen)
#         assert result is not None and len(result) > 0
#         return result
#
#     def test_target_hp(self):
#         screen = cv2.imread("res/input/classic/target/Shot00003.bmp")
#         window_parser = TargetWindowParser(env_path, self.templates.farm.target, debug=False)
#         parser = TargetHpParser(env_path, debug=True)
#         hp_box = window_parser.parse_image(screen)
#         result = parser.parse_image(hp_box)
#         print(result)
#
#
# class TestSoloCaptcha(unittest.TestCase):
#     def setUp(self):
#         self.templates = load_templates("res/template/classic")
#
#     def test_warn_dialog(self):
#         screen = cv2.imread("res/input/classic/captcha/Shot00008.bmp")
#         dialog_parser = WarnDialogParser(env_path, self.templates.captcha.warn_dialog, debug=False)
#         dialog, ok_position, cancel_position = dialog_parser.parse_image(screen)
#
#         captcha_parser = DialogTextParser(env_path, debug=False)
#         captcha_text = captcha_parser.parse_image(dialog, default_scale=500)
#         print(captcha_text)
#
#         solver = CaptchaSolver()
#         print(solver.solve(captcha_text))
#

# class TestManor(unittest.TestCase):
#     def setUp(self):
#         self.templates = load_templates("res/template/classic")
#         self.keyboard = MockKeyboard()
#
#     def test_manor(self):
#         castles = [
#             ManorSellCastle("Gludio", "Fake", start_index=2)
#             # ManorSellCastle("Giran", "Fake", start_index=3)
#         ]
#
#         manor_dialog_parser = ManorDialogParser(env_path, self.templates.manor.manor_dialog_template)
#         crop_list_parser = CropListParser(env_path, self.templates.manor.crop_sales_dialog)
#         castles_list_parser = CastlesListParser(env_path, self.templates.manor.chooser_template)
#         castles_chooser_parser = CastlesListChooserParser(env_path, self.templates.manor.chooser_expanded_template)
#         manor = ManorHandler(self.keyboard, castles,
#                              manor_dialog_parser, crop_list_parser, castles_list_parser, castles_chooser_parser)
#
#         screen1 = cv2.imread("res/input/classic/manor/Shot00016.bmp")
#         screen2 = cv2.imread("res/input/classic/manor/Shot00017.bmp")
#         screen3 = cv2.imread("res/input/classic/manor/Shot00018.bmp")
#         screen4 = cv2.imread("res/input/classic/manor/Shot00019.bmp")
#         manor.on_tick(screen1, time.time())
#         manor.on_tick(screen2, time.time())
#         manor.on_tick(screen3, time.time())
#         manor.on_tick(screen4, time.time())

#
# class TestPetParser(unittest.TestCase):
#     def setUp(self):
#         self.templates = load_templates("res/template/reborn_classic")
#
#     def test_pet_small_dialog(self):
#         screen = cv2.imread("res/input/reborn_classic/pet/4.bmp")
#         parser = PetStatusParser(env_path, self.templates.status.user_pet, True)
#         hp, mp = parser.parse_image(screen)
#         print("HP -> {}    MP -> {}".format(hp, mp))

class TestFlauronDialogCaptcha(unittest.TestCase):
    def setUp(self):
        self.templates = templates.load_templates("res/template/reborn_classic")

    def test_dialog_captcha(self):
        img = cv2.imread("res/input/flauron/dialog_captcha/Shot00001.jpg")
        dialog_parser = WarnDialogParser(env_path, self.templates.captcha.warn_dialog, debug=False)
        dialog, ok_position, cancel_position = dialog_parser.parse_image(img)

        text_parser = TextParser(env_path, debug=False)
        text = text_parser.parse_image(dialog, default_scale=500)

        solver = CaptchaSolver()
        answer = solver.solve(text)
        print(text)
        print(answer)


class TestFlauronQuizCaptcha(unittest.TestCase):
    def setUp(self):
        self.templates = templates.load_templates("res/template/reborn_classic")

    def test_quiz_start_captcha(self):
        start_quiz_img = cv2.imread("res/input/flauron/quiz_captcha/start/Shot00002.jpg")

        quiz_parser = QuizStartDialogParser(env_path, self.templates.captcha.captcha_quiz_start, False)
        rez = quiz_parser.parse_image(start_quiz_img)
        print(rez)

    def test_quiz_continue(self):
        quiz_parser = QuizContinueDialogParser(env_path, self.templates.captcha.captcha_quiz_continue, True)

        quiz_img = cv2.imread("res/input/flauron/quiz_captcha/Shot00010.jpg")
        rez = quiz_parser.parse_image(quiz_img)
        print(rez)


if __name__ == '__main__':
    from tests.TestT import TestTt
    unittest.main()
