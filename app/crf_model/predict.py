# import re
# from .pre_processing import word2features
# from .tagger import initialize_tagger

# def predict_annotations(sentence):
#     tagger = initialize_tagger()

#     # Divisez la phrase en mots ou en ponctuation en utilisant une expression régulière
#     words = re.findall(r'\b\w+\b|[.,!?;:]', sentence)

#     # Extraction des caractéristiques de la phrase
#     input_sentence = [(word, "") for word in words]

#     # Utilisez le modèle (tagger) pour annoter la phrase
#     predicted_labels = tagger.tag([word2features(input_sentence, i) for i in range(len(input_sentence))])

#     # Créez un dictionnaire pour stocker les groupes de mots
#     grouped_words = {}
#     start = 0
#     sentences = ""

#     # Parcourez les mots et leurs étiquettes prédites
#     for i in range(len(input_sentence)):
#         word, label = input_sentence[i], predicted_labels[i]

#         # Ajoutez le mot à la phrase en cours
#         sentences += word[0] + " "

#         if label.startswith('B-'):
#             tag = label[2:]  # Supprimez le préfixe 'B-'

#             # Créez un groupe de mots
#             group = {
#                 "mot": word[0],
#                 "debut": len(sentences) - 1 - len(word[0]),
#                 "fin": len(sentences) - 1,
#                 "tag": tag
#             }
#             j = i + 1

#             # Recherchez les mots suivants avec des étiquettes I-
#             while j < len(input_sentence) and predicted_labels[j].startswith('I-' + tag):
#                 group["mot"] += " " + input_sentence[j][0]
#                 group["fin"] += len(input_sentence[j][0]) + 1  # Ajoutez 1 pour l'espace
#                 start = group["fin"] + 1
#                 j += 1

#             # Ajoutez le groupe de mots au dictionnaire
#             if tag in grouped_words:
#                 grouped_words[tag].append(group)
#             else:
#                 grouped_words[tag] = [group]

#         elif label == "O":
#             start += len(word) + 1  # Ajoutez 1 pour l'espace

#     return {"annotated_text": grouped_words, "sentences": sentences}


import re
from .pre_processing import word2features
from .tagger import initialize_tagger

def predict_annotations(sentence):
    tagger = initialize_tagger()

    # Divisez la phrase en mots ou en ponctuation en utilisant une expression régulière
    words = re.findall(r'\b\w+\b|[.,!?;:]', sentence)

    # Extraction des caractéristiques de la phrase
    input_sentence = [(word, "") for word in words]

    # Utilisez le modèle (tagger) pour annoter la phrase
    predicted_labels = tagger.tag([word2features(input_sentence, i) for i in range(len(input_sentence))])

    # Créez une liste pour stocker les entités nommées
    entities = []
    start = 0
    sentences = ""

    # Parcourez les mots et leurs étiquettes prédites
    for i in range(len(input_sentence)):
        word, label = input_sentence[i], predicted_labels[i]

        # Ajoutez le mot à la phrase en cours
        sentences += word[0] + " "

        if label.startswith('B-'):
            tag = label[2:]  # Supprimez le préfixe 'B-'

            # Créez une entité nommée
            entity = {
                "text": word[0],
                "label": tag,
                "start": len(sentences) - 1 - len(word[0]),
                "end": len(sentences) - 1
            }
            j = i + 1

            # Recherchez les mots suivants avec des étiquettes I-
            while j < len(input_sentence) and predicted_labels[j].startswith('I-' + tag):
                entity["text"] += " " + input_sentence[j][0]
                entity["end"] += len(input_sentence[j][0]) + 1  # Ajoutez 1 pour l'espace
                start = entity["end"] + 1
                j += 1

            # Ajoutez l'entité nommée à la liste d'entités
            entities.append(entity)

        elif label == "O":
            start += len(word) + 1  # Ajoutez 1 pour l'espace

    return {"entities": entities, "sentences": sentences}
