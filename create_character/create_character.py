import json
from gpt_api import gpt_call
from create_character.create_character_prompts import *

class GenerateCharacter:
    def __init__(self, selected_tone, setting_details, locations_of_interest):
        self.selected_tone = selected_tone
        self.setting_details = setting_details
        self.locations_of_interest = locations_of_interest
        self.race_options = None
        self.class_options = None
        self.background_options = None
        self.player_character = []
        self.player_race = None
        self.player_class = None
        self.player_background = None

    # setting up player character preferences

    def GenerateCharacter(self):
        print(create_character_welcome_message)
        self.get_player_gender()
        print("\nGenerating player races...\n")
        self.get_player_race()
        print("\nGenerating player classes...\n")
        self.get_player_class()
        print("\nGenerating player backgrounds...\n")
        self.get_player_background()
        self.get_player_name()

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
                                                                   locations_of_interest=self.locations_of_interest,
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

