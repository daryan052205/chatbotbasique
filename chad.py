import re
import otherresponse as other

def probabilité(user_message, mots_reconnu , réponse_unique=False,mots_requis=[] ):
    messagecertainty=0
    has_required=True

    for word in user_message:
        if word in mots_reconnu:
            messagecertainty+=1
    pourcentage=float(messagecertainty)/float(len(mots_reconnu))
    for a in mots_requis:
        if a not in user_message :
            has_required=False
            
    if  réponse_unique or has_required:
        return pourcentage*100
    else:
      
        return 0
    
def checkallmessages(message):
    high_problist={}

    def reponse(réponse_du_bot,liste_de_mot,réponse_unique=False,mots_requis=[]):
        nonlocal high_problist
        high_problist[réponse_du_bot]=probabilité(message,liste_de_mot,réponse_unique,mots_requis)
    #repone--------------------------------
    reponse('salut!',['salut','hey','bonjour','bonsoir'],réponse_unique=True)
    reponse('ça va et toi ?',['comment','tu','va',],réponse_unique=False,mots_requis=['comment'])
    reponse('bien et toi ?',['ça','va',],réponse_unique=False,mots_requis=['ça'])
    reponse(other.react,['qui','es ','tu'],réponse_unique=False,mots_requis=['qui'])
    reponse(other.react1,['bien','tranquille','ouais',"vais ","pète",'forme' ],réponse_unique=True)
    #reponse(other.react2,['comment','vas','tu','ça','va',],réponse_unique=False,mots_requis=['ça'])
    #reponse(other.react3,['comment','vas','tu','ça','va',],réponse_unique=False,mots_requis=['ça'])
  
    
    meilleur_choix= max(high_problist,key=high_problist.get )
    
    if high_problist[meilleur_choix]<1:
        return other.inconnu()
    else:
        return meilleur_choix

 

def reponse_donnee(input):
    splitmessage=re.split(r'\s+|[,;?!.-]\s*', input.lower())
    reponse= checkallmessages(splitmessage)
    return reponse




while True:
    print('bot:'+ reponse_donnee(input('you:')) )

  
    