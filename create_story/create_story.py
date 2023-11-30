from common.utils import safe_json_parse
from gpt_api import gpt_call
from common.config import num_story_beats
from create_story.create_story_prompts import *

# putting everything together to form a story
class GenerateStory:
    def __init__(self, selected_tone, setting_details, locations_of_interest, player_character):
        self.selected_tone = selected_tone
        self.setting_details = setting_details
        self.locations_of_interest = locations_of_interest
        self.player_character = player_character

    def get_story_beats(self):
        print("\nNow, we'll begin writing the story. Please wait a moment...\n\n")
        story_prompt_full = story_beat_generation_prompt_1.format(num_story_beats=num_story_beats,
                                                                  setting_details=self.setting_details,
                                                                  locations_of_interest=self.locations_of_interest,
                                                                  player_character=self.player_character) + story_beat_generation_prompt_2
        self.story_beats = gpt_call(story_prompt_full, tone=self.selected_tone)
        self.story_beats = safe_json_parse(self.story_beats)
        return self.story_beats