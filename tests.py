import os
import sys
import unittest
import subprocess
import hashlib
import string

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "./trdg")))

try:
    os.mkdir("tests/out")
except:
    pass

from diffimg import diff

from trdg.data_generator_update import FakeTextDataGenerator
from trdg import background_generator
from trdg.generators import (
    GeneratorFromDict,
    GeneratorFromRandom,
    GeneratorFromStrings,
    GeneratorFromWikipedia,
)
from trdg.string_generator import (
    create_strings_from_file,
    create_strings_from_dict,
    create_strings_from_wikipedia,
    create_strings_randomly,
)


def empty_directory(path):
    for f in os.listdir(path):
        os.remove(os.path.join(path, f))


# class Generators(unittest.TestCase):
#     def test_generator_from_dict(self):
#         generator = GeneratorFromDict()
#         i = 0
#         while i < 100:
#             img, lbl = next(generator)
#             self.assertTrue(img.size[1] == 32, "Shape is not right")
#             i += 1

#     def test_generator_from_random(self):
#         generator = GeneratorFromRandom()
#         i = 0
#         while i < 100:
#             img, lbl = next(generator)
#             self.assertTrue(img.size[1] == 32, "Shape is not right")
#             i += 1

#     # def test_generator_from_strings(self):
#     #     generator = GeneratorFromStrings(["慶出火宅作清"])
#     #     i = 0
#     #     while i < 100:
#     #         img, lbl = next(generator)
#     #         self.assertTrue(img.size[1] == 32, "Shape is not right")
#     #         i += 1

#     # def test_generator_from_wikipedia(self):
#     #     generator = GeneratorFromWikipedia()
#     #     i = 0
#     #     while i < 100:
#     #         img, lbl = next(generator)
#     #         self.assertTrue(img.size[1] == 32, "Shape is not right")
#     #         i += 1

#     # def test_generator_from_dict_stops(self):
#     #     generator = GeneratorFromDict(count=1)
#     #     next(generator)
#     #     self.assertRaises(StopIteration, generator.next)

#     # def test_generator_from_random_stops(self):
#     #     generator = GeneratorFromRandom(count=1)
#     #     next(generator)
#     #     self.assertRaises(StopIteration, generator.next)

#     # def test_generator_from_strings_stops(self):
#     #     generator = GeneratorFromStrings(["TEST TEST TEST"], count=1)
#     #     next(generator)
#     #     self.assertRaises(StopIteration, generator.next)

#     # def test_generator_from_wikipedia_stops(self):
#     #     generator = GeneratorFromWikipedia(count=1)
#     #     next(generator)
#     #     self.assertRaises(StopIteration, generator.next)


