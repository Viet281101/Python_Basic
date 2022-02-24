#{{{ partie creation d'arbre
class Objet:
    def __repr__(s):
        return "<type arbre :"+ affiche_arbre(s)+">"

def lance_erreur(s):
    o=Objet()
    o.string=s
    raise o

def parseur(chaine):
    parseurExp(chaine,0) # remplace les mot Vrai Faux bi par leur val
    return parseurR(chaine)

def parseurR(chaine):
    # chaine est une liste de mot : ( ) ET OU NON
    # ou contrien un  arbre syntaxique
    parseurParenthese(chaine,0)
    parseurNot(chaine,0)
    parseurEtb(chaine,0)
    parseurOu(chaine,0)
    if len(chaine)!=1:
        lance_erreur("expression mal formee")
    return chaine[0]

# (A OU B) ET C OU NON (A ET B) OU D

def parseurExp(chaine,place):
    # remplace les mot Vrai Faux bi par leur val
    if len(chaine)<=place:
        return
    c=numerobit(chaine[place])
    if c!="erreur":
        o=Objet()
        o.etiquette="BIT"
        o.nombre=c
        del chaine[place]
        chaine.insert(place,o)
    c=estTrueFalse(chaine[place])
    if c!="erreur":
        o=Objet()
        o.etiquette="CONST"
        o.val=c
        del chaine[place]
        chaine.insert(place,o)
    parseurExp(chaine,place+1)

def parseurParenthese(chaine,place):
    if len(chaine)<=place:
        return
    if estParentheseO(chaine[place]):
        n=tailleExpression(chaine,place+1,1)
        Nchaine=chaine[place+1:place+n] # 
        obj=parseurR(Nchaine) 
        del chaine[place:place+n+1]
        chaine.insert(place,obj)
    parseurParenthese(chaine,place+1)

def parseurOub(chaine,place): # depreci'e
    if len(chaine)<=place:
        return
    if estOr(chaine[place]):
        if place==0 or not estExp(chaine[place-1]):
            lance_erreur("erreur de syntaxe")
        if place+1>=len(chaine) or not estExp(chaine[place+1]):
            lance_erreur("erreur de syntaxe")
        a=CreerNoeudI(chaine[place-1],"OR",chaine[place+1])
        del chaine[place-1:place+2]
        chaine.insert(place-1,a)
        parseurOu(chaine,place)
    else:
        parseurOu(chaine,place+1)

def parseurGeneral(chaine,place,estXX,XX):
    if len(chaine)<=place:
        return
    if estXX(chaine[place]):
        if place==0 or not estExp(chaine[place-1]):
            lance_erreur("erreur de syntaxe")
        if place+1>=len(chaine) or not estExp(chaine[place+1]):
            lance_erreur("erreur de syntaxe")
        a=CreerNoeudI(chaine[place-1],XX,chaine[place+1])
        del chaine[place-1:place+2]
        chaine.insert(place-1,a)
        parseurGeneral(chaine,place,estXX,XX)
    else:
        parseurGeneral(chaine,place+1,estXX,XX)

def parseurEt(chaine,place):
    return parseurGeneral(chaine,place,estAnd,"AND")
def parseurOu(chaine,place):
    return parseurGeneral(chaine,place,estOr,"OR")

def parseurEtb(chaine,place): 
    if len(chaine)<=place:
        return
    if estAnd(chaine[place]):
        if place==0 or not estExp(chaine[place-1]):
            lance_erreur("erreur de syntaxe")
        if place+1>=len(chaine) or not estExp(chaine[place+1]):
            lance_erreur("erreur de syntaxe")
        a=CreerNoeudI(chaine[place-1],"AND",chaine[place+1])
        del chaine[place-1:place+2]
        chaine.insert(place-1,a)
        parseurEtb(chaine,place)
    elif estExp(chaine[place]) and place>0 and estExp(chaine[place-1]):
        a=CreerNoeudI(chaine[place-1],"AND",chaine[place])
        del chaine[place-1:place+1]
        chaine.insert(place-1,a)
        parseurEtb(chaine,place)
    else :
        parseurEtb(chaine,place+1)


