class TTRPGPT:
    def __init__(self):
        self.data_to_save = ["setting_details", "locations_of_interest", "player_character", "story_beats"]
        self.selected_tone = 'balanced'
        self.setting_details = None
        self.locations_of_interest = None
        self.player_character = None
        self.story_beats = None