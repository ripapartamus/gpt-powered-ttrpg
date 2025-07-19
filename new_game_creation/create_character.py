import json
import streamlit as st
from gpt.gpt_api import gpt_call
from new_game_creation.create_character_prompts import *

class GenerateCharacter:
    def __init__(self, setting_details):
        self.setting_details = setting_details

    def create_character(self):
        if 'character_state' not in st.session_state:
            st.session_state['character_state'] = 'select_method'