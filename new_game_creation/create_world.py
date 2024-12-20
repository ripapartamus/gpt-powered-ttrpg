import streamlit as st
import json
from common.utils import safe_json_parse
from gpt.gpt_api import gpt_call
from new_game_creation.create_world_prompts import *
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

    # the player is asked to select 2 setting categories, either by taking a personality quiz or selecting the categories directly
    # the player is then asked to choose the tone they want for the game
    # based on this, the world is generated

    def create_setting(self):
        # Initialize state variables
        if 'state' not in st.session_state:
            st.session_state['state'] = 'select_method'
        if 'creator_method' not in st.session_state:
            st.session_state['creator_method'] = None
        if 'first_category' not in st.session_state:
            st.session_state['first_category'] = None
        if 'second_category' not in st.session_state:
            st.session_state['second_category'] = None
        if 'responses' not in st.session_state:
            st.session_state['responses'] = {}

        # Handle states
        if st.session_state['state'] == 'select_method':
            st.write(create_world_welcome_message)
            st.session_state['creator_method'] = st.radio(
                label="How would you like to generate your world?",
                options=[
                    "Take a personality quiz to generate the setting",
                    "I'll choose the setting for myself"
                ],
                index=None,
                key='cm',
                label_visibility='hidden'
            )
            if st.button('Continue'):
                st.session_state['state'] = 'category_select'

        elif st.session_state['state'] == 'category_select':
            if st.session_state['creator_method'] == "Take a personality quiz to generate the setting":
                # Quiz handling
                if 'quiz' not in st.session_state:
                    with st.spinner('Please wait while Ogma creates a new personality quiz...'):
                        quiz_prompt_full = setting_quiz_prompt.format(
                            setting_options=setting_options,
                            num_quiz_questions=num_quiz_questions
                        ) + setting_quiz_format
                        quiz = safe_json_parse(gpt_call(quiz_prompt_full))
                        st.session_state['quiz'] = quiz

                quiz = st.session_state['quiz']
                st.subheader("Ogma will use the following questions to select the setting most suited to you.")
                for question, options in quiz.items():
                    st.session_state['responses'][question] = st.radio(
                        options['Question'],
                        options=list(options['Options'].values()),
                        key=question,
                        index=None
                    )

                all_answered = all(st.session_state['responses'].values())
                if all_answered:
                    if st.button("Submit responses"):
                        with st.spinner('Please wait while Ogma selects the best setting for you...'):
                            setting_select_prompt_full = setting_selection_prompt_1.format(
                                quiz_and_results=st.session_state['responses'],
                                setting_options=setting_options
                            ) + setting_selection_prompt_2
                            self.setting_categories = safe_json_parse(gpt_call(setting_select_prompt_full))
                            st.session_state['setting_categories'] = self.setting_categories
                        st.write('Ogma has selected the following categories for your story:')
                        st.write(f"{st.session_state['setting_categories']["Setting selections"][0]["Category"]}--{st.session_state['setting_categories']["Setting selections"][0]["Subcategory"]}")
                        st.write(f"{st.session_state['setting_categories']["Setting selections"][1]["Category"]}--{st.session_state['setting_categories']["Setting selections"][1]["Subcategory"]}")
                        st.button('Continue', on_click=lambda: st.session_state.update({'state': 'select_tone'}))
            else:
                # Direct category selection
                categories = list(setting_options["categories"].keys())
                if not st.session_state['first_category']:
                    st.session_state['first_category'] = st.radio(
                        "Choose your first setting category:",
                        categories,
                        key="first_category"
                    )
                elif not st.session_state['second_category']:
                    categories.remove(st.session_state['first_category'])
                    st.write(f"You have selected {st.session_state['first_category']} as your first category.")
                    st.session_state['second_category'] = st.selectbox(
                        "Choose your second setting category:",
                        categories,
                        key="second_category"
                    )
                else:
                    # Subcategory selection
                    def select_subcategory(category):
                        subcategories = list(setting_options["categories"][category]["subcategories"])
                        return st.radio(f"Select a subcategory for {category}:", subcategories,
                                        key=f"{category}_subcategory")

                    first_subcategory = select_subcategory(st.session_state['first_category'])
                    second_subcategory = select_subcategory(st.session_state['second_category'])

                    if first_subcategory and second_subcategory:
                        self.setting_categories = {
                            "Setting selections": [
                                {"Category": st.session_state['first_category'], "Subcategory": first_subcategory},
                                {"Category": st.session_state['second_category'], "Subcategory": second_subcategory}
                            ]
                        }
                        st.session_state['setting_categories'] = self.setting_categories

                        st.button('Continue', on_click=lambda: st.session_state.update({'state': 'select_tone'}))

        elif st.session_state['state'] == 'select_tone':
            st.session_state.selected_tone = st.radio(
                "Select the tone you'd like Ogma to take when weaving your story:",
                tone_options,
                index=None
            )
            if st.session_state.selected_tone:
                st.session_state['selected_tone'] = st.session_state.selected_tone
                st.button('Continue', on_click=lambda: st.session_state.update({'state': 'create_setting'}))

        elif st.session_state['state'] == 'create_setting':
            st.write(f'Your setting: {st.session_state['setting_categories']["Setting selections"][0]["Category"]}--{st.session_state['setting_categories']["Setting selections"][0]["Subcategory"]}; {st.session_state['setting_categories']["Setting selections"][1]["Category"]}--{st.session_state['setting_categories']["Setting selections"][1]["Subcategory"]}')
            st.write( f"Your tone: {st.session_state.selected_tone}")
            with st.spinner('Please wait while Ogma crafts a new world...'):
                setting_prompt_full = setting_generation_prompt_1.format(
                    setting_categories=st.session_state['setting_categories']
                ) + setting_generation_prompt_2
                self.setting_details = safe_json_parse(gpt_call(setting_prompt_full, tone=st.session_state['selected_tone']))

                self.setting_details = safe_json_parse(self.setting_details)
                self.player_intro = self.setting_details.pop("INTRODUCTION")
                st.session_state.setting_details = self.setting_details
                st.write(self.player_intro)
                st.write("\nHere is some information about the world you will inhabit:\n")
                for key, value in self.setting_details.items():
                    if key not in ['SETTINGS', 'WORLD_NAME']:
                        st.write(f"{key}: {value}\n")
            st.button('Finish', on_click=lambda: st.session_state.update({'state': 'end'}))

        else:
            raise Exception(f'{st.session_state['state']} not valid world creation state')