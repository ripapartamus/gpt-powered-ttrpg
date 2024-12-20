import streamlit as st
from new_game_creation.new_game_creator import GenerateWorld

world = GenerateWorld()

world.create_setting()