class DataGenerator(unittest.TestCase):
    # def test_create_string_from_wikipedia(self):
    #     """
    #         Test that the function returns different output if called twice.
    #         (And that it doesn't throw of course)
    #     """

    #     strings = create_strings_from_wikipedia(20, 2, "en")

    #     self.assertTrue(
    #         len(strings) == 2
    #         and strings[0] != strings[1]
    #         and len(strings[0].split(" ")) >= 20
    #         and len(strings[1].split(" ")) >= 20
    #     )

    # def test_create_string_from_file(self):
    #     strings = create_strings_from_file("tests/test.txt", 6)

    #     self.assertTrue(
    #         len(strings) == 6 and strings[0] != strings[1] and strings[0] == strings[3]
    #     )

    # def test_create_strings_from_dict(self):
    #     strings = create_strings_from_dict(
    #         3, False, 2, ["之", "以", "人",  "月", "十", "不", "年", "帝", "有"]
    #     )

    #     self.assertTrue(len(strings) == 2 and len(strings[0].split(" ")) == 3)

    def test_generate_data_with_format(self):
        FakeTextDataGenerator.generate(
            index = 0,
            text = "九霄日月映重光",
            fonts = "tests/font",
            out_dir = "tests/out/",
            gray_scale = True,
            min_font_size=30,
            max_font_size=60,
            extension="jpg",
            random_spacing=True,
            max_random_spacing=len("九霄日月映重光") - 1,
            skewing_angle=1,
            random_skew=True,
            blur=0,
            random_blur=True,
            background_type=3,
            distorsion_type=0,
            distorsion_orientation=2,
            is_handwritten= False,
            name_format=0,
            width=-1,
            alignment=0,
            text_color="#010101",
            orientation= 1,
            space_width=1,
            character_spacing=0,
            margins=(5, 5, 5, 5),
            fit=1,
            output_mask=0,
            word_split=False,
            image_dir=os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
        )

        # self.assertLess(
        #     diff(
        #         "tests/out/九霄日月映重光_0.jpg",
        #         "tests/expected_results/九霄日月映重光_0.jpg",
        #         delete_diff_file=True,
        #     ),
        #     0.11
        # )

        # os.remove("tests/out/九霄日月映重光_0.jpg")

    # def test_generate_data_with_extension(self):
    #     FakeTextDataGenerator.generate(
    #         1,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         32,
    #         "png",
    #         0,
    #         False,
    #         0,
    #         False,
    #         1,
    #         0,
    #         0,
    #         False,
    #         0,
    #         -1,
    #         0,
    #         "#010101",
    #         0,
    #         1,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         False,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/九霄日月映重光_1.png",
    #     #         "tests/expected_results/九霄日月映重光_1.png",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.07
    #     # )

    #     # os.remove("tests/out/九霄日月映重光_1.png")

    # def test_generate_data_with_skew_angle(self):
    #     FakeTextDataGenerator.generate(
    #         2,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         64,
    #         "jpg",
    #         15,
    #         False,
    #         0,
    #         False,
    #         1,
    #         0,
    #         0,
    #         False,
    #         0,
    #         -1,
    #         0,
    #         "#010101",
    #         0,
    #         1,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         False,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/九霄日月映重光_2.jpg",
    #     #         "tests/expected_results/九霄日月映重光_2.jpg",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.05
    #     # )

    #     # os.remove("tests/out/九霄日月映重光_2.jpg")

    # def test_generate_data_with_blur(self):
    #     FakeTextDataGenerator.generate(
    #         3,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         64,
    #         "jpg",
    #         0,
    #         False,
    #         3,
    #         False,
    #         1,
    #         0,
    #         0,
    #         False,
    #         0,
    #         -1,
    #         0,
    #         "#010101",
    #         0,
    #         1,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         False,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/九霄日月映重光_3.jpg",
    #     #         "tests/expected_results/九霄日月映重光_3.jpg",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.06
    #     # )

    #     # os.remove("tests/out/九霄日月映重光_3.jpg")

    # def test_generate_data_with_sine_distorsion(self):
    #     FakeTextDataGenerator.generate(
    #         4,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         64,
    #         "jpg",
    #         0,
    #         False,
    #         3,
    #         False,
    #         1,
    #         1,
    #         2,
    #         False,
    #         0,
    #         -1,
    #         0,
    #         "#010101",
    #         0,
    #         1,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         False,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/九霄日月映重光_4.jpg",
    #     #         "tests/expected_results/九霄日月映重光_4.jpg",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.05
    #     # )

    #     # os.remove("tests/out/九霄日月映重光_4.jpg")

    # def test_generate_data_with_cosine_distorsion(self):
    #     FakeTextDataGenerator.generate(
    #         5,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         64,
    #         "jpg",
    #         0,
    #         False,
    #         3,
    #         False,
    #         1,
    #         2,
    #         2,
    #         False,
    #         0,
    #         -1,
    #         0,
    #         "#010101",
    #         0,
    #         1,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         False,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/九霄日月映重光_5.jpg",
    #     #         "tests/expected_results/九霄日月映重光_5.jpg",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.05
    #     # )

    #     # os.remove("tests/out/九霄日月映重光_5.jpg")

    # def test_generate_data_with_left_alignment(self):
    #     FakeTextDataGenerator.generate(
    #         6,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         64,
    #         "jpg",
    #         0,
    #         False,
    #         0,
    #         False,
    #         1,
    #         0,
    #         0,
    #         False,
    #         0,
    #         600,
    #         0,
    #         "#010101",
    #         0,
    #         1,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         False,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/九霄日月映重光_6.jpg",
    #     #         "tests/expected_results/九霄日月映重光_6.jpg",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.07
    #     # )

    #     # os.remove("tests/out/九霄日月映重光_6.jpg")

    # def test_generate_data_with_center_alignment(self):
    #     FakeTextDataGenerator.generate(
    #         7,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         64,
    #         "jpg",
    #         0,
    #         False,
    #         0,
    #         False,
    #         1,
    #         0,
    #         0,
    #         False,
    #         0,
    #         800,
    #         1,
    #         "#010101",
    #         0,
    #         1,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         False,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/九霄日月映重光_7.jpg",
    #     #         "tests/expected_results/九霄日月映重光_7.jpg",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.05
    #     # )

    #     # os.remove("tests/out/九霄日月映重光_7.jpg")

    # def test_generate_data_with_right_alignment(self):
    #     FakeTextDataGenerator.generate(
    #         8,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         64,
    #         "jpg",
    #         0,
    #         False,
    #         0,
    #         False,
    #         1,
    #         0,
    #         0,
    #         False,
    #         0,
    #         1000,
    #         2,
    #         "#010101",
    #         0,
    #         1,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         False,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/九霄日月映重光_8.jpg",
    #     #         "tests/expected_results/九霄日月映重光_8.jpg",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.05
    #     # )

    #     # os.remove("tests/out/九霄日月映重光_8.jpg")

    # def test_raise_if_handwritten_and_vertical(self):
    #     try:
    #         FakeTextDataGenerator.generate(
    #             9,
    #             "九霄日月映重光",
    #             "tests/NomNaTong_Regular.ttf",
    #             "tests/out/",
    #             64,
    #             "jpg",
    #             0,
    #             False,
    #             0,
    #             False,
    #             1,
    #             0,
    #             0,
    #             True,
    #             0,
    #             1000,
    #             2,
    #             "#010101",
    #             1,
    #             1,
    #             0,
    #             (5, 5, 5, 5),
    #             0,
    #             0,
    #             False,
    #             os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #         )
    #         raise Exception("Vertical handwritten did not throw")
    #     except ValueError:
    #         pass

    # def test_generate_vertical_text(self):
    #     FakeTextDataGenerator.generate(
    #         10,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         32,
    #         "jpg",
    #         0,
    #         False,
    #         0,
    #         False,
    #         1,
    #         0,
    #         0,
    #         False,
    #         0,
    #         -1,
    #         0,
    #         "#010101",
    #         1,
    #         1,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         False,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/九霄日月映重光_10.jpg",
    #     #         "tests/expected_results/九霄日月映重光_10.jpg",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.05
    #     # )

    #     # os.remove("tests/out/九霄日月映重光_10.jpg")

    # def test_generate_horizontal_text_with_variable_space(self):
    #     FakeTextDataGenerator.generate(
    #         11,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         32,
    #         "jpg",
    #         0,
    #         False,
    #         0,
    #         False,
    #         1,
    #         0,
    #         0,
    #         False,
    #         0,
    #         -1,
    #         0,
    #         "#010101",
    #         0,
    #         4,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         False,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/九霄日月映重光_11.jpg",
    #     #         "tests/expected_results/九霄日月映重光_11.jpg",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.09
    #     # )

    #     # os.remove("tests/out/九霄日月映重光_11.jpg")

    # def test_generate_vertical_text_with_variable_space(self):
    #     FakeTextDataGenerator.generate(
    #         12,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         32,
    #         "jpg",
    #         0,
    #         False,
    #         0,
    #         False,
    #         1,
    #         0,
    #         0,
    #         False,
    #         0,
    #         -1,
    #         0,
    #         "#010101",
    #         1,
    #         2,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         False,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/九霄日月映重光_12.jpg",
    #     #         "tests/expected_results/九霄日月映重光_12.jpg",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.05
    #     # )

    #     # os.remove("tests/out/九霄日月映重光_12.jpg")

    # def test_generate_text_with_unknown_orientation(self):
    #     try:
    #         FakeTextDataGenerator.generate(
    #             12,
    #             "九霄日月映重光",
    #             "tests/NomNaTong_Regular.ttf",
    #             "tests/out/",
    #             32,
    #             "jpg",
    #             0,
    #             False,
    #             0,
    #             False,
    #             1,
    #             0,
    #             0,
    #             False,
    #             0,
    #             -1,
    #             0,
    #             "#010101",
    #             100,
    #             2,
    #             0,
    #             (5, 5, 5, 5),
    #             0,
    #             0,
    #             False,
    #             os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #         )
    #         raise Exception("Unknown orientation did not throw")
    #     except ValueError:
    #         pass

    # def test_generate_data_with_fit(self):
    #     FakeTextDataGenerator.generate(
    #         13,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         64,
    #         "jpg",
    #         0,
    #         False,
    #         0,
    #         False,
    #         1,
    #         0,
    #         0,
    #         False,
    #         0,
    #         -1,
    #         0,
    #         "#010101",
    #         0,
    #         1,
    #         0,
    #         (0, 0, 0, 0),
    #         1,
    #         0,
    #         False,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/九霄日月映重光.jpg",
    #     #         "tests/expected_results/九霄日月映重光_13.jpg",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.19
    #     # )

    #     # os.remove("tests/out/九霄日月映重光_13.jpg")

    # def test_generate_data_with_word_split(self):
    #     FakeTextDataGenerator.generate(
    #         14,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         64,
    #         "png",
    #         0,
    #         False,
    #         0,
    #         False,
    #         1,
    #         0,
    #         0,
    #         False,
    #         0,
    #         -1,
    #         0,
    #         "#010101",
    #         0,
    #         1,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         True,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/九霄日月映重光_14.png",
    #     #         "tests/expected_results/九霄日月映重光_14.png",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.05
    #     # )

    #     # os.remove("tests/out/九霄日月映重光_14.png")

    # def test_generate_data_with_first_name_format(self):
    #     FakeTextDataGenerator.generate(
    #         15,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         64,
    #         "png",
    #         0,
    #         False,
    #         0,
    #         False,
    #         1,
    #         0,
    #         0,
    #         False,
    #         0,
    #         -1,
    #         0,
    #         "#010101",
    #         0,
    #         1,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         True,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/九霄日月映重光_15.png",
    #     #         "tests/expected_results/九霄日月映重光_15.png",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.05
    #     # )

    #     # os.remove("tests/out/九霄日月映重光_15.png")

    # def test_generate_data_with_second_name_format(self):
    #     FakeTextDataGenerator.generate(
    #         16,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         64,
    #         "png",
    #         0,
    #         False,
    #         0,
    #         False,
    #         1,
    #         0,
    #         0,
    #         False,
    #         1,
    #         -1,
    #         0,
    #         "#010101",
    #         0,
    #         1,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         True,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/九霄日月映重光_16.png",
    #     #         "tests/expected_results/九霄日月映重光_16.png",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.05
    #     # )

    #     # os.remove("tests/out/九霄日月映重光_16.png")

    # def test_generate_data_with_third_name_format(self):
    #     FakeTextDataGenerator.generate(
    #         17,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         64,
    #         "png",
    #         0,
    #         False,
    #         0,
    #         False,
    #         1,
    #         0,
    #         0,
    #         False,
    #         2,
    #         -1,
    #         0,
    #         "#010101",
    #         0,
    #         1,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         True,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/17.png",
    #     #         "tests/expected_results/17.png",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.05
    #     # )

    #     # os.remove("tests/out/17.png")

    # def test_generate_data_with_wrong_name_format(self):
    #     FakeTextDataGenerator.generate(
    #         18,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         64,
    #         "png",
    #         0,
    #         False,
    #         0,
    #         False,
    #         1,
    #         0,
    #         0,
    #         False,
    #         3,
    #         -1,
    #         0,
    #         "#010101",
    #         0,
    #         1,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         True,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/九霄日月映重光_18.png",
    #     #         "tests/expected_results/九霄日月映重光_18.png",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.05
    #     # )

    #     # os.remove("tests/out/九霄日月映重光_18.png")

    # def test_generate_data_with_quasicrystal_background_from_generate(self):
    #     FakeTextDataGenerator.generate(
    #         19,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         64,
    #         "png",
    #         0,
    #         False,
    #         0,
    #         False,
    #         3,
    #         0,
    #         0,
    #         False,
    #         0,
    #         -1,
    #         0,
    #         "#010101",
    #         0,
    #         1,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         True,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #     )

    #     # os.remove("tests/out/九霄日月映重光_19.png")

    # def test_raise_if_invalid_orientation(self):
    #     try:
    #         FakeTextDataGenerator.generate(
    #             20,
    #             "九霄日月映重光",
    #             "tests/NomNaTong_Regular.ttf",
    #             "tests/out/",
    #             64,
    #             "jpg",
    #             0,
    #             False,
    #             0,
    #             False,
    #             1,
    #             0,
    #             0,
    #             False,
    #             0,
    #             1000,
    #             2,
    #             "#010101",
    #             3,
    #             1,
    #             0,
    #             (5, 5, 5, 5),
    #             0,
    #             0,
    #             False,
    #             os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #         )
    #         raise Exception("Invalid orientation did not throw")
    #     except ValueError:
    #         pass

    # def test_generate_data_with_output_bounding_box(self):
    #     FakeTextDataGenerator.generate(
    #         21,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         64,
    #         "jpg",
    #         0,
    #         False,
    #         0,
    #         False,
    #         1,
    #         0,
    #         0,
    #         False,
    #         0,
    #         -1,
    #         0,
    #         "#010101",
    #         0,
    #         1,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         False,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #         output_bboxes=1,
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/九霄日月映重光_21.jpg",
    #     #         "tests/expected_results/九霄日月映重光_21.jpg",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.11
    #     # )

    #     # os.remove("tests/out/九霄日月映重光_21.jpg")
    #     # os.remove("tests/out/九霄日月映重光_21_boxes.txt")

    # def test_generate_data_with_tesseract_output_bounding_box(self):
    #     FakeTextDataGenerator.generate(
    #         22,
    #         "九霄日月映重光",
    #         "tests/NomNaTong_Regular.ttf",
    #         "tests/out/",
    #         64,
    #         "jpg",
    #         0,
    #         False,
    #         0,
    #         False,
    #         1,
    #         0,
    #         0,
    #         False,
    #         0,
    #         -1,
    #         0,
    #         "#010101",
    #         0,
    #         1,
    #         0,
    #         (5, 5, 5, 5),
    #         0,
    #         0,
    #         False,
    #         os.path.join(os.path.split(os.path.realpath(__file__))[0], "trdg/images"),
    #         output_bboxes=2,
    #     )

    #     # self.assertLess(
    #     #     diff(
    #     #         "tests/out/九霄日月映重光_22.jpg",
    #     #         "tests/expected_results/九霄日月映重光_22.jpg",
    #     #         delete_diff_file=True,
    #     #     ),
    #     #     0.11
    #     # )

    #     # os.remove("tests/out/九霄日月映重光_22.jpg")
    #     # os.remove("tests/out/九霄日月映重光_22.box")

    # def test_generate_string_with_letters(self):
    #     s = create_strings_randomly(1, False, 1, True, False, False, "en")[0]

    #     self.assertTrue(all([l in string.ascii_letters for l in s]))

    # def test_generate_string_with_numbers(self):
    #     s = create_strings_randomly(1, False, 1, False, True, False, "en")[0]

    #     self.assertTrue(all([l in "0123456789" for l in s]))

    # def test_generate_string_with_symbols(self):
    #     s = create_strings_randomly(1, False, 1, False, False, True, "en")[0]

    #     self.assertTrue(all([l in "!\"#$%&'()*+,-./:;?@[\\]^_`{|}~" for l in s]))

    # def test_generate_chinese_string(self):
    #     s = create_strings_randomly(1, False, 1, True, False, False, "cn")[0]

    #     cn_chars = [chr(i) for i in range(19968, 40908)]

    #     self.assertTrue(all([l in cn_chars for l in s]))

    # def test_generate_japanese_string(self):
    #     s = create_strings_randomly(1, False, 1, True, False, False, "ja")[0]

    #     ja_chars = [chr(i) for i in range(12288, 12543)] + [chr(i) for i in range(65280, 65519)] + [chr(i) for i in range(19968, 40908)]

    #     self.assertTrue(all([l in ja_chars for l in s]))

    # def test_generate_data_with_wild_background(self):
    #     background_generator.image(64, 128, "tests/background").save(
    #         "tests/out/bricks.jpg"
    #     )

    #     self.assertTrue(
    #         diff(
    #             "tests/out/bricks.jpg",
    #             "tests/background/bricks.jpg",
    #             delete_diff_file=True,
    #         )
    #         < 0.01
    #     )

    #     os.remove("tests/out/bricks.jpg")

    def test_generate_data_with_quasicrystal_background(self):
        bkgd = background_generator.quasicrystal(64, 128)

        self.assertTrue(len(bkgd.histogram()) > 20 and bkgd.size == (128, 64))


