import json
from gpt_api import gpt_call
from common.prompts import (setting_quiz_prompt, setting_quiz_format, setting_selection_prompt_1, setting_selection_prompt_2, tone_options, setting_generation_prompt_1, setting_generation_prompt_2, setting_options, location_generation_prompt,\
                            race_option_prompt_1, race_option_prompt_2, class_option_prompt_1, class_option_prompt_2, background_option_prompt_1, background_option_prompt_2, story_beat_generation_prompt_1, story_beat_generation_prompt_2)
from common.config import num_quiz_questions, num_locations, num_story_beats

#TODO: add a check for whether a json is actually a json or just a string

class GenerateStory:
    def __init__(self):
        # prompts
        self.setting_quiz_prompt = setting_quiz_prompt
        self.setting_quiz_format = setting_quiz_format
        self.setting_options = setting_options
        self.setting_selection_prompt_1 = setting_selection_prompt_1
        self.setting_selection_prompt_2 = setting_selection_prompt_2
        self.location_generation_prompt = location_generation_prompt
        self.race_option_prompt_1 = race_option_prompt_1
        self.race_option_prompt_2 = race_option_prompt_2
        self.class_option_prompt_1 = class_option_prompt_1
        self.class_option_prompt_2 = class_option_prompt_2
        self.background_option_prompt_1 = background_option_prompt_1
        self.background_option_prompt_2 = background_option_prompt_2
        self.story_beat_generation_prompt_1 = story_beat_generation_prompt_1
        self.story_beat_generation_prompt_2 = story_beat_generation_prompt_2
        # config
        self.num_quiz_questions = num_quiz_questions
        self.num_locations = num_locations
        self.num_story_beats = num_story_beats
        # initialize variables
        self.setting_categories = None
        self.selected_tone = None
        self.player_intro = None
        self.setting_details = None
        self.locations_of_interest = None
        self.race_options = None
        self.class_options = None
        self.background_options = None
        self.player_character = []
        self.player_race = None
        self.player_class = None
        self.player_background = None
        self.story_beats = None

    def create_setting(self):
        print("""How would you like to generate your new world?""")
        print("A. Take a personality quiz generate a setting")
        print("B. I'll chose the setting for myself")
        user_response = input("Your answer (A/B): ").strip().upper()

        while user_response not in ["A", "B"]:
            print("Invalid option. Please choose A or B.")
            user_response = input("Your answer (A/B): ").strip().upper()

        if user_response == "A":
            self.get_setting_categories()
        else:
            self.user_select_setting_categories()

        self.selected_tone = self.get_tone()

        setting_prompt_full = setting_generation_prompt_1.format(setting_categories = self.setting_categories) + setting_generation_prompt_2
        self.setting_details = json.loads(gpt_call(setting_prompt_full, tone = self.selected_tone))

        self.player_intro = self.setting_details.pop("INTRODUCTION")
        self.setting_details = self.setting_details

        return self.player_intro, self.setting_details

    def get_setting_categories(self):
        completed_quiz = self.give_setting_quiz()
        setting_select_prompt_full = setting_selection_prompt_1.format(quiz_and_results = completed_quiz, setting_options = self.setting_options, num_setting_categories = self.num_setting_categories) + setting_selection_prompt_2
        self.setting_categories = gpt_call(setting_select_prompt_full, tone = "balanced")
        return self.setting_categories

    def get_setting_quiz(self):
        quiz_prompt_full = self.setting_quiz_prompt.format(setting_options = self.setting_options, num_quiz_questions = self.num_quiz_questions) + self.setting_quiz_format
        response = gpt_call(quiz_prompt_full, tone = "balanced")
        return response

    def give_setting_quiz(self):
        # Parse the JSON string
        quiz = self.get_setting_quiz()
        quiz = json.loads(quiz)

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

        categories = list(self.setting_options["categories"].keys())

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
            subcategories = list(self.setting_options["categories"][category]["subcategories"])
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

    def get_locations(self):
        location_prompt_full = location_generation_prompt.format(setting_details = self.setting_details, num_locations = self.num_locations)
        self.locations_of_interest = gpt_call(location_prompt_full, tone = self.selected_tone)
        return self.locations_of_interest

    # setting up player character preferences

    def display_character_options(self, option_json, trait):
        option_json = json.loads(option_json)
        print('\n' + option_json["Question"])
        for key, option in option_json["Options"].items():
            print(f"{key}: {option['Name']} - {option['Description']}")

        user_response = input("Please enter your choice (A, B, C, D): ").strip().upper()
        while user_response not in option_json['Options']:
            print("Invalid option. Please choose A, B, C, or D.")
            user_response = input("Your answer (A/B/C/D): ").strip().upper()

        chosen_option = option_json['Options'][user_response]
        concatenated_choice = f"{chosen_option['Name']} - {chosen_option['Description']}"
        self.player_character.append({"Trait": trait, "Description": concatenated_choice})

        return concatenated_choice

    def get_player_gender(self):
        question_text = "What are your preferred pronouns?"
        print(question_text)
        print("A: She/her")
        print("B: He/him")
        print("C: They/them")
        user_response = input("Your answer (A/B/C): ").strip().upper()
        while user_response not in ["A", "B", "C"]:
            print("Invalid option. Please choose A, B, or C.")
            user_response = input("Your answer (A/B/C): ").strip().upper()
        if user_response == "A":
            player_choice = "A: She/Her"
        elif user_response == "B":
            player_choice = "B: He/Him"
        else:  # user_response == "C"
            player_choice = "C: They/Them"

        self.player_character.append({"Trait": "Gender", "Description": player_choice})

    def get_player_race(self):
        race_prompt_full = race_option_prompt_1.format(setting_details=self.setting_details) + race_option_prompt_2
        race_options = gpt_call(race_prompt_full, tone = self.selected_tone)
        # self.player_race = self.display_character_options(self, race_options, "Player race")
        self.player_race = self.display_character_options(option_json = race_options, trait = "Player race")

    def get_player_class(self):
        class_prompt_full = class_option_prompt_1.format(setting_details=self.setting_details,
                                                         player_race=self.player_race) + class_option_prompt_2
        class_options = gpt_call(class_prompt_full, tone = self.selected_tone)
        self.player_class = self.display_character_options(option_json = class_options, trait = "Player starting class")

    def get_player_background(self):
        background_prompt_full = background_option_prompt_1.format(setting_details=self.setting_details,
                                                                   player_race=self.player_race,
                                                                   player_class = self.player_class) + background_option_prompt_2
        background_options = gpt_call(background_prompt_full, tone = self.selected_tone)
        self.player_background = self.display_character_options(option_json = background_options, trait = "Player background")

    def get_player_name(self):
        question_text = "What is your name?"
        print('\n' + question_text)
        while True:
            user_response = input("(Maximum 20 characters): ")
            if len(user_response) <= 20:
                break
            else:
                print("Name is too long. Please enter a shorter name.")
        self.player_character.append({"Trait": "Player name", "Description": user_response})

    def get_player_info(self):
        self.get_player_gender()
        self.get_player_race()
        self.get_player_class()
        self.get_player_background()
        self.get_player_name()

    # putting everything together to form a story
    def get_story_beats(self):
        story_prompt_full = story_beat_generation_prompt_1.format(num_story_beats = self.num_story_beats, setting_details = self.setting_details, locations_of_interest = self.locations_of_interest, player_character = self.player_character) + story_beat_generation_prompt_2
        self.story_beats = gpt_call(story_prompt_full, tone = self.selected_tone)
        return self.story_beats
