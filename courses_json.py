import sys
import json
choix = ""
chemin = "D:\ProjetsBackEnd\ListCoursesWithJson\donnees.json"
list_courses = []
    
while not(choix.isdigit()) or not(1 <= int(choix) <=5):
    print('''
        Le programme doit permettre de réaliser 5 actions :  
        1 - Ajouter un élément à la liste de courses.
        2 - Retirer un élément de la liste de courses.
        3 - Afficher les éléments de la liste de courses.
        4 - Vider la liste de courses.
        5 - Quitter le programme.
     ''')

    choix = input("Entrez un nombre entre (1 - 5) : ")
        
    if choix == "1":
        courses =  input("Entrez le nom d'un element a ajouter a la liste de courses : ")
        with open(chemin, mode = "r") as fichier:
         list_courses = json.load(fichier)
       
        list_courses.append(courses)
       
        with open(chemin, mode = "w") as fichier:
          json.dump(list_courses,fichier,indent = 4)

        print(f"L'element {courses} a bien ete ajoute a la liste.")
        choix = ""

    elif choix == "2":
        retirer = input("Entrez le nom d'un element a retirer de la liste de courses : ") 
        if list_courses.count(retirer):

            with open(chemin, mode = "r") as fichier:
             list_courses = json.load(fichier)
       
            list_courses.remove(retirer)
       
            with open(chemin, mode = "w") as fichier:
                json.dump(list_courses,fichier,indent = 4)

            print(f"L'element {retirer} a bien ete suprimer de la liste.")
        else:
                print(f"L'element {retirer} n'est pas dans la liste.")   
        choix = ""        

    elif choix == "3":

        with open(chemin, mode = "r") as fichier:
            list_courses = json.load(fichier)

        if list_courses:        
            print("Voici le contenu de votre liste : ") 
            for i, course in enumerate(list_courses,1):
                print(f"{i}.",course)
        else:    
                print("votre liste ne contient aucun element.")      
        choix = ""    

    elif choix == "4":

        with open(chemin, mode = "r") as fichier :
            list_courses = json.load(fichier)

        list_courses.clear(),

        fichier =  open(chemin, mode = "w")
        json.dump(list_courses,fichier,indent = 4)
        fichier.close()

        print("La liste a ete videe de son contenu") 
        choix = ""    
                
    elif choix == "5":
        print("A bientot !")  
        sys.exit() 