import string
def word2features(sent, i):
    # Récupérer le mot actuel et son étiquette
    word, tag = sent[i]

    # Initialiser le dictionnaire des caractéristiques
    features = {
        'bias': 1.0,  # Terme de biais
        'word.lower()': word.lower(),  # Mot en minuscules
        'word.upper()': word.upper(),  # Mot en majuscules
        'word[-3:]': word[-3:],  # Les 3 derniers caractères du mot
        'word.isupper()': word.isupper(),  # Le mot est-il entièrement en majuscules ?
        'word.istitle()': word.istitle(),  # Le mot commence-t-il par une majuscule ?
        'word.isdigit()': word.isdigit(),  # Le mot est-il un nombre ?
        'word.isalpha()': word.isalpha(),  # Le mot est-il composé uniquement de lettres ?

        # Caractéristiques supplémentaires
        'word.length()': len(word),  # Longueur du mot
        'word.hasdigits()': any(char.isdigit() for char in word),  # Présence de chiffres
        'word.hasuppercase()': any(char.isupper() for char in word[1:]),  # Majuscules en milieu de mot

        # Caractéristiques lexicales
        'prev_word': 'BOS' if i == 0 else sent[i - 1][0],  # Mot précédent ou BOS si premier mot
        'next_word': 'EOS' if i == len(sent) - 1 else sent[i + 1][0],  # Mot suivant ou EOS si dernier mot

        # Caractéristiques de ponctuation
        'word.haspunctuation()': any(char in string.punctuation for char in word),  # Présence de ponctuation
    }

    if i > 0:
        # Si ce n'est pas le premier mot dans la phrase
        word1, tag1 = sent[i - 1]
        features.update({
            '-1:word.lower()': word1.lower(),
            'prev_word.isupper()': word1.isupper(),
            'prev_word.istitle()': word1.istitle(),
            'prev_word.isdigit()': word1.isdigit(),
            'prev_word.isalpha()': word1.isalpha(),
            '-1:tag': tag1,  # Étiquette du mot précédent
        })
    else:
        # Si c'est le premier mot dans la phrase
        features['BOS'] = True  # Marqueur de début de phrase (Beginning of Sentence)

    if i < len(sent) - 1:
        # Si ce n'est pas le dernier mot dans la phrase
        word2, tag2 = sent[i + 1]
        features.update({
            '+1:word.lower()': word2.lower(),
            'next_word.isupper()': word2.isupper(),
            'next_word.istitle()': word2.istitle(),
            'next_word.isdigit()': word2.isdigit(),
            'next_word.isalpha()': word2.isalpha(),
            '+1:tag': tag2,  # Étiquette du mot suivant
        })
    else:
        # Si c'est le dernier mot dans la phrase
        features['EOS'] = True  # Marqueur de fin de phrase (End of Sentence)

    # Caractéristiques lexicales
    # Mots voisins à gauche
    if i > 1:
        word2, tag2 = sent[i - 2]
        features.update({
            '-2:word.lower()': word2.lower(),
            'prev_prev_word.isupper()': word2.isupper(),
            'prev_prev_word.istitle()': word2.istitle(),
            'prev_prev_word.isdigit()': word2.isdigit(),
            'prev_prev_word.isalpha()': word2.isalpha(),
            '-2:tag': tag2,  # Étiquette du mot précédent précédent
        })

    # Mots voisins à droite
    if i < len(sent) - 2:
        word3, tag3 = sent[i + 2]
        features.update({
            '+2:word.lower()': word3.lower(),
            'next_next_word.isupper()': word3.isupper(),
            'next_next_word.istitle()': word3.istitle(),
            'next_next_word.isdigit()': word3.isdigit(),
            'next_next_word.isalpha()': word3.isalpha(),
            '+2:tag': tag3,  # Étiquette du mot suivant suivant
        })

    return features



def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [label for word, label in sent]