def parseurNot(chaine,place):
    if place >= len(chaine):
        return
    o=chaine[place]
    if estNot(o):
        n=longueurNot(chaine,place)
        if place+n>=len(chaine):
            lance_erreur("erreur de syntaxe")
        o=chaine[place+n]
        if not estExp(o):
            lance_erreur("erreur de syntaxe")
        del chaine[place:place+n+1]
        if n%2==0:
            chaine.insert(place,o)
        else:
            chaine.insert(place,CreerNoeudI(o,"NOT",False))
    parseurNot(chaine,place+1)
        

def estAnd(o): # renvoie True si o est un And
    return type(o)==str and (o.upper()=="AND" or o.upper()=="ET" or o=="."  or o=="*")
def estNot(o): # renvoie True si o est un not
    return type(o)==str and (o.upper()=="NOT" or o.upper()=="NON")
def estOr(o): # renvoie True si o est un not
    return type(o)==str and (o.upper()=="OR" or o.upper()=="OU" or o=="+")

def estExp(c):
    # renvoie vrai si o est un expression 
    if hasattr(c,"etiquette"):
        return True
    return False

def estTrueFalse(c):
    if type(c)==str:
        c=c.upper()
        if c in set(["TRUE","T","V","VRAI","1"]):
            return True
        if c in set(["FALSE","F","FAUX","0"]):
            return False
    return "erreur"

def numerobit(c):
    # renvoie erreur si c est une chaine qui  designt pas un bit b0 b1 b2 b3
    if type(c)!=str:
        return "erreur"
    u=c.upper()
    if u[0]=="B" and len(c)==2:
        try :
            a=int(u[1])
        except ValueError:
            lance_erreur("erreur : verifier l'expression, elle doit etre la forme b0 ou b1 ou b2 ou b3 ou False ou True ou T ou V Vrai Faux")
        if a>3:
            return "erreur"
        return a
    return "erreur"


def estParentheseO(c): # renvoie True si c est une parenthese ouverte.
    return c=="("
def estParentheseF(c) : # renvoie True si c est une parenthes fermante
    return c==")"
def CreerNoeudI(a,b,c): 
    o=Objet()
    o.etiquette=b
    o.gauche=a
    o.droite=c
    return o

    
def tailleExpression(chaine,place,comptparenth) : 
    # renvoie la longueur des que comptparenth tombe a zero
    if len(chaine)<=place:
        lance_erreur("expression mal parenthesee")
    if(estParentheseF(chaine[place])) :
        if(comptparenth==1):
            return 1
        else:
            return 1+tailleExpression(chaine,place+1,comptparenth-1)
    if(estParentheseO(chaine[place])):
        return tailleExpression(chaine,place+1,comptparenth+1)+1
    return tailleExpression(chaine,place+1,comptparenth)+1



def longueurNot(chaine,place):
    # renvoie la longueur du plus long mot de not qui suit
        if len(chaine)> place and estNot(chaine[place]):
            return 1+longueurNot(chaine,place+1)
        else:
            return 0
#}}} fin partie creation d'arbre

import sys
def ecrire(s):
    sys.stdout.write(s)


def decoupeEnListe(chaine,place,sortie,mot):
    def ajoutermot():
        if mot!=[]:
            sortie.append("".join(mot))
    if place >= len(chaine) :
        ajoutermot()
        return
    a=chaine[place]
    if a==')' or a=='(' or a=='+' or a=='*' or\
         a=='.' or a=="=" :
        ajoutermot()
        sortie.append(a)
        decoupeEnListe(chaine,place+1,sortie,[])
        return
    if a==' ' or a=="\t":
        ajoutermot()
        decoupeEnListe(chaine,place+1,sortie,[])
        return
    mot.append(a)
    decoupeEnListe(chaine,place+1,sortie,mot)

def affiche_arbre(c):
    if hasattr(c,"etiquette"):
        if c.etiquette=="NOT":
            return "NOT( "+affiche_arbre(c.gauche)+" )"  
        if c.etiquette=="CONST":
            return repr(c.val)
        if c.etiquette=="BIT":
            return "B"+str(c.nombre)
        return "( "+affiche_arbre(c.gauche)+" "+c.etiquette+" "+\
                affiche_arbre(c.droite)+" )"
    return c
    
