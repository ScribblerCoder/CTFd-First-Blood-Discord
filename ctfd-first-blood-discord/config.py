# CTFd API endpoint
HOST = "https://ctfd.io"

# CTFd API token
API_TOKEN = ""

# How frequently to check for new solves
POLL_PERIOD = 5

# Discord webhook url
WEBHOOK_URL = ""

# Available template variables are:
# User Name (if individual mode) / Team Name (if team mode): {user_name}
# Challenge Name: {chal_name}
FIRST_BLOOD_ANNOUNCE_STRING = "```ini\n🩸 First Blood for challenge <{chal_name}> goes to team <{user_name}>!\n```"

# To be used with announce_all_solves
SOLVE_ANNOUNCE_STRING = "```ini\n🚩 team <{user_name}> just solved [{chal_name}]!\n```"

# Whether or not to announce all solves as well as first bloods
ANNOUNCE_ALL_SOLVES = True

# Category Emojis (if any)
CATEGORY_EMOJIS = {
    "web": [":globe_with_meridians:"],
    "crypto": [":sob::closed_lock_with_key:"],
    "pwn": [":bug:"],
    "rev": [":rewind:"],
    "forensics": [":mag:"],
    "osint": [":detective:"],
    "blockchain": [":white_large_square::chains:"],
    "misc": [":jigsaw:"],
}

# GIFs and images to be added with the discord embed 
IMG_URLS = ['https://miro.medium.com/fit/c/96/96/1*MptLjygMO184yyWqmg4PUA.gif','https://miro.medium.com/max/1400/1*fApaeq6-ht-s6Cdu6qdlrQ.gif','https://media.tenor.com/3bTxZ4HdrysAAAAC/pixels-neon.gif','https://64.media.tumblr.com/a4ceca22cc9c75d182f3f1bde1b154ea/1a81e7dc134d48c3-4e/s540x810/bbd495716a2f3624ad1e234ad254d639c38a6f51.gif','https://media.tenor.com/tm3KA5yrnmMAAAAC/hacker-man-hacker.gif','https://media.tenor.com/9Pn19IB5kYcAAAAC/hacking-computer-screen.gif','https://i.imgur.com/KvehwgO.png','https://media.tenor.com/yOwKX_hMp6cAAAAd/hackerman-rami-malek.gif','https://media.tenor.com/Pm4S40MGsIQAAAAC/hacker-hackerman.gif','https://i.giphy.com/media/o0vwzuFwCGAFO/giphy.webp']

# Timezone of the competition to add current time of the firstblood in the discord embed
TIME_ZONE = 'America/New_York'
