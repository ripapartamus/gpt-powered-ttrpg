
# prompts for building a character
create_character_welcome_message = """Your journey begins! Now you'll decide how you fit in.\n"""

race_option_prompt_1 = """Below you will find the setting for a tabletop role-playing game, along with some locations of interest within that setting. Based on these details, please create 4 possible playable races for the player to choose from, along with a brief description of each.

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

class_option_prompt_1 = """Below you will find the setting for a tabletop role-playing game, along with the player's chosen race. Based on these details, please create 4 possible playable classes for the player to choose from as their startintg class, along with a brief description of each.
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

background_option_prompt_1 = """Below you will find the setting for a tabletop role-playing game, along with some locations of interest within that setting, the player's chosen race, and the player's starting class. Based on these details, please create 4 possible backgrounds that serve as the player's origin, along with a brief description of each.
Here are the setting details:
{setting_details}

Here is the player's race:
{player_race}

Here is the player's starting class:
{player_class}

Here are some locations of interest:
{locations_of_interest}
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