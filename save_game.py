import os
import json
import re

class SaveGame:
    def __init__(self):
        self.data_to_save = ["setting_details", "locations_of_interest", "player_character", "story_beats"]

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