def calcul(expression,valeur):
    if expression.etiquette=="CONST":
        return expression.val
    elif expression.etiquette=="BIT":
        return valeur[expression.nombre]
    elif expression.etiquette=="AND":
        return calcul(expression.gauche,valeur) and calcul(expression.droite,valeur)
    elif expression.etiquette=="OR":
        return calcul(expression.gauche,valeur) or calcul(expression.droite,valeur)
    elif expression.etiquette=="NOT":
        return not calcul(expression.gauche,valeur)
        
def conversion(n):
    return [n%2==1,int((n/2))%2==1,int((n/4))%2==1,int((n/8))%2==1]

def evaluer(s,val):
    a=[]
    decoupeEnListe(s,0,a,[])
    c=parseur(a)
    return calcul(c,val)


sorties={
            "SH":None,
            "SB":None,
            "SM":None,
            "SGH":None,
            "SGB":None,
            "SDB":None,
            "SDH":None,
            }

# tracee :

Hauteur=2 # hauteur d'une barre verticale en caractere
Largeur=4 # largeur d'une barre horizontale en caractere
# un afficheur est prend donc Largeur+2 de largeur et Hauteur*2+3 de hauteur
Espace=5

def tracerVertical(x,y,Tableau,car):
    global Hauteur
    for i in range(Hauteur):
        Tableau[x][y+i]=car

def tracerHorizontal(x,y,Tableau,car):
    global Largeur
    for i in range(Largeur):
        Tableau[x+i][y]=car


barre={ 
    "SH":(tracerHorizontal,(1,0),"-"),
    "SB":(tracerHorizontal,(1,2*Hauteur+2),"-"),
    "SM":(tracerHorizontal,(1,Hauteur+1),"-"),
    "SGH":(tracerVertical,(0,1),"|"),
    "SGB":(tracerVertical,(0,2+Hauteur),"|"),
    "SDB":(tracerVertical,(1+Largeur,2+Hauteur),"|"),
    "SDH":(tracerVertical,(1+Largeur,1),"|")
    }

def designerSegment(s):
    # modifie s pour standardiser segment et le renvoie
    # renvoie "erreur" si ce n'est pas un segment valable
    s=s.upper()
    if s[0]!="S":
        return "erreur"
    if len(s)==2 and (s[1]=="H" or s[1]=="B" or s[1]=="M"):
        return s
    if len(s)==3 :
        if (s[1:]=="GH" or s[1:]=="HG"):
            return "SGH"
        if (s[1:]=="GB" or s[1:]=="BG"):
            return "SGB"
        if (s[1:]=="DB" or s[1:]=="BD"):
            return "SDB"
        if (s[1:]=="DH" or s[1:]=="HD"):
            return "SDH"
    return "erreur"


def coller(col,ligne,sortie,Tableau):
    # colle le baton sortie dans Tableau decale de col et ligne
    (trace,(x,y),car)=barre[sortie]
    trace(col+x,ligne+y,Tableau,car)


def main1():
    global Largeur,Hauteur,Espace,sorties
    f= open("expression","r")
    Lignes=f.readlines()
    for i,ligne in  enumerate(Lignes) : # boucle qui associe les arbres dexpression aux segments
        a=[]
        decoupeEnListe(ligne[:-1],0,a,[])
        if len(a)>0:
            sor=designerSegment(a[0])
            if sor in sorties :
                if a[1]!="=":
                    lance_erreur("erreur ligne "+i)
                sorties[sor]=parseur(a[2:])
    for i,v in sorties.items(): # verifie que chaque segment a une expression associe
        if v==None:
            lance_erreur("erreur il manque l'expression de "+ i.lower())
    Tableau=[[" "]*120  for i in range(120)]
    for i in range(10): # dessine le resultat
        v=conversion(i)
        Tableau[int(Largeur/2)+i*(Largeur+Espace)][1]=str(i)
        for sort,exp in sorties.items():
            c=calcul(exp,v)
            if c:
                coller(i*(Largeur+Espace),3,sort,Tableau) # i*Largeur
    for y in range((3+2*Hauteur)+5):
        for x in range(((2+Largeur+Espace)*10)):
            ecrire(Tableau[x][y])
        ecrire("\n")
    f.close()

main1()