# class CommandLineInterface(unittest.TestCase):
#     def test_output_dir(self):
#         args = ["python3", "run.py", "-c", "1", "--output_dir", "../tests/out_2/"]
#         subprocess.Popen(args, cwd="trdg/").wait()
#         self.assertTrue(len(os.listdir("tests/out_2/")) == 1)
#         empty_directory("tests/out_2/")

#     def test_language_english(self):
#         args = [
#             "python3",
#             "run.py",
#             "-l",
#             "en",
#             "-c",
#             "1",
#             "--output_dir",
#             "../tests/out/",
#         ]
#         subprocess.Popen(args, cwd="trdg/").wait()
#         self.assertTrue(len(os.listdir("tests/out/")) == 1)
#         empty_directory("tests/out/")

#     def test_language_french(self):
#         args = [
#             "python3",
#             "run.py",
#             "-l",
#             "fr",
#             "-c",
#             "1",
#             "--output_dir",
#             "../tests/out/",
#         ]
#         subprocess.Popen(args, cwd="trdg/").wait()
#         self.assertTrue(len(os.listdir("tests/out/")) == 1)
#         empty_directory("tests/out/")

#     def test_language_spanish(self):
#         args = [
#             "python3",
#             "run.py",
#             "-l",
#             "es",
#             "-c",
#             "1",
#             "--output_dir",
#             "../tests/out/",
#         ]
#         subprocess.Popen(args, cwd="trdg/").wait()
#         self.assertTrue(len(os.listdir("tests/out/")) == 1)
#         empty_directory("tests/out/")

