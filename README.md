# CTFd First Blood Discord

# ⚠️ Deprecation Notice ⚠️
The original author will no longer be maintaining this bot and he suggests that you migrate to his Rust rewrite https://github.com/jordanbertasso/ctfd-solve-announcer-discord

---

This is a dockerised bot that uses Discords channel webhook feature to announce CTFd first bloods.

## Usage
1. [Create a Discord channel webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) for the channel where you want the first bloods to be announced and copy the webhook link.

2. Create a CTFd API token in your user settings and copy that down.

3. Update `config.py` with the webhook link, timezone, some nice GIFs (for the discord embed), CTFd API token and the API endpoint for your instance of CTFd.

4. Start with
    ```
    make run
    ```

You can customise the announcement template in `config.py` as well.


## Discord embed 


<p align="center">
<img src="PoC.gif?raw=true" width="800">
</p>
