import re
from .pre_processing import word2features
from .tagger import initialize_tagger



def predict_annotations(text):
    tagger = initialize_tagger()
    # Découpez le texte en phrases en utilisant une expression régulière
    sentences = re.split(r'(?<=[.!?])\s', text)


    # Ajout de la déclaration ici
    entities = []
    start = 0
    sentences_text = ""
    for sentence in sentences:
        words = re.findall(r'\b\w+\b|[.,!?;:]', sentence)
        input_sentence = [(word, "") for word in words]
        predicted_labels = tagger.tag([word2features(input_sentence, i) for i in range(len(input_sentence))])


        for i in range(len(input_sentence)):
            word, label = input_sentence[i], predicted_labels[i]

            # Ajoutez le mot à la phrase en cours
            sentences_text += word[0] + " "

            if label.startswith('B-'):
                tag = label[2:]  # Supprimez le préfixe 'B-'

                # Créez une entité nommée
                entity = {
                    "text": word[0],
                    "label": tag,
                    "start": len(sentences_text) - 1 - len(word[0]),
                    "end": len(sentences_text) - 1
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
                start += len(word[0]) + 1  # Ajoutez 1 pour l'espace

    return {"entities": entities, "sentences": sentences_text}
