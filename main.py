from forex_python.converter import CurrencyRates

# Dictionnaire pour stocker les taux de conversion personnalisés
taux_conversion_personnalises = {'MZDY': 1.78}

def convertir_devise():
    montant_euros = float(input("Veuillez saisir la valeur en euros : "))
    devise_cible = input("Veuillez saisir le code de la devise cible (par exemple, CAD) : ")

    # Vérifier si la devise est dans le dictionnaire des taux personnalisés
    if devise_cible in taux_conversion_personnalises:
        montant_converti = montant_euros * taux_conversion_personnalises[devise_cible]
        print(f"{montant_euros} Euros équivaut à {montant_converti} {devise_cible}")
    else:
        # Si la devise n'est pas trouvée, utiliser la bibliothèque forex-python
        montant_converti = CurrencyRates().convert('EUR', devise_cible, montant_euros)
        print(f"{montant_euros} Euros équivaut à {montant_converti} {devise_cible}")

def ajouter_devise(nom_devise, taux_conversion):
    # Ajouter la nouvelle devise avec son taux de conversion au dictionnaire
    taux_conversion_personnalises[nom_devise] = taux_conversion
    print(f"La devise {nom_devise} a été ajoutée avec un taux de conversion de {taux_conversion}.")

# Appeler la fonction pour ajouter une nouvelle devise
ajouter_devise('MZDY', 1.78)

# Appeler la fonction pour effectuer la conversion
convertir_devise()

# Appeler la fonction pour effectuer la conversion
convertir_devise()
