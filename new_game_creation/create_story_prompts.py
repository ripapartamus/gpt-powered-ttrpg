# prompts for generating story information

story_beat_generation_prompt_1 = """Below you will find the setting for a tabletop role-playing game, along with locations of interest and a description of the player's character. Based on these details, please write a story in {num_story_beats} acts. 
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
    ...
  ]
}

"""
