import numpy as np

salaire_horaire = [ 9.50, 33.50, 30.25, 10.75, 41.50, 16.75, 18.00, 15.50, 21.00,
                   15.25, 21.50, 38.00, 25.25, 42.00, 25.00, 18.75, 37.25, 38.50,
                   40.00, 41.00]
heures_par_semaine = 37.5           # nombre d'heures travaillées par semaine
semaine_par_annee = 52              # nombre de semaines payées par année


data1 = np.array([salaire_horaire])
salaire_hebdomadaire = np.sum(data1 * heures_par_semaine)
print(salaire_hebdomadaire)
heures_annuel = heures_par_semaine * semaine_par_annee
salaire_annuel = np.mean(data1 * heures_annuel)
print(salaire_annuel)
salaire_median = np.median(data1)
print(salaire_median)
print(data1[data1 < 15.5])
nb_emp_sal_30 = np.size(data1[data1 >= 30])
print(nb_emp_sal_30)
aug_sal_percent = 0.025
aug_sal = np.sum((data1[data1 < 25] * heures_annuel) * aug_sal_percent)
print(aug_sal)




def create_image(size):
    largeur, hauteur = size
    
    bitmap = np.zeros(largeur, hauteur, np.uint16)
    return bitmap

def fill(image, color=1):
    if color == 1:
        image[:] = 255
    elif color == 0:
        image[:] = 0
    else:
        raise ValueError("Color doit être d'une valeur 1 ou 0")