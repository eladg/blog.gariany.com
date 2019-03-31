#!/usr/bin/python

import json
import string

from pprint import pprint


def format_filename(s):
    """Take a string and return a valid filename constructed from the string.
Uses a whitelist approach: any characters not present in valid_chars are
removed. Also spaces are replaced with underscores.
 
Note: this method may produce invalid filenames such as ``, `.` or `..`
When I use this method I prepend a date string like '2009_01_15_19_46_32_'
and append a file extension like '.txt', so I avoid the potential of using
an invalid filename.
 
"""
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ','_') # I don't like spaces in filenames.
    return filename

# =============================================================================
# script starts here:
# =============================================================================

with open('old-posts.json') as f:
  data = json.load(f)

for p in data["posts"]:
  print("\n")
  pprint(p)
  print("\n")

  markdown = '''
---
title: "{title}"
date: "{date}"
lastmod: "{date}"
author: "Elad Gariany"
cover: "/img/cover.jpg"
tags: {tags}
categories: [{category}]
link: "{url}"
id: {id}
---

## {title}

'''.format(
    title=p["title"],
    date=p["date"],
    category=json.dumps(p["category"]),
    tags=json.dumps(p["tags"]),
    url=p["url"],
    id=p["id"]
  )

  print(markdown + "\n\n")

  fname = ("posts/" + format_filename(p["title"]) + ".md").lower()
  pprint("will print to: ")
  pprint(fname)
  print("\n\n")

  f = open(fname,"w+")
  f.write(markdown)
  f.close()