#     def test_language_german(self):
#         args = [
#             "python3",
#             "run.py",
#             "-l",
#             "de",
#             "-c",
#             "1",
#             "--output_dir",
#             "../tests/out/",
#         ]
#         subprocess.Popen(args, cwd="trdg/").wait()
#         self.assertTrue(len(os.listdir("tests/out/")) == 1)
#         empty_directory("tests/out/")

#     def test_language_chinese(self):
#         args = [
#             "python3",
#             "run.py",
#             "-l",
#             "cn",
#             "-c",
#             "1",
#             "--output_dir",
#             "../tests/out/",
#         ]
#         subprocess.Popen(args, cwd="trdg/").wait()
#         self.assertTrue(len(os.listdir("tests/out/")) == 1)
#         empty_directory("tests/out/")

#     def test_count_parameter(self):
#         args = ["python3", "run.py", "-c", "10", "--output_dir", "../tests/out/"]
#         subprocess.Popen(args, cwd="trdg/").wait()
#         self.assertTrue(len(os.listdir("tests/out/")) == 10)
#         empty_directory("tests/out/")

#     def test_random_sequences_letter_only(self):
#         args = [
#             "python3",
#             "run.py",
#             "-rs",
#             "-let",
#             "-c",
#             "1",
#             "--output_dir",
#             "../tests/out/",
#         ]
#         subprocess.Popen(args, cwd="trdg/").wait()
#         self.assertTrue(
#             all(
#                 [
#                     c in string.ascii_letters
#                     for f in os.listdir("tests/out/")
#                     for c in f.split("_")[0]
#                 ]
#             )
#         )
#         empty_directory("tests/out/")

