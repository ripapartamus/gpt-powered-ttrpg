health_status_prompt = """You are an agent designed to inform a tabletop roleplaying game how injured they are IN QUALITATIVE TERMS ONLY based on the following information:
Player health currently  9 out of 10 total hitpoints
Player has "burned" status effect
Player asks: "How hurt am I?"
DO NOT REPORT THE PLAYER'S CURRENT OR TOTAL HITPOINTS, only give a 1-sentence qualitative response.

Always use the second person when delivering this status to maintain immersion."""



create_racial_features_prompt = """You are an agent that helps create player characters for a tabletop RPG. For each of the following player races below, please provide 2 racial traits that set them apart from each other.

A: Mictlantecuhtli - Descendants of the ancient god of the underworld, Mictlantecuhtli. These beings possess a natural affinity for necromancy and can commune with the spirits of the deceased.
B: Chalchiuhtlicue - Descendants of the goddess of water and rivers, Chalchiuhtlicue. These beings are able to manipulate water and control the weather, making them formidable in both combat and survival situations.
C: Quetzalcoatl - Descendants of the feathered serpent god, Quetzalcoatl. These beings have the ability to transform into a giant feathered serpent and possess heightened senses, agility, and wisdom.
D: Xolotl - Descendants of the god of lightning and death, Xolotl. These beings have the power to manipulate electricity and possess incredible speed and agility.

Each race should have 1 beneficial trait and 1 negative trait that differentiate them from the others. These should be traits that would affect mechanical aspects of the game BUT ONLY DESCRIBE THEM IN QUALITATIVE TERMS to maintain immersion. Please output as a json object in the following format:
{
  "Race A name": {
    "Positive trait name": "Trait Description",
    "Negative trait name": "Trait Description"
  },
"Race B name": {
    "Positive trait name": "Trait Description",
    "Negative trait name": "Trait Description"
  }
"""

create_class_features_prompt = """You are an agent that helps create player characters for a tabletop RPG. For each of the following player starting classes below, please provide 2 class traits that set them apart from each other.

A: Spirit Channeler - Harness the power of the spirits to heal and protect your allies, while also wielding necromantic abilities to strike fear into the hearts of your enemies.
B: Shadowblade - Master the art of stealth and assassination, utilizing your necromantic powers to manipulate shadows and strike down your foes with deadly precision.
C: Tempest Caller - Command the forces of nature and channel the wrath of the storm gods, using your necromantic powers to control the weather and devastate your enemies.
D: Artifact Hunter - Specialize in locating and utilizing ancient relics and artifacts, using your necromantic abilities to awaken their hidden powers and turn the tide of battle.

Each class should have 1 trait is a stat bonus to and 1trait that is a stat penalty to that differentiate them from the others. These should be stats that would affect mechanical aspects of the game. EACH TRAIT SHOULD ONLY IMPACT 1 STAT. Please output as a json object in the following format:

{
  "Class A name": {
    "Positive trait name": "Trait Description",
    "Negative trait name": "Trait Description"
  },
"Class B name": {
    "Positive trait name": "Trait Description",
    "Negative trait name": "Trait Description"
  }
 ...
}
"""

background_trait_prompt = """You are an agent that helps create player characters for a tabletop RPG in the following setting:


SETTINGS: Cinematic (Post-apocalyptic), Mythology (Aztec mythology)

INTRODUCTION: Welcome, brave adventurer, to a world where the ashes of the old mingle with the ancient tales of gods and heroes. In this post-apocalyptic realm infused with the rich tapestry of Aztec mythology, prepare to embark on a journey like no other. As the sun sets on the ruins of civilization, a new chapter begins, where the remnants of humanity and the ancient gods collide.

WORLD DETAILS: Welcome to "Tlalocan," a name derived from Aztec mythology, representing the mythical paradise reserved for those who die a watery death. In this world, the average person is a survivor, eking out a meager existence amidst the crumbling remnants of once-great cities. They are resourceful and resilient, drawing strength from the stories of their ancestors and the hope of a brighter future.

CONFLICT: The predominant conflict in Tlalocan is the struggle for survival and the search for a way to restore balance to a world ravaged by both human folly and the wrath of vengeful gods. As the player, you will navigate the treacherous landscapes, face dangerous creatures, and encounter factions vying for control over limited resources. But there is a deeper conflict brewing, one that involves the ancient Aztec gods themselves and their desire to reclaim their lost glory.

FUN FACTS:
1. The ruins of ancient cities now serve as both shelter and danger. Beware of collapsing structures and hidden traps left behind by the architects of the past.

2. The Aztec pantheon is very much alive in this world. Prepare to encounter gods like Quetzalcoatl, Huitzilopochtli, and Tlaloc, each with their own agendas and desires.

3. The scarcity of resources has given rise to a thriving trade in relics and artifacts from the old world. You never know what kind of ancient technology or mystical artifact you might stumble upon in your travels.

For each of the following player starting backgrounds below, please provide 2 background traits that set them apart from each other.

A: The Lost Heir - Born into a line of Mictlantecuhtli's chosen champions, you were raised in seclusion, trained in the ways of the spirit channelers to one day reclaim your birthright and restore balance to the world.
B: The Relic Hunter - Driven by a thirst for knowledge and the desire to uncover the secrets of the past, you have spent your life scouring the ruins of ancient cities, collecting artifacts and relics imbued with the power of the gods.
C: The Outcast - Cast out by your own people due to your unique abilities, you have wandered the wastelands alone, honing your necromantic skills and surviving by your wits.
D: The Scribe of Legends - As a scribe in the ancient libraries of Tlalocan, you have spent years studying the myths and legends of the Aztec gods. Armed with this knowledge, you have set out on a quest to bring the tales to life and ensure their preservation for future generations.
Each class should have 1 trait that gives them a social advantage in this setting, and 1trait that gives them a social disadvantage in this setting to differentiate them from the others. ONLY DESCRIBE THEM IN QUALITATIVE TERMS to maintain immersion. Please output as a json object in the following format:

{
  "Background A name": {
    "Positive trait name": "Trait Description",
    "Negative trait name": "Trait Description"
  },
"Background B name": {
    "Positive trait name": "Trait Description",
    "Negative trait name": "Trait Description"
  }
 ...
}"""


story_start_prompt = """The following is a description of world:
The following is a description of player:
The following is a description of the campaign the character will follow:

Based on this, give an 2-3 sentence introduction to the player telling them a little bit about their backstory and how that informs their current abilities.
Also give a 2-3 sentence description of how they find themselves in the starting point of the story.
Provide a 2-3 sentence story hook to give them some initial reason to start adventuring and some guidance of where to go from here."""