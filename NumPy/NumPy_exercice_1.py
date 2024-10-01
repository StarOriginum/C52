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


arr_size = (5, 4)

#1
def create_image(size):
    return np.zeros((size[1], size[0]), dtype=np.uint16)

im = create_image(arr_size)
#2
def fill(image, color=1):
    image[:] = color
#3    
def clear(image):
    fill(image, 0)
#4    
def randomize(image, percent=0.5):
    rng = np.random.default_rng()
    rand = rng.random(image.shape)
    good = rand >= percent
    very_good = good.astype(image.dtype)
    image[:] = very_good
    
#5  
def draw_point(image, point, color=1):
    if point > image.shape:
        raise ValueError("Veuillez entrer un point valide!")
    image[point[1], point[0]] = color
    
#6
def draw_rectangle(image, top_left, bottom_right):
    x0, y0 = top_left
    x1, y1 = bottom_right
    image[max(0, x0):min(image.shape[1], x1), max(0, y0):min(image.shape[0], y1)] = 1
    

#7
def reset_border(image):
    image[0, :] = 0
    image[:, 0] = 0
    image[-1, :] = 0
    image[:, -1] = 0
    
#8
def draw_random_point(image, color=1):
    height, width = image.shape
    rng = np.random.default_rng()
    x = rng.integers(0, width)
    y = rng.integers(0, height)
    
    image[y, x] = color
    
#9
def inverse_random_point(image, color=0):
    height, width = image.shape
    rng = np.random.default_rng()
    x = rng.integers(0, width)
    y = rng.integers(0, height)
    
    if (color == 1):
        image[y, x] = 0
    elif (color == 0):
        image[y, x] = 1
    
    
    
    












#11
def draw_circle(image, center, radius):
    height, width = image.shape
    cy, cx = center
    col, row = np.meshgrid(np.arange(width), np.arange(height))
    dist_hor = col - cx
    dist_ver = row - cy
    dist_hor_squared = dist_hor ** 2
    dist_ver_squared = dist_ver ** 2
    dist_squared = dist_hor_squared - dist_ver_squared
    #distance = np.sqrt(dist_squared)
    in_circle = dist_squared <= radius ** 2
    in_cycle_type = in_circle.astype(image.dtype)
    
    #image[:] =  np.logical_or(image, in_cycle_type)
    image[in_circle] = 1
    pass

    image[((row-cy)**2 + (col-cy)**2 < radius ** 2)] = 1
    
# fill(im, 1)
# print(im)
# clear(im)
# print(im)
# randomize(im)
# print(im)
# clear(im)
# print(im)
# draw_point(im, (4, 8), 1)
# print("test draw point")
# print(im)
# clear(im)
# draw_rectangle(im, (2, 2), (8, 7))
# print(im)
# fill(im, 1)
# print (im)
# reset_border(im)
# print(im)
# clear(im)
# print(im)
# draw_random_point(im, 1)
# print(im)
randomize(im)
print(im)
inverse_random_point(im, 1)
print(im)

        
    
    
    
    