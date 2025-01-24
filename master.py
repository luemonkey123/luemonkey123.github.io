#! /usr/bin/python3

from datetime import datetime
from icecream import ic
import os
import shutil
import filecmp
import shlex
import subprocess

## MUST have / at the end of dir
postdirV = "/Users/shunquanshen/Documents/Obsidian/jekyll/posts/"
picsdirV = "/Users/shunquanshen/Documents/Obsidian/jekyll/"
postdirJ = "/Users/shunquanshen/Projects/blogs/luemonkey123.github.io/_posts/"
assetsJ = "/Users/shunquanshen/Projects/blogs/luemonkey123.github.io/assets/pimgs/"

date = datetime.today().strftime('%Y-%m-%d')

## Copy Posts to posts-dir
posts = os.listdir(postdirV)
oldPosts = os.listdir(postdirJ)
ic(posts)
ic(oldPosts)
for i in oldPosts:
    if i[11:] in posts:
        oldf = postdirJ + i
        newf = postdirV + posts[posts.index(i[11:])]
        if filecmp.cmp(oldf, newf):
            del posts[posts.index(i[11:])]
        else:
            os.remove(oldf)

ic (posts)

for i in posts:
    shutil.copy(postdirV + i, postdirJ+date+"-"+i)

## Git stuff
count = open("count.txt", "r+")
count_num = int(count.read())

subprocess.call(shlex.split("git add ."))
subprocess.call(shlex.split("git commit -m \"Post #" + str(count_num) + "\""))
subprocess.call(shlex.split("git push -u origin main"))

count_num = count_num + 1

os.remove("count.txt")

with open("count.txt", "w") as file:
    file.write(str(count_num))

print("Everything should be done")