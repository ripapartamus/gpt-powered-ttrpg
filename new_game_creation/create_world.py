import streamlit as st
from common.utils import safe_json_parse
from gpt.gpt_api import gpt_call
from new_game_creation.create_world_prompts import *
from common.config import num_quiz_questions, num_locations

class GenerateWorld:

    # the player is asked to select 2 setting categories, either by taking a personality quiz or selecting the categories directly
    # the player is then asked to choose the tone they want for the game
    # based on this, the world is generated

    def create_setting(self):
        # Initialize state variables
        if 'setting_state' not in st.session_state:
            st.session_state['creator_method'] = None
            st.session_state['first_category'] = None
            st.session_state['second_category'] = None
            st.session_state['responses'] = {}
            st.session_state['setting_state'] = 'select_method'

        # Handle states
        if st.session_state['setting_state'] == 'select_method':
            st.markdown(create_world_welcome_message)
            st.session_state['creator_method'] = st.radio(
                label="How would you like to generate your world?",
                options=["Take a personality quiz to generate the setting", "I'll choose the setting for myself"],
                index=None,
                label_visibility='hidden'
            )
            if st.session_state['creator_method']:
                st.button('Continue', on_click=lambda: st.session_state.update({'setting_state': 'category_select'}))

        elif st.session_state['setting_state'] == 'category_select':
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
                        st.write(f"{st.session_state['setting_categories']['Setting selections'][0]['Category']}--{st.session_state['setting_categories']['Setting selections'][0]['Subcategory']}")
                        st.write(f"{st.session_state['setting_categories']['Setting selections'][1]['Category']}--{st.session_state['setting_categories']['Setting selections'][1]['Subcategory']}")
                        st.button('Continue', on_click=lambda: st.session_state.update({'setting_state': 'select_tone'}))

            else:
                # Direct category selection
                categories = list(setting_options["categories"].keys())
                selected_categories = st.multiselect(
                    "Choose two setting categories:",
                    categories,
                    key="selected_categories",
                    max_selections=2
                )

                if len(selected_categories) == 2:
                    def select_subcategory(category):
                        subcategories = list(setting_options["categories"][category]["subcategories"])
                        return st.radio(
                            f"Select a subcategory for {category}:",
                            subcategories,
                            key=f"{category}_subcategory",
                            index=None
                        )

                    first_category, second_category = selected_categories
                    first_subcategory = select_subcategory(first_category)
                    second_subcategory = select_subcategory(second_category)

                    if first_subcategory and second_subcategory:
                        st.session_state['setting_categories'] = {
                            "Setting selections": [
                                {"Category": first_category, "Subcategory": first_subcategory},
                                {"Category": second_category, "Subcategory": second_subcategory}
                            ]
                        }
                        st.button('Continue', on_click=lambda: st.session_state.update({'setting_state': 'select_tone'}))

        elif st.session_state['setting_state'] == 'select_tone':
            st.session_state['selected_tone'] = st.radio(
                "Select the tone you'd like Ogma to take when weaving your story:",
                tone_options,
                index=None
            )
            if st.session_state['selected_tone']:
                st.session_state['selected_tone'] = st.session_state['selected_tone']
                st.button('Continue', on_click=lambda: st.session_state.update({'setting_state': 'create_setting'}))

        elif st.session_state['setting_state'] == 'create_setting':
            with st.spinner('Please wait while Ogma crafts a new world...'):
                st.session_state['setting_details'] = safe_json_parse(gpt_call(setting_generation_prompt_1.format(setting_categories=st.session_state['setting_categories'], tone=st.session_state['selected_tone']) + setting_generation_prompt_2))
                st.session_state['setting_details']['selected tone'] = st.session_state['selected_tone']
            with st.spinner(f'Please wait while Ogma fills your world with places to explore...'):
                st.session_state['setting_details']['main_locations'] = safe_json_parse(gpt_call(location_generation_prompt_1 + location_generation_prompt_2.format(num_locations=num_locations,setting_details=st.session_state['setting_details'])))

                st.session_state['world_description'] = st.session_state['setting_details'].pop("INTRODUCTION")
                st.session_state['world_description'] += '\n\n'
                st.session_state['world_description'] += st.session_state['setting_details']['WORLD_DETAILS']
                st.session_state['world_description'] += '\n\n'
                st.session_state['world_description'] += st.session_state['setting_details']['CONFLICT']
                st.session_state['world_description'] += f"\n\nSome facts about {st.session_state['setting_details']['WORLD_NAME']}:\n"
                for fact in st.session_state['setting_details']['FUN_FACTS']:
                    st.session_state['world_description'] += f'\n- {fact}\n'
                st.session_state['world_description'] += f"\n\nSome key locations:\n"
                for location in st.session_state['setting_details']['main_locations']:
                    st.session_state['world_description'] += f'\n- {location['NAME']}: {location['DESCRIPTION']} {location['IMPORTANCE']}\n'

                st.markdown(st.session_state['world_description'])

        #     st.button('Continue to character creation', on_click=lambda: st.session_state.update({'setting_state': 'end'}))
        #
        # elif st.session_state['setting_state'] == 'end':
            keys_to_remove = [
                'setting_state',
                'quiz',
                'responses',
                'first_category',
                'second_category',
                'setting_categories',
                'selected_tone',
                'creator_method',
            ]

            for key in keys_to_remove:
                st.session_state.pop(key, None)

            return

        else:
            raise Exception(f'{st.session_state['setting_state']} not valid world creation state')
