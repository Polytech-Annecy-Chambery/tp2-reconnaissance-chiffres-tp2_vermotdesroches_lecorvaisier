from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    sim_max = 0
    id_sim_max = 0
    im_bin = image.binarisation( S)
    im_loc = im_bin.localisation()
    for i in range (len(liste_modeles)):
        im_redim = im_loc.resize(liste_modeles[i].H, liste_modeles[i].W)
        sim = im_redim.similitude(liste_modeles[i])
        if sim > sim_max : 
            sim_max = sim
            id_sim_max = i
    return id_sim_max
    

