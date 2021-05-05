#!/usr/bin/env python

import os

HEADER="""# 

# Blog_Contents

https://jjester.tistory.com/

블로그 글 저장소

---

"""


def main():
    content = ""
    content += HEADER

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

        content += "### {}\n\n".format(category)

        for file in files:
            content += "- [{}]({})\n".format(category, os.path.join(root, category, file))
        content += "\n"

    with open("README.md", "w") as fd:
        fd.write(content)


if __name__ == "__main__":
    main()