#     def test_random_sequences_number_only(self):
#         args = [
#             "python3",
#             "run.py",
#             "-rs",
#             "-num",
#             "-c",
#             "1",
#             "--output_dir",
#             "../tests/out/",
#         ]
#         subprocess.Popen(args, cwd="trdg/").wait()
#         self.assertTrue(
#             all(
#                 [
#                     c in "0123456789"
#                     for f in os.listdir("tests/out/")
#                     for c in f.split("_")[0]
#                 ]
#             )
#         )
#         empty_directory("tests/out/")

#     def test_random_sequences_symbols_only(self):
#         args = [
#             "python3",
#             "run.py",
#             "-rs",
#             "-sym",
#             "-c",
#             "1",
#             "--output_dir",
#             "../tests/out/",
#         ]
#         subprocess.Popen(args, cwd="trdg/").wait()
#         with open("tests/out/labels.txt", "r") as f:
#             self.assertTrue(
#                 all(
#                     [
#                         c in "!\"#$%&'()*+,-./:;?@[\\]^_`{|}~"
#                         for c in f.readline().split(" ")[1][:-1]
#                     ]
#                 )
#             )
#         empty_directory("tests/out/")

#     def test_handwritten(self):
#         args = ["python3", "run.py", "-c", "1", "--output_dir", "../tests/out/"]
#         subprocess.Popen(args, cwd="trdg/").wait()
#         self.assertTrue(len(os.listdir("tests/out/")) == 1)
#         empty_directory("tests/out/")

