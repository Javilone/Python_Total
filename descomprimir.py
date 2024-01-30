import shutil

archivo = "/Users/javilone/Desktop/Python Total Udemy/Codigo/Dia 9/Proyecto Dia 9.zip"
target = "/Users/javilone/Desktop/Python Total Udemy/Codigo/Dia 9"
archivo_format = "zip"
shutil.unpack_archive(archivo,target,archivo_format)


#shutil.make_archive(archivo_destino, "zip", carpeta_origen)