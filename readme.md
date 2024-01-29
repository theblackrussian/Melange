# What is this Melange for?

Melange was inspired by Daniel Miessler work on [Fabric](https://github.com/danielmiessler/fabric). Instead of using shells, Melange uses Python modules. Melange uses [poe-api-wrapper](https://github.com/snowby666/poe-api-wrapper) to leverage the GraphQL API of Poe.

# What are the letters `p`, `qp`, `xp` and whatnot?

Those are aliases.
Melange was designed on a macOS system so you will have to edit your bash profile to add those aliases into it. The aliases should point to your Python modules. The naming convention is entirely yours.

# Why am I running this project on Python v3.10?
Because during the creation of my environment through pipenv I had the Python versioning specified inside my Pipfile file, and it required Python v3.10. However, pipenv can be used with higher versions of Python. It was a mistake on my end. If I wanted to, I could delete this environment and create a new one with higher version of Python. 

# What is `smy.py` doing?
This module can summarize any YouTube video.
It can summarize multiple YouTube videos. For this, juste copy all your URLs all at once, separated by commas.
```text
url1,url2,url3
```
This module should be piped with xy.py. Usage below:
```bash
p|xy|smy
```

# What is `qp.py` doing?
This module can answer any question you have on any web page. It can work multiple web pages. For this, just copy all your URLs all at once, separated by commas.
```text
url1,url2,url3
```
This module should be piped with `xp.py`. Usage below:
```bash
p|xp;qp
```

Please not that because qp is taking user input under the form of a question, it should not be piped with xp. Hence why `;` was used instead.

`pbpaste|ExtractPage|QuestionPage`

# What is `kwd.py` doing?
This module can search for a keyword in a YouTube video.
It will print in your terminal the timestamps at which the keyword appears in the video. 

This module should NOT be piped in its current configuration. Usage below:
```bash
kwd
```

This command will start `kwd.py` and prompt you for a `YouTube URL` and a `keyword`.

# Whats the `config.py` file for?

This file contains the settings for:
- The location of the directory for `transcripts`/`webpages` (for v1)
- The `chatID` for the bot
- The `chatCode` for the bot

# Whats `prompt.py` for?

This module contains the prompt that will be sent along with your query. You can edit that prompt to your liking.

Alternatively you could use a prompt directly from Poe inside the bot's settings but by using a local prompt it gives you more flexibility.