#     def test_personalfont(self):
#         args = [
#             "python3",
#             "run.py",
#             "--font",
#             "fonts/latin/Aller_Bd.ttf",
#             "-c",
#             "1",
#             "--output_dir",
#             "../tests/out/",
#         ]
#         subprocess.Popen(args, cwd="trdg/").wait()
#         self.assertTrue(len(os.listdir("tests/out/")) == 1)
#         empty_directory("tests/out/")

#     def test_personalfont_unlocated(self):
#         args = [
#             "python3",
#             "run.py",
#             "--font",
#             "fonts/latin/unlocatedFont.ttf",
#             "-c",
#             "1",
#             "--output_dir",
#             "../tests/out/",
#         ]
#         subprocess.Popen(args, cwd="trdg/").wait()
#         self.assertTrue(len(os.listdir("tests/out/")) == 0)
#         empty_directory("tests/out/")

#     def test_personalfont_directory(self):
#         args = [
#             "python3",
#             "run.py",
#             "--font_dir",
#             "fonts/latin/",
#             "-c",
#             "1",
#             "--output_dir",
#             "../tests/out/",
#         ]
#         subprocess.Popen(args, cwd="trdg/").wait()
#         self.assertTrue(len(os.listdir("tests/out/")) == 1)
#         empty_directory("tests/out/")

#     def test_personalfont_directory_unlocated(self):
#         args = [
#             "python3",
#             "run.py",
#             "--font_dir",
#             "fonts/void/",
#             "-c",
#             "1",
#             "--output_dir",
#             "../tests/out/",
#         ]
#         subprocess.Popen(args, cwd="trdg/").wait()
#         self.assertTrue(len(os.listdir("tests/out/")) == 0)
#         empty_directory("tests/out/")

#     def test_personaldict(self):
#         args = [
#             "python3",
#             "run.py",
#             "--dict",
#             "dicts/en.txt",
#             "-c",
#             "1",
#             "--output_dir",
#             "../tests/out/",
#         ]
#         subprocess.Popen(args, cwd="trdg/").wait()
#         self.assertTrue(len(os.listdir("tests/out/")) == 1)
#         empty_directory("tests/out/")

#     def test_personaldict_unlocated(self):
#         args = [
#             "python3",
#             "run.py",
#             "--dict",
#             "dicts/unlocatedDict.txt",
#             "-c",
#             "1",
#             "--output_dir",
#             "../tests/out/",
#         ]
#         subprocess.Popen(args, cwd="trdg/").wait()
#         self.assertTrue(len(os.listdir("tests/out/")) == 0)
#         empty_directory("tests/out/")

#     def test_first_name_format(self):
#         args = [
#             "python3",
#             "run.py",
#             "--dict",
#             "dicts/unlocatedDict.txt",
#             "-c",
#             "1",
#             "--output_dir",
#             "../tests/out/",
#         ]
#         subprocess.Popen(args, cwd="trdg/").wait()
#         self.assertTrue(len(os.listdir("tests/out/")) == 0)
#         empty_directory("tests/out/")


#    def test_word_count(self):
#        args = ['python3', 'run.py', '-c', '1', '-w', '5']
#        subprocess.Popen(args, cwd="trdg/").wait()
#        self.assertTrue(False)
#        empty_directory('tests/out/')
#
#    def test_extension_jpg(self):
#        args = ['python3', 'run.py', '-c', '1', '-e', 'jpg']
#        subprocess.Popen(args, cwd="trdg/").wait()
#        self.assertTrue(False)
#        empty_directory('tests/out/')
#
#    def test_extension_png(self):
#        args = ['python3', 'run.py', '-c', '1', '-e', 'png']
#        subprocess.Popen(args, cwd="trdg/").wait()
#        self.assertTrue(False)
#        empty_directory('tests/out/')
#
#    def test_name_format_0(self):
#        args = ['python3', 'run.py', '-c', '1', '-na', '0']
#        subprocess.Popen(args, cwd="trdg/").wait()
#        self.assertTrue(False)
#        empty_directory('tests/out/')
#
#    def test_name_format_1(self):
#        args = ['python3', 'run.py', '-c', '1', '-na', '1']
#        subprocess.Popen(args, cwd="trdg/").wait()
#        self.assertTrue(False)
#        empty_directory('tests/out/')
#
#    def test_name_format_2(self):
#        args = ['python3', 'run.py', '-c', '1', '-na', '2']
#        subprocess.Popen(args, cwd="trdg/").wait()
#        self.assertTrue(False)
#        empty_directory('tests/out/')

if __name__ == "__main__":
    unittest.main()
