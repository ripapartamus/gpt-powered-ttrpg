import json
from common.utils import safe_json_parse
from gpt_api import gpt_call
from create_world.create_world_prompts import *
from common.general_prompts import tone_options
from common.config import num_quiz_questions, num_locations

class GenerateWorld:
    def __init__(self):
        # initialize variables
        self.setting_categories = None
        self.selected_tone = None
        self.player_intro = None
        self.setting_details = None
        self.locations_of_interest = None

    def world_creator(self):
        print(create_world_welcome_message)
        self.create_setting()
        print(self.player_intro)
        print("\nHere is some information about the world you will inhabit:\n")
        for key, value in self.setting_details.items():
            # Print the key and value if the key is not 'SETTINGS' or 'WORLD_NAME'
            if key not in ['SETTINGS', 'WORLD_NAME']:
                print(f"{key}: {value}\n")
        print('\nPlease wait while we fill the world with interesting places...')
        self.get_locations()
        print("\nWorld map has been generated!\n")


# the player is asked to select 2 setting categories, either by taking a personality quiz or selecting the categories directly
# the player is then asked to choose the tone they want for the game
# based on this, the world is generated

    def create_setting(self):
        print("""How would you like to generate your world?""")
        print("1. Take a personality quiz to generate the setting")
        print("2. I'll chose the setting for myself")
        user_response = input("Your answer (1/2): ").strip().upper()

        while user_response not in ["1", "2"]:
            print("Invalid option. Please choose 1 or 2.")
            user_response = input("Your answer (1/2): ").strip().upper()

        if user_response == "1":
            self.get_setting_categories()
        else:
            self.user_select_setting_categories()

        self.selected_tone = self.get_tone()

        print('\nGenerating your world...\n')

        setting_prompt_full = setting_generation_prompt_1.format(setting_categories = self.setting_categories) + setting_generation_prompt_2
        self.setting_details = json.loads(gpt_call(setting_prompt_full, tone = self.selected_tone))

        self.setting_details = safe_json_parse(self.setting_details)

        self.player_intro = self.setting_details.pop("INTRODUCTION")
        self.setting_details = self.setting_details

        return self.player_intro, self.setting_details

    def get_setting_categories(self):
        completed_quiz = self.give_setting_quiz()
        print('\nChoosing the setting most suited to your responses...')
        setting_select_prompt_full = setting_selection_prompt_1.format(quiz_and_results = completed_quiz, setting_options = setting_options) + setting_selection_prompt_2
        self.setting_categories = gpt_call(setting_select_prompt_full, tone = "balanced")
        return self.setting_categories

    def get_setting_quiz(self):
        quiz_prompt_full = setting_quiz_prompt.format(setting_options = setting_options, num_quiz_questions = num_quiz_questions) + setting_quiz_format
        response = gpt_call(quiz_prompt_full, tone = "balanced")
        return response

    def give_setting_quiz(self):
        # Parse the JSON string
        quiz = self.get_setting_quiz()
        quiz = json.loads(quiz)

        print("\nThe following questions will be used to select the setting most suited to you.\n")

        # Iterate through each question
        for key, value in quiz.items():
            print(f"{value['Question']}")
            for option, text in value['Options'].items():
                print(f"  {option}: {text}")

            # Get user response
            user_response = input("Your answer (A/B/C/D): ").strip().upper()
            while user_response not in value['Options']:
                print("Invalid option. Please choose A, B, C, or D.")
                user_response = input("Your answer (A/B/C/D): ").strip().upper()

            # Append the response to the JSON object
            quiz[key]['User Response'] = user_response

        quiz_with_responses = json.dumps(quiz, indent=4)

        return quiz_with_responses

    def user_select_setting_categories(self):
        print(
            "\n\nOkay! Let's get started! You will be selecting two of these setting categories to create your world. You will then select a specific setting subcategory within those two.\n")

        def get_user_selection(options):
            for i, option in enumerate(options, start=1):
                print(f"{i}. {option}")
            while True:
                try:
                    user_input = int(input(f"Choose a number between 1 and {len(options)}: "))
                    if 1 <= user_input <= len(options):
                        return user_input - 1
                    else:
                        print(f"Please enter a number between 1 and {len(options)}.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        categories = list(setting_options["categories"].keys())

        # Select first category
        print("\nPlease select your first setting category from the following options:\n")
        first_category_index = get_user_selection(categories)
        first_category = categories.pop(first_category_index)

        # Select second category
        print("\nNow select a second category from the following options:\n")
        second_category_index = get_user_selection(categories)
        second_category = categories[second_category_index]

        # Select subcategories
        def select_subcategory(category):
            subcategories = list(setting_options["categories"][category]["subcategories"])
            print(f"\nPlease select from the following {category} subcategories:\n")
            subcategory_index = get_user_selection(subcategories)
            return subcategories[subcategory_index]

        first_subcategory = select_subcategory(first_category)
        second_subcategory = select_subcategory(second_category)

        self.setting_categories = {
            "Setting selections": [
                {"Category": first_category, "Subcategory": first_subcategory},
                {"Category": second_category, "Subcategory": second_subcategory}
            ]
        }
        return self.setting_categories

    def get_tone(self):
        print("\nI prefer the tone of role-playing games to be:")
        for i, option in enumerate(tone_options, start=1):
            print(f"{i}. {option}")
        while True:
            try:
                user_input = int(input(f"Choose a number between 1 and {len(tone_options)}: "))
                if 1 <= user_input <= len(tone_options):
                    return tone_options[user_input - 1]
                else:
                    print(f"Please enter a number between 1 and {len(tone_options)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # given the tone of the campaign and setting, several locations of interest are generated. These help inform story and character background later
    def get_locations(self):
        location_prompt_full = location_generation_prompt.format(setting_details = self.setting_details, num_locations = num_locations)
        self.locations_of_interest = gpt_call(location_prompt_full, tone = self.selected_tone)
        return self.locations_of_interest

