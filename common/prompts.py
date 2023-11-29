# system prompt for overall context

system_prompt = """You are an experienced game master with all of the knowledge of the world's tabletop RPGs at your disposal. You are here to guide the user through a RPG experience with humor, wit, excitement, and pathos. 
You are good natured and fair, but you're not afraid to let the player's choices result in negative consequences!"""

# prompt for creating new setting
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
Based on your interpretation of their personality quiz, please select EXACTLY {num_setting_categories} of the categories from the json object below for a roleplaying game setting. From each of those {num_setting_categories} categories, select exactly ONE subcategory. 
\n Here are the categories and subcategories for you to choose from, you must choose EXACTLY {num_setting_categories} categories and ONLY ONE SUBCATEGORY FROM EACH CATEGORY.
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

setting_generation_prompt = """The following are {num_setting_categories} setting subcategories chosen for a tabletop roleplaying game:
{setting_categories}
You will then combine the {num_setting_categories} selected subcategories to create a new, unique world for the game.
You will return a description of this world to the user. The format of this description should be the following:
1. SETTINGS: The {num_setting_categories} subcategories chosen.
2. INTRODUCTION: A greeting that captures the tone/culture of this world, welcoming the player and providing flavor.
3. WORLD DETAILS: The name of the world and a brief description of what life is like for the average person there.
4. CONFLICT: The predominant conflict is in this world, which may or may not be related to the player's role and the eventual campaign of the game.
5. FUN FACTS: A few fun facts about the world, its culture, or its inhabitants to get the player in the mood for the game.
"""

location_generation_prompt = """Below you will find the setting for a tabletop roleplaying game, along with some background information on that setting. Based on these details, please provide {num_locations} locations of interest within the setting.
Each location of interest should showcase the fascinating and diverse world of the setting, but fit together into a cohesive world--these places should be able to coexist in the same setting.

Return the list as a json object that includes location name, location physical description, and reason for location's importance.

Here are the details of the world: {setting_details}
"""

story_beat_generation_prompt_1 = """Below you will find the setting for a tabletop roleplaying game, along with some locations of interest within that setting and a description of the player's character. Based on these details, please write a story in {num_story_beats} acts. 
First, provide a description of where the player is starting in this world. What is their initial role? How do they fit into the world around them?
Second, provide a description of where the player will eventually end up if they're successful in this adventure. What will they achieve? How will their status change as a result of their actions?
Third, provide a 2-3 sentence story arc that will describe how the player will get from their starting point to that end point.
Fourth, provide a 2-3 sentence description of the primary conflict that the character is involved in.
Fifth and finally, provide a description of each of the {num_story_beats} acts and how each relates to the one before it and the one after, and which location of interest relates most to this beat.

Here are the setting details:
{setting_details}

Here are the locations of interest:
{locations_of_interest}

Here is info about the player's character:
{player_character}
"""

story_beat_generation_prompt_2 = """
Please output this as a json object using the following format:
{
  "storyBeginning": Description of the story's beginning,
  "storyEnding": Description of how the story ends,
  "storyArc": Overview of the story arc, including major developments,
  "storyMainConflict": Description of the main conflict in the story,
  "mainStoryBeats": [
    {
      "storyBeatNumber": 1,
      "description": Description of Story Beat 1,
      "primaryLocation": Primary location for Story Beat 1
    },
    {
      "storyBeatNumber": 2,
      "description": Description of Story Beat 2,
      "primaryLocation": Primary location for Story Beat 2
    },
    {
      "storyBeatNumber": 3,
      "description": Description of Story Beat 3,
      "primaryLocation": Primary location for Story Beat 3
    }
  ]
}

"""

# prompts for building a character
race_option_prompt_1 = """Below you will find the setting for a tabletop roleplaying game, along with some locations of interest within that setting. Based on these details, please create 4 possible playable races for the player to choose from, along with a brief description of each.

Here are the setting details:
{setting_details}
"""

race_option_prompt_2 = """
Please return your response as a json object in the following format:
{
    "Question": "Of the following races, which would you like your character to be?",
    "Options": {
      "A": {
        "Name": "RACE A NAME",
        "Description": "RACE A DESCRIPTION (1 sentence)"
      },
      "B": {
        "Name": "RACE B NAME",
        "Description": "RACE B DESCRIPTION (1 sentence)"
      },
      "C": {
        "Name": "RACE C NAME",
        "Description": "RACE C DESCRIPTION (1 sentence)"
      },
      "D": {
        "Name": "RACE D NAME",
        "Description": "RACE D DESCRIPTION (1 sentence)"
      }
    }
}
YOU MUST INCLUDE DESCRIPTIONS WITHIN THE JSON OBJECT, AND ONLY WITHIN THE JSON OBJECT.
"""

class_option_prompt_1 = """Below you will find the setting for a tabletop roleplaying game, along with some locations of interest within that setting and the player's chosen race. Based on these details, please create 4 possible playable classes for the player to choose from as their startintg class, along with a brief description of each.
Here are the setting details:
{setting_details}

Here is the player's race:
{player_race}
"""

class_option_prompt_2 = """
Please return your response as a json object in the following format:
{
    "Question": "Of the following starting classes, which would you like your character to be?",
    "Options": {
      "A": {
        "Name": "CLASS A NAME",
        "Description": "CLASS A DESCRIPTION (1 sentence)"
      },
      "B": {
        "Name": "CLASS B NAME",
        "Description": "CLASS B DESCRIPTION (1 sentence)"
      },
      "C": {
        "Name": "CLASS C NAME",
        "Description": "CLASS C DESCRIPTION (1 sentence)"
      },
      "D": {
        "Name": "CLASS D NAME",
        "Description": "CLASS D DESCRIPTION (1 sentence)"
      }
    }
}
YOU MUST INCLUDE DESCRIPTIONS WITHIN THE JSON OBJECT, AND ONLY WITHIN THE JSON OBJECT. Remember to consider the player's chosen race when designing the classes! Make sure the classes make sense given the player's chosen race.
"""

background_option_prompt_1 = """Below you will find the setting for a tabletop roleplaying game, along with some locations of interest within that setting, the player's chosen race, and the player's starting class. Based on these details, please create 4 possible backgrounds that serve as the player's origin, along with a brief description of each.
Here are the setting details:
{setting_details}

Here is the player's race:
{player_race}

Here is the player's starting class:
{player_class}
"""

background_option_prompt_2 = """
Please return your response as a json object in the following format:
{
    "Question": "Of the following backgrounds, which would you like your character to come from?",
    "Options": {
      "A": {
        "Name": "BACKGROUND A NAME",
        "Description": "BACKGROUND A DESCRIPTION (1 sentence)"
      },
      "B": {
        "Name": "BACKGROUND B NAME",
        "Description": "BACKGROUND B DESCRIPTION (1 sentence)"
      },
      "C": {
        "Name": "BACKGROUND C NAME",
        "Description": "BACKGROUND C DESCRIPTION (1 sentence)"
      },
      "D": {
        "Name": "BACKGROUND D NAME",
        "Description": "BACKGROUND D DESCRIPTION (1 sentence)"
      }
    }
}
YOU MUST INCLUDE DESCRIPTIONS WITHIN THE JSON OBJECT, AND ONLY WITHIN THE JSON OBJECT. Remember to consider the player's chosen race and class when designing the backgrounds! Make sure that the backgrounds make sense given the player's chosen race and class.
"""