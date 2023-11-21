import pandas as pd
import pickle
import json
from sklearn.metrics.pairwise import cosine_similarity

#---------------------------------------Dataframe---------------------------------------------

df = pd.read_json('Data/df_clothes_embeded.json')
dfX = pd.read_csv('Data/dataset.csv')

dfX.columns = dfX.columns.str.strip()

#---------------------------------------PICKLE------------------------------------------------

with open('Model/modele.pickle', 'rb') as fichier:
    model = pickle.load(fichier)

#---------------------------------------Fonction pour modele BERT------------------------------

def BERT(requete, genre='WOM'):

  requete_code = model.encode(requete)

  laliste = []
  df3 = df[df['sexe']==genre]
  for i in list(df3['encoding_label']):
    laliste.append(i) 

  score_cos = cosine_similarity(
        [requete_code],
        laliste)
    
  score_cos = score_cos.tolist()

  d = {'sentence': df3['Image'], 'score': score_cos[0]}
  df2 = pd.DataFrame(data=d)

  df2 = df2.sort_values(by=['score'], ascending=False)

  return (df2.sentence[0:4].tolist())

#---------------------------------------Fonction la reco de taille ------------------------------


def find_size(marque, sexe, tour_poitrine, tour_taille, tour_hanche):
    selected_data = dfX[(dfX["Marque"] == marque) & (dfX["Sexe"] == sexe)]

    for index, row in selected_data.iterrows():
        if (row["Tour de poitrine"] >= tour_poitrine and
            row["Tour de taille"] >= tour_taille and
            row["Tour de hanches"] >= tour_hanche):
            return row["Taille"]

    return "XXXL or more"
