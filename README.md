# The Tall Bot

This is a collaborative Discord bot meant for learning and experimenting with Python, as such don't expect any high code quality.

---

## Table of Contents
Click on the menu icon next to README.md for a list of sections

---

## Requirements

* Python >=3.5.3
* discord.py
* requests

## Setup

```
git clone https://github.com/mtothem1337/thetallbot
cd thetallbot
```

### Manual

```sh
# Create new virtual enviornment
python3 -m venv /path/to/new/venv
# Load the virtual enviornment
source /path/to/new/venv/bin/activate
# Install dependencies
python -m pip install -r requirements.txt
# Run the bot
./src/main.py
```

## Docker

### Building an image

```
docker build -t thetallbot .
```

### Running an image

#### CLI

```
docker run -d -p 3000:3000 --env-file=.env thetallbot
```

#### Docker Compose

```
docker-compose up -d
```

### API Key

API key will be loaded from the `$TTB_TOKEN` env variable, or `.env` when using docker-compose.

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
