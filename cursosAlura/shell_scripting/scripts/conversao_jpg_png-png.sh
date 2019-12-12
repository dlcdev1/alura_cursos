#!bin/bash
echo "teste"

cd ~/training/alura_cursos/cursos/shell_scripting/imagens-livros/

if [ ! -d png ]
then
echo "Criando diretorio png"
    mkdir png
fi


# $@ engloga todos os parametros
for imagem in *.jpg
do 
    imagem_sem_extensao=$(ls $imagem | awk -F. '{ print $1 }')
    convert $imagem_sem_extensao.jpg png/$imagem_sem_extensao.png
done