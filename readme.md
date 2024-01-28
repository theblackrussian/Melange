# Why am I running this project on Python v3.10?
Because during the creation of my environment through pipenv I had the Python versioning specified inside my Pipfile file, and it required Python v3.10. However, pipenv can be used with higher versions of Python. It was a mistake on my end. If I wanted to, I could delete this environment and create a new one with higher version of Python. 

# What is smy.py doing?
This module can summarize any YouTube video.
It can summarize multiple YouTube videos. For this, juste copy all your URLs all at once, separated by commas.
```text
url1,url2,url3
```
This module should be piped with xy.py. Usage below:
```bash
p|xy|smy
```

# What is qp.py doing?
This module can summarize any web page.
It can summarize multiple web pages. For this, just copy all your URLs all at once, separated by commas.
```text
url1,url2,url3
```
This module should be piped with xp.py. Usage below:
```bash
p|xp|qp
```
