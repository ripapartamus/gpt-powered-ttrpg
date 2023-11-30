# prompt for creating new setting
create_world_welcome_message = """It's the dawn of a new world! 
\nEvery aspect of this game will be totally unique to you--the setting, the story, the characters, it will all be generated based on your choices.\n"""

setting_quiz_prompt = """Your will ask a user about their preferences, and from those preferences craft a setting for a tabletop RPG setting that suits their tastes. The catch is, you'll be asking them about preferences that don't directly relate to games!

Your first task is to ask the user to take a short {num_quiz_questions}-question personality quiz, in the style of Buzzfeed or similar quizzes. This SHOULD NOT RELATE TO RPGS OR GAMES IN ANY WAY. This quiz will help to select from the following setting options:
\n {setting_options}
\n Please return the quiz as a json object with the following format: \n"""

setting_quiz_format = """{
  "Question 1": {
    "Question": QUESTION TEXT HERE,
    "Options": {
      "A": OPTION A HERE,
      "B": OPTION B HERE,
      "C": OPTION C HERE,
      "D": OPTION D HERE
    },
  etc
  }"""

setting_selection_prompt_1 = """The following is a list of personality quiz questions and the user's responses: 
\n {quiz_and_results}
Based on your interpretation of their personality quiz, please select EXACTLY TWO of the categories from the json object below for a role-playing game setting. From each of those two categories, select exactly ONE subcategory. 
\n Here are the categories and subcategories for you to choose from, you must choose EXACTLY TWO categories and ONLY ONE SUBCATEGORY FROM EACH CATEGORY.
\n {setting_options}"""

setting_selection_prompt_2 = """
Please use the following json format:
{
  "Setting selections": [
    {
      "Category": (your first category selection),
      "Subcategory": (your first subcategory selection)
    },
    {
      "Category": (your second category selection),
      "Subcategory": (your second subcategory selection)
    }
  ]
}
"""

setting_options = {
  "categories": {
    "Fantasy": {
      "subcategories": ["High fantasy", "Low fantasy", "Rainbow fantasy", "Talking animals"]
    },
    "Sci-Fi": {
      "subcategories": ["Space opera", "Hard sci-fi", "Colonizing alien worlds"]
    },
    "Mythology": {
      "subcategories": ["Egyptian mythology", "Aztec mythology", "Norse mythology", "Greco-Roman mythology", "Celtic mythology", "Japanese mythology", "Polynesian mythology", "Judeo-Christian mythology"]
    },
    "Punk": {
      "subcategories": ["Cyberpunk", "Steampunk", "Street punk"]
    },
    "Horror": {
      "subcategories": ["Gothic horror", "Eldtritch horror", "Vampire"]
    },
    "Stylish": {
      "subcategories": ["Film noir", "Anime", "X-Treme"]
    },
    "Cinematic": {
      "subcategories": ["Old West", "Pirate", "Post-apocalyptic", "Superhero", "Kung fu"]
    }
  }
}

setting_generation_prompt_1 = """The following are 2 setting categories chosen for a tabletop role-playing game:
{setting_categories}
You will then combine the selected subcategories to create a new, unique world for the game.
"""

setting_generation_prompt_2 = """
You will return a description of this world to the user. The format of this description should be a json object with the following structure:
{
  "SETTINGS": The setting categories chosen,
  "WORLD_NAME": The name of the world,
  "INTRODUCTION": A greeting that captures the tone/culture of this world, welcoming the player and providing flavor,
  "WORLD_DETAILS": A brief description of what life is like for the average person there,
  "CONFLICT": The predominant conflict in this world, which may or may not be related to the player's role and the eventual campaign of the game,
  "FUN_FACTS": [
    Fun fact 1 about the world, its culture, or its inhabitants,
    Fun fact 2 about the world, its culture, or its inhabitants,
    Fun fact 3 about the world, its culture, or its inhabitants
  ]
}
"""

location_generation_prompt = """Below you will find the setting for a tabletop role-playing game, along with some background information on that setting. Based on these details, please provide {num_locations} locations of interest within the setting.
Each location of interest should showcase the fascinating and diverse world of the setting, but fit together into a cohesive world--these places should be able to coexist in the same setting.

Return the list as a json object that includes location name, location physical description, and reason for location's importance.

Here are the details of the world: {setting_details}
"""