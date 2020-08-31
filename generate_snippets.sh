#!/bin/bash

red_bold="\033[1;31m";
reset="\033[0m";

file="~/.vim/UltiSnips/python/python_generate.snippets"
folder="~/.vim"

echo "" > ~/.vim/UltiSnips/python/python_generate.snippets

for i in $(find -name '*.py'); do
   [ -f "$i" ] || break
   # echo "$i --> ${i##*/}"
   echo "Snippet ${i##*/} was generated"
   
   echo "" >> ~/.vim/UltiSnips/python/python_generate.snippets
   echo "snippet $(basename -- "$i" .py) \"$(basename -- "$i" .py) autocomplete\"" >> ~/.vim/UltiSnips/python/python_generate.snippets
   cat "$i" >> ~/.vim/UltiSnips/python/python_generate.snippets
   echo "" >> ~/.vim/UltiSnips/python/python_generate.snippets
   echo "endsnippet" >> ~/.vim/UltiSnips/python/python_generate.snippets
   echo "" >> ~/.vim/UltiSnips/python/python_generate.snippets
done
