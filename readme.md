# A good storytelling ChatGPT game

# Installation

Install requirements.txt. So far it's pretty light. I use the most recent version of OpenAI.

To run this, you will need your own ChatGPT API key. I will not give you mine.

Create a file called `credentials.py` with the following format:

`GPT_KEY = 'your-gpt-key-here'`

To see an example of how to run everything (that I've put together so far), run the `Running everything so far.ipynb` 
notebook in Jupyter or whatever you want. 

# Game rules

## Character attributes and taking actions

For each new setting created, ChatGPT will create 6 character attributes relevant to the setting. These will always be:

- **Two physical attributes**
- **Two mental attributes**
- **Two social attributes**

All attrributes start at +0. When selecting a race, the player will receive a modifier of +1 to one attribute, and a modifier of -1 for another.
As the player progresses and gains experience, these modifiers will change.

Whenever the player takes an action that requires effort, skill, or knowledge, ChatGPT will select the appropriate attribute for that action.
For all actions, ChatGPT will roll two 6-sided dice, add them together, and add any relevant attribute modifiers. The total will determine the outcome:

- **3 and below:** very negative outcome. The action fails completely, and the player incurs a negative consequence.
- **4-5:** negative outcome. The action fails completely, but no further consequences are incurred.
- **6-9:** positive outcome. The action partially succeeds, though there may be outcomes that the player did not intend.
- **10 and above:** very positive outcome. The action succeeds completely, and there may be unintended positive outcomes.

Players may not re-try any actions.

## Character creation

During character creation, the player selects:

- **Character race.** Each race confers one positive and one negative modifier to player attributes. This has a mechanical impact on actions taken.
- **Character class.** Each class confers two class-specific skills that can be used at any time. These have mechanical impact as the character interacts with the world.
- **Character background.** Each background confers two class-specific social traits--one positiive, one negative. These impact how other characters in the world interact with the player character.

## Navigating the world

ChatGPT acts as a Game Master, guiding you through the world and determining the impact of the player's actions.
The player may enter whatever prompt they wish, and ChatGPT will do its best to parse that input as it relates to the game.

**NOTE:** ChatGPT will refuse to engage with any prompt that is sexually explicit, bigoted, or overly violent.

ChatGPT will remember previous interactions and respond based on the setting, recent actions taken, and the overall arc the player has taken.

## Default actions

At any time, the player may enter one of the following Default Actions (not case-sensitive):

- **Help.** ChatGPT will guide the player through the basics of using the TTRPGPT system.
- **Save.** Save the game progress to this point. Any saved game can be resumed later as if the player had never left.
- **Load.** Load a previously saved game.
- **Character.** This will provide a description of the character, including their race, class, and background, as well as their current status.
- **Status.** This will provide a description of the player's current status.
- **Inventory.** This will provide a description of all the items currently held by the player.
- **Journal.** This will provide a description of all current and past objectives pursued by the player. This will also provide a brief description of the most recent actions taken.
