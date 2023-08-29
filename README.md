
# AlwaysDungeons
24-hour AI DND generation.

## Environment Variables

|KEY|DESCRIPTION|
|--|--|
|DISCORDBOT|The discord bot's token.|
|NEURAL|Your NeuralLove api key. Should look like "Bearer v...."|
|PB|Your Quora api key. You'll sign into Quora on your browser, go into your Inspect Element -> Storage -> Quora.com cookies, and copy the m-b cookie. Used to access poe.com's ChatGPT bot.|
|EMAIL|The email used with your ChatGPT account. Used as a fallback to poe.com, and not required to fill in.|
|PASS|The password used with your ChatGPT account. Used as a fallback to poe.com, and not required to fill in.
|


## Functionality

The bot's primary purpose is to access generative AI programs for the sake of creating Dungeons and Dragons homebrew content. By using the sites "poe.com" and "neural.love" and their respective toolkits, the bot is capable of organizing generated content using Discord's recent Forums feature and provide useful features for Dungeon Masters. It sorts requests for content into a queue and takes the next requested generation after the last one is resolved (roughly every 24 seconds). If no content is requested, every six "cycles" (checks for requests) the bot will produce an unprompted piece of homebrew content, choosing randomly from the available categories. This can be disabled (read "Setup").

The bot is not built to be invited to multiple servers. Since it organizes content across several channels, it's far more efficient to have each server host its own instance of the bot, hence this repo.

In main.py, you'll find several fields at the top of the file (starting with guildID and ending with autogen). Each of these correlates to a value specific to each instance of the bot, such as the bot's ID or the channel IDs used. Those are listed with more detail in the Setup section.

## Setup

The bot has several values. When this repo is cloned, it's required that you alter them alongside setting the environment variables.

guildID and botID are, respectively, the IDs for the server the bot is in and the bot itself. To access these values, enable Developer Mode.

magicForum, raceForum, subclassForum, locationForum, monsterForum, npcForum, and otherForum are all the Forum Channels that the bot requires. These can point to the same channel in theory, but are designed to be separated into individual channels for each topic.

logChannel is the channel that error messages and other announcements from the bot are posted in. Be sure to put this channel in a publicly visible place; it announces when a user's request is being fulfilled.

autogen enables or disables the bot's automatic production of homebrew content. If this is not desired, change autogen to False.
