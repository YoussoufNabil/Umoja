import os
import shutil


# creation d un dossier dans la racine C
def creationDossierdansC():
    nomdossier=input("enter le nom du dosser : ")
    os.chdir("C:/")
    os.mkdir(nomdossier)
    print("le dossier",nomdossier,"est cree dans la racine C :")
#creationDossierdansC()

#lire un fichier
def lirefichier(fichier):
    f=open(fichier,"r")
    continu=f.readline()
    f.close()
    return continu
fichier="C:/windows/setupact.log"
C=lirefichier(fichier)
#print(C)

#fonction de copie de dossier
def copieDossier(source,destination):
    try :
        shutil.copy2(source, destination)
    except PermissionError:
        print("vous n'avez pas les droits pour copier ce fichier")
    except FileNotFoundError:
        print("le fichier n'existe pas")
source="C:/test"
destination="C:/testdst"
copieDossier(source,destination)

#fonction de suppression de dossier
def suppressionDossier(nomDossier):
    try :
        shutil.rmtree(nomDossier)
        print("le dosier",nomDossier,"est bien supprimer")
    except FileNotFoundError:
        print("le dossier est introuvable")
    except FileExistsError:
        print("le dossier n'existe pas")
nomDossier="C:/testdst"
suppressionDossier(nomDossier)

#fonction de cration de fichier CSV contenant des dossiers de configuration des equipement
def creationFichierCSV():
    fichier ="config.csv"
    idE="ISI_"
    ordi="ordinateur_"
    routeur="Routeur_ISI_"
    salle="salle"
    f=open(fichier,"w")
    for i in range(1000000):
        idE+=str(i)
        ordi+=str(i)
        routeur=str(i)
        a=1000000%100
        salle+=str(a)
        info=idE+";"+ordi+";"+routeur+"\n"
        f.write(info)
    f.close()
creationFichierCSV()
