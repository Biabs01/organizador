import os
import shutil

from_dir = "C:/Users/biabs/Downloads"
to_dir = "C:Users/biabs/Downloads/imagensbaixadas"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

#Mova todos os arquivos de imagem da pasta Downloads para outra pasta
for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpeg', '.jpg', '.jfif']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Arquivos_Imagem_"
        path3 = to_dir + '/' + "Arquivos_Imagem_" + file_name
        #print(path1)
        #print(path3)

        #Checar se a pasta/diretório existe antes de mover
        #Se não existir fazer uma NOVA pasta/diretório antes de mover
        if os.path.exists(path2):
            print("Movendo " + file_name + "...")

            #Mover do path1 para path2
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Movendo " + file_name + "...")
            shutil.move(path1,path3)

print(dir(shutil))
print(dir(os))