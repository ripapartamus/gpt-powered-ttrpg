from create_world.create_world import GenerateWorld
from create_character.create_character import GenerateCharacter
from create_story.create_story import GenerateStory
import os
import json
import re
from common.general_prompts import startup_welcome_message

# starting up the game
class TTRPGPT:
    def __init__(self):
        self.data_to_save = ["setting_details", "locations_of_interest", "player_character", "story_beats"]
        self.selected_tone = 'balanced'
        self.setting_details = None
        self.locations_of_interest = None
        self.player_character = None
        self.story_beats = None

    def run_game(self):
        print(startup_welcome_message)
        self.load_or_new_game()

    def load_or_new_game(self):
        print("Would you like to create a new game, or load a saved game?")
        print("1. New game")
        print("2. Load game")
        user_response = input("Your answer (1/2): ")
        while user_response not in ["1", "2"]:
            print("Invalid option. Please choose 1 or 2.")
            user_response = input("Your answer (1/2): ")
        if user_response == "1":
            self.new_game()
        else:
            self.load_game()

    def load_game(self):
        print("Coming soon!")

    def new_game(self):
        # world creation
        world = GenerateWorld()
        world.world_creator()
        self.selected_tone = world.selected_tone
        self.setting_details = world.setting_details
        self.locations_of_interest = world.locations_of_interest

        # character creation
        character = GenerateCharacter(self.selected_tone, self.setting_details, self.locations_of_interest)
        character.GenerateCharacter()
        self.player_character = character.player_character

        # story creation
        story = GenerateStory(self.selected_tone, self.setting_details, self.locations_of_interest, self.player_character)
        story.get_story_beats()
        self.story_beats = story.story_beats
        print(self.story_beats["storyBeginning"])
        print("\n\nLet's get started!")

        # save all this info
        self.save_game_data()

    # saving game data
    def save_game_data(self):
        # Prompt for subfolder name with validation
        subfolder_name = self.get_valid_subfolder_name()

        # Create the 'save_game' directory and the subfolder
        subfolder_path = self.create_subfolder(subfolder_name)

        # Define the list of data attributes to save

        # Iterate and save each data attribute
        for data_name in self.data_to_save:
            self.save_data_attribute(subfolder_path, data_name)

        print(f"Game data saved in {subfolder_path}")

    def get_valid_subfolder_name(self):
        while True:
            subfolder_name = input("Enter a name for your game save subfolder: ").strip()
            # Check if the folder name is valid
            if re.match("^[a-zA-Z0-9_\- ]+$", subfolder_name):
                return subfolder_name
            else:
                print("Invalid folder name. Please use only letters, numbers, underscores, hyphens, and spaces.")

    def create_subfolder(self, subfolder_name):
        save_dir = "save_game"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        subfolder_path = os.path.join(save_dir, subfolder_name)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)

        return subfolder_path

    def save_data_attribute(self, subfolder_path, data_name):
        file_path = os.path.join(subfolder_path, f"{data_name}.json")
        with open(file_path, 'w') as file:
            data = getattr(self, data_name, {})
            json.dump(data, file, indent=4)