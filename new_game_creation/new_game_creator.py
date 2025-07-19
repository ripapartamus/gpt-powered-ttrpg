import streamlit as st
from new_game_creation.create_world import GenerateWorld
from new_game_creation.create_character import GenerateCharacter
from new_game_creation.create_story import GenerateStory

class NewGameCreator:

    def create_new_game(self):
        if 'new_game_state' not in st.session_state:
            st.session_state['setting_details'] = None
            st.session_state['character_details'] = None
            st.session_state['new_game_state'] = 'generate_world'

        if st.session_state['new_game_state'] == 'generate_world':
            world = GenerateWorld()
            world.create_setting()
            if st.session_state['setting_details']:
                st.button('Continue to character creation', on_click=lambda: st.session_state.update({'new_game_state': 'create_character'}))
        elif st.session_state['new_game_state'] == 'create_character':
            character = GenerateCharacter(st.session_state['setting_details'])
            character.create_character()
            if st.session_state['character_details']:
                st.button('Start your story', on_click=lambda: st.session_state.update({'new_game_state': 'create_story'}))
        elif st.session_state['new_game_state'] == 'create_story':
            st.session_state['new_game_state'] = 'end'
        elif st.session_state['new_game_state'] == 'end':
            return
        else:
            raise Exception(f'{st.session_state['new_game_state']} not valid new game creation state')

