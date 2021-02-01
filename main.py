#Concevoir une application qui permet
# de calculer le panier client
montantTotal = 0.0
reponse = "oui"
recette = 0
while(reponse == "oui"):

    for i in range(0, 2):
        print("Entrez le prix unitaire de l'article ", (i + 1))
        part = float(input())
        print("Entrez la quantité de larticle", (i + 1))
        qart = float(input())
        montantTotal = montantTotal + (part * qart)
        recette = recette + montantTotal
    print("Le montant total est : ", montantTotal)
    reponse = input("Voulez vous continuer? oui pour continuer ou autre reponse pour arrêter")
print("La recette  est : ", recette)



