import streamlit as st
from common.general_prompts import game_instructions

st.set_page_config(layout='wide')

def go_back():
    st.session_state.stage = st.session_state.previous_stage

def view_instructions():
    st.session_state.previous_stage = st.session_state.stage
    st.session_state.stage = 'instructions'

def create_new_game():
    st.session_state.stage = 'new_game'



if 'stage' not in st.session_state:
    with st.spinner('Welcome to O.G.M.A, a ChatGPTTRPG! Please wait while O.G.M.A. inscribes its scripts...'):
        st.session_state.stage = 'title'

if st.session_state.stage == 'title':
    st.markdown(
        """
        <style>
        .centered-header {
            text-align: center;
            font-size: 4em; /* Adjust size for the main header */
            margin: 20px 0 10px 0; /* Margin above and below the header */
        }
        .centered-subheader {
            text-align: center;
            font-size: 2.5em; /* Adjust size for the subheader */
            color: gray; /* Optional: Change the color for distinction */
            margin: 0 0 20px 0; /* Margin below the subheader */
        }
        </style>
        <div class="centered-header">O.G.M.A.</div>
        <div class="centered-subheader">A ChatGPTTRPG</div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    with col3:
        st.button('New game', key='new_game_button', on_click=create_new_game)
        st.button('Load game', key='load_game_button')
        st.button('How to play', key='instructions_button', on_click=view_instructions)

elif st.session_state.stage == 'new_game':
    pass

elif st.session_state.stage == 'instructions':
    st.markdown(
        """
        <style>
        .centered-header {
            text-align: center;
            font-size: 4em; /* Adjust size for the main header */
            margin: 20px 0 10px 0; /* Margin above and below the header */
        }
        .centered-subheader {
            text-align: center;
            font-size: 2.5em; /* Adjust size for the subheader */
            color: gray; /* Optional: Change the color for distinction */
            margin: 0 0 20px 0; /* Margin below the subheader */
        }
        </style>
        <div class="centered-header">O.G.M.A.</div>
        <div class="centered-subheader">A ChatGPTTRPG</div>
        """,
        unsafe_allow_html=True,
    )

    st.write(game_instructions)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col3:
        st.button('Back', key='back_button', on_click=go_back)

else:
    st.write(f'Error! Stage {st.session_state.stage} not defined.')







