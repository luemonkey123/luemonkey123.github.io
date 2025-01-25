#! /usr/bin/python3

## A ton of imports
from datetime import datetime       ## For time in front of file names
import os                           ## Mostly file operations
import shutil                       ## For file transfers
import filecmp                      ## For comparing files to see updates
import shlex                        ## Spliting for git commands
import subprocess                   ## Actually do git commands
import re

## MUST have / at the end of dir
postdirV = "/Users/shunquanshen/Documents/Obsidian/jekyll/posts/"
picsdirV = "/Users/shunquanshen/Documents/Obsidian/jekyll/"
postdirJ = "/Users/shunquanshen/Projects/blogs/luemonkey123.github.io/_posts/"
assetsJ = "/Users/shunquanshen/Projects/blogs/luemonkey123.github.io/assets/img/pimg/"

date = datetime.today().strftime('%Y-%m-%d') ## Get date in correct format

def images(posts_dir, attachments_dir, static_images_dir):
    # Step 1: Process each markdown file in the posts directory
    for filename in os.listdir(posts_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(posts_dir, filename)
            
            with open(filepath, "r") as file:
                content = file.read()
            
            # Step 2: Find all image links in the format ![Image Description](/images/Pasted%20image%20...%20.png)
            images = re.findall(r'\[\[([^]]*\.png)\]\]', content)
            
            # Step 3: Replace image links and ensure URLs are correctly formatted
            for image in images:
                # Prepare the Markdown-compatible link with %20 replacing spaces
                markdown_image = f"[Image Description](/assets/img/pimg/{image.replace(' ', '%20')})"
                content = content.replace(f"[[{image}]]", markdown_image)
                
                # Step 4: Copy the image to the Hugo static/images directory if it exists
                image_source = os.path.join(attachments_dir, image)
                if os.path.exists(image_source):
                    shutil.copy(image_source, static_images_dir)

            # Step 5: Write the updated content back to the markdown file
            with open(filepath, "w") as file:
                file.write(content)

    print("Markdown files processed and images copied successfully.")


## Copy Posts to posts-dir
posts = os.listdir(postdirV)
oldPosts = os.listdir(postdirJ)
## ic(posts)
## ic(oldPosts)

## Logic to prep for copy
for i in oldPosts:                         ## See all the posts
    if i[11:] in posts:                    ## Remove the first 11 chars (date) to compare
        oldf = postdirJ + i                ## Just placeholder vars
        newf = postdirV + posts[posts.index(i[11:])]
        if filecmp.cmp(oldf, newf):        ## If unchanged:
            del posts[posts.index(i[11:])] ## Remove from transfer list
        else:                              ## If changed
            os.remove(oldf)                ## Delete the old file

## ic (posts)

for i in posts:
    shutil.copy(postdirV + i, postdirJ+date+"-"+i)

## Images:
images(postdirJ, picsdirV, assetsJ)

## Git stuff

## Open and see count for commit message
count = open("count.txt", "r+")
count_num = int(count.read())

subprocess.call(shlex.split("git add ."))                                        ## Add all
subprocess.call(shlex.split("git commit -m \"Post #" + str(count_num) + "\""))   ## Commit w/ messages
subprocess.call(shlex.split("git push -u origin main"))                          ## Push

count_num = count_num + 1 ## Add one to count

## Delete and make new file
os.remove("count.txt")
with open("count.txt", "w") as file:
    file.write(str(count_num))

## Done!
print("Everything should be done")