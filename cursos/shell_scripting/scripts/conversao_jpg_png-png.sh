#!bin/bash
echo "teste"

CAMINHO_IMAGENS=~/training/alura_cursos/cursos/shell_scripting/imagens-livros/

#no linux é utilizado o comando #convert algoritmo.jpg algortimo.png
convert $CAMINHO_IMAGENS/$1.jpg $CAMINHO_IMAGENS/$1.png
convert $CAMINHO_IMAGENS/$2.jpg $CAMINHO_IMAGENS/$2.png