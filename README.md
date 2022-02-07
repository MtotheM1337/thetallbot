# The Tall Bot

This is a collaborative Discord bot meant for learning and experimenting with Python, as such don't expect any high code quality.

---

## Table of Contents
Click on the menu icon next to README.md for a list of sections

---

## Requirements

* Python >=3.5.3
* discord.py
* dotenv
* requests

## Setup

```sh
# Create new virtual enviornment
python3 -m venv /path/to/new/venv
# Load the virtual enviornment
source /path/to/new/venv
# Install dependencies
python -m pip install discord.py python-dotenv requests

# Download the source code
git clone https://github.com/mtothem1337/thetallbot
# Change into the source code directory
cd thetallbot
# Run the bot
./main.py
```

### API Key

Since keeping secrets in source code is unsafe, especilly in regards to version control systems such as git. We will store the key in a `.env` file not managed by git.

It is important to note that secrets should never be world readable either, as any user on the system can then read the key for themselves. Only the bot user should be allowed to read it's contents.

```sh
# .env
TTB_TOKEN='api-key'
```

## Design

In order to keep the code clean, `discordpy` offers a modular design called `cogs`. These are standalone class objects that can be hot loaded/un-loaded during runtime. This mechanism also handles the merging of intersecting logic automatically.

So for the sake of cleanliness, we separate each feature into it's own standalone cog.

If it's not obvious already, Having this structure means that any cog written for this bot, can also be imported into other `discordpy` projects and wise versa. Similar to building using lego bricks.

```
.
├── cogs
│   ├── cog1.py
│   └── cog2.py
└── main.py
```
