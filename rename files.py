def remplire():
    #n = int(input("Donner le nomber de fichiers : ")) version 0.0
    sn = int(input("input first nbre of file : ")) # | []= version 0.1
    fn = int(input("input end nbre of file : "))   # | []= version 0.1
    default_name = input("default name  : ")
    new_name = input("new name : ")
    return sn,fn,default_name,new_name
def traitment(sn,fn,default_name,new_name):
    f = open("cmd_code.txt","w")
    for i in range(sn,fn+1):
        line = "ren "+'"'+default_name+str(i)+'.png"'+" "+'"'+new_name+str(i)+'.png"'
        f.write(line+"\n")
    f.close()
sn,fn,default_name,new_name = remplire()
traitment(sn,fn,default_name,new_name)
print("Thanks For using My Programe by Jeridi Mohamed")
input("Open file 'cmd_code.txt' and copie all and past in the cmd root folder ...")
input("Press eny Key to exit ...")