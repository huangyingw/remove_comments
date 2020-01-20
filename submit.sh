#!/bin/zsh
SCRIPT=$(realpath "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
cd "$SCRIPTPATH"

find . -type f -name "[0-9]*.py" | while read ss
do
    if $(~/loadrc/pythonrc/remove_comments.py "$ss")
    then
        mv -fv "$ss.strip" "$ss"
        sed -i.bak '/print.*(/d;/^_author_/d;/__main__/d;/ = Solution()/d;/^_project_/d;/\bprint\b/d;s/#--//g;s/##//g;/^$/d;/^\s*$/d' "$ss"
        autopep8 --in-place "$ss"
        leetcode submit -d "$ss"
    else
        rm "$ss.strip"
    fi
done
