
# fonction pour lancer l'operation
def runOperation(val1, val2, op):
    res=None
    if op == '+':
        res = val1+val2
    elif op == '-':
        res = val1 - val2
    elif op == '*':
        res = val1 * val2
    elif op == '/':
        if val2 == 0:
            print("Erreur impossible de diviser par 0.\nRetour resultat à 0")
            res = 0
        else:
            res = val1 / val2
    
    return res


# fonction cast des valeurs numerique en float
def castFloat(val):
    return float(val)


# fonction de check conformite des operateurs
def checkOperator(op):
    return op in ['*','+','-','/']


# fonction check conformite des valeur numerique
def checkNumeric(val):
    return val.isnumeric()


# fonction de check conformite je continu
def checkContinuer(cont):
    return cont.lower() in ['o', 'n', 'oui', 'non']


# fonction d'analyse de la reponse je continu
def continuerResult(cont):
    return True if cont.lower() in ['o','oui'] else False


# fonction qui interagi avec l'utilisateur
# msg : message affiche a l'utilisateur
# checkfonction : fonction de check de conformite entree
# processFonction : fonction de process sur l'entree utilisateur
def askUser(msg, checkfunction, processFunction=None):
    # boucle infini
    while True:
        # affiche msg a l'utilisateur et recuperer le resultat
        ui = input(msg+"\n(ou entrer q pour quitter)\n")
        # si ui=q je quitte le programme
        if ui.lower() == 'q':
            exit()
        # sinon je lance ma fonction de chek sur le resultat
        if checkfunction(ui):
            # si le check passe 
            # je lance ma fonction de processing sur le resultat si presente 
            if processFunction:
                return processFunction(ui)
            else:
                # si pas de fonction de processing retour du resulat brut
                return ui
            break
        else:
            # si le check ne passe pas j'affiche une erreur et je redemande le parametre
            print("Erreur, parametre non reconnu.")


# point d'entree du programme
# boucle infinie
while True:

    # recuperation de val1
    val1 = askUser('\nEntrez une première valeur numerique', checkNumeric, castFloat)
    # recuperation de val2
    val2 = askUser('\nEntrez une deuxième valeur numerique', checkNumeric, castFloat)
    # recuperation de l'operateur
    op = askUser("\nEntrez un operateur *, /, -, +", checkOperator)

    # run de l'operation et affichage du resultat
    print("\nResultat de l'operation  : %.2f"%(runOperation(val1, val2, op)))

    # je demande si continu si false exit()
    if not askUser('\nVoulez vous effectuer une nouvelle operation : o (oui), n (non)', checkContinuer, continuerResult):
        exit()
