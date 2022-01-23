from datetime import datetime
from moviepy.editor import VideoFileClip, concatenate_videoclips
import sys

def recorrer_dir(dir,ext):
    import os
    ficheros=list()
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(ext) or file.endswith(ext.upper()):
                ficheros.append(os.path.join(root, file))
    return ficheros    

def junta(dir,salida, quitar):
    ext=salida[-4:]
    print("Extension %s" % ext )
    ficheros=recorrer_dir(dir,ext)
    subclips=list()
    i=0
    duracion_total=0
    total=len(ficheros)
    ahora=datetime.now()
    print("Total ficheros a tratar : %s " % str(total ))
    for fichero in ficheros:
        inicio=datetime.now()
        i+=1
        clip = VideoFileClip(fichero)
        duracion_total=clip.duration-quitar+duracion_total
        duracion=-quitar
        sub=clip.subclip(0,clip.duration+duracion)
        subclips.append(sub)
        acabo=datetime.now()
        print("",end="")
        print("[%s].Fich: %s (%s/%s) %s .Dur Total Vid: %s mins.Ult Vid: %s .T. ejec: %s .ETA: %s en %s" 
            % (str(acabo),fichero,str(i),str(total),str(round(i/total*100,2)),str(round(duracion_total/60,2))
            ,str(acabo-inicio),str(acabo-ahora), str(acabo+(acabo-inicio)*(total-i)),str((acabo-inicio)*(total-i)) )
            #,end='\x1b[1K\r', flush=True
            )
        
    if len(ficheros)>0:
        print("Generando fichero final: %s" % salida)           
        final_clip = concatenate_videoclips(subclips)
        final_clip.write_videofile(salida)
        acabo=datetime.now()
        print("Tiempo total usado : %s " % (str(acabo-ahora)))

if __name__ == "__main__":
    if len(sys.argv)<3:
        print("USAGE python videos.py <dir> <output_file> [<segundos a quitar>]")
    else:
        print ("Tratando directorio: %s para generar %s" % (sys.argv[1],sys.argv[2]) )
        if len(sys.argv)==3:
            quitar=0
        else:
            quitar=sys.argv[3]
        
        junta(sys.argv[1],sys.argv[2], quitar)
