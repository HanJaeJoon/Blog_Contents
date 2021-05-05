#!/usr/bin/env python

import os
from urllib import parse

HEADER="""# 
# Blog_Contents

https://jjester.tistory.com/

블로그 글 저장소

---
"""


def main():
    content = ""
    content += HEADER
    
    directories = [];

    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        category = os.path.basename(root)
        
        if category == 'images':
            continue
        
        directory = os.path.basename(os.path.dirname(root))
        
        if directory == '.':
            continue
            
        if directory == category:
            content += "### [{}]({})\n".format(category, parse.quote(os.path.join(root, file)))
            continue
        
        if directory not in directories:
            content += "### {}\n".format(directory)
            directories.append(directory)

        for file in files:
            content += "- [{}]({})\n".format(category, parse.quote(os.path.join(root, file)))
        content += "\n"

    with open("README.md", "w") as fd:
        fd.write(content)


if __name__ == "__main__":
    main()
