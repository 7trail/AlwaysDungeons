# AlwaysDungeons ([mirror](https://git.askiiart.net/askiiart/AlwaysDungeons))

[![Build Status](https://drone.askiiart.net/api/badges/askiiart/AlwaysDungeons/status.svg?ref=refs/heads/main)](https://drone.askiiart.net/askiiart/AlwaysDungeons)

24-hour AI DND generation.

## Environment Variables

| KEY              | DESCRIPTION                                                                                                                                                                              |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BOT_TOKEN        | The discord bot's token.                                                                                                                                                                 |
| NEURAL           | Your NeuralLove api key. Should look like "Bearer v...."                                                                                                                                 |
| POE_TOKEN        | Your Quora api key. You'll sign into Quora on your browser, go into your Inspect Element -> Storage -> Quora.com cookies, and copy the m-b cookie. Used to access poe.com's ChatGPT bot. |
| OPENAI_EMAIL     | OPTIONAL, currently not implemented. The email used with your ChatGPT account. Used as a fallback to poe.com, and not required to fill in.                                               |
| OPENAI_PASS      | OPTIONAL, currently not implemented. The password used with your ChatGPT account. Used as a fallback to poe.com, and not required to fill in.                                            |
| GUILD_ID         | The ID of the server the bot is in.                                                                                                                                                      |
| BOT_ID           | The ID of the bot itself.                                                                                                                                                                |
| MAGIC_ITEM_FORUM | The channel ID of the magic item forum                                                                                                                                                   |
| RACE_FORUM       | The channel ID of the race forum                                                                                                                                                         |
| SUBCLASS_FORUM   | The channel ID of the subclass forum                                                                                                                                                     |
| LOCATION_FORUM   | The channel ID of the location forum                                                                                                                                                     |
| MONSTER_FORUM    | The channel ID of the monster forum                                                                                                                                                      |
| NPC_FORUM        | The channel ID of the NPC forum                                                                                                                                                          |
| OTHER_FORUM      | The channel ID of the other forum                                                                                                                                                        |
| LOG_CHANNEL      | The channel ID of the log channel                                                                                                                                                        |
| AUTOGEN          | Whether or not the bot should automatically generate content. (true/false)                                                                                                                            |

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

## Running the bot

### Docker

Example `docker run`:

```bash
docker run -d --env-file /path/to/.env docker.askiiart.net/askiiart/discord-always-dungeons
```

Example `docker-compose.yml`:

```yaml
version: '3.7'
services:
  always-dungeons:
    image: docker.askiiart.net/askiiart/discord-always-dungeons
    env_file:
      - /path/to/.env
```

## Build the Docker image

Run this to build the image:

```bash
git apply docker.patch
docker run -v .:/repo python /bin/sh -c "cd /repo && pip install -r requirements.txt && apt-get update && apt-get install binutils -y && pip install pyinstaller && pyinstaller main.py && cd /repo/dist/main && chmod -R 777 /repo/dist/main && tar cvfz /repo/AlwaysDungeons.tar.gz *"
docker build .
```

Alternatively, you can just run `./build-and-push.sh`, which will do all that for you. Just make sure to set the variables before running it.

## Run the dev image

This image is built for development. It mounts the current directory to /data, installs all the dependencies, and runs the bot from there. Keep in mind this runs differently than the production image. It uses load_dotenv, not `--env-file`.

```bash
docker run -v .:/data docker.askiiart.net/askiiart/always-dungeons-testing
```

```yaml
version: '3.7'
services:
  always-dungeons:
    image: docker.askiiart.net/askiiart/discord-always-dungeons
    volumes:
      - .:/data
```
