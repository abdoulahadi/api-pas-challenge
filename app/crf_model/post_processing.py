def group_entities(annotated_sentence):
    grouped_entities = []
    current_entity = None

    for word, label in annotated_sentence:
        if label.startswith("B-"):  # Nouvelle entité
            if current_entity is not None:
                grouped_entities.append(current_entity)
            current_entity = {"entity": label[2:], "words": [word]}
        elif label.startswith("I-") and current_entity is not None:  # Continuation de l'entité
            current_entity["words"].append(word)
        else:  # Étiquette non liée à une entité
            if current_entity is not None:
                grouped_entities.append(current_entity)
            current_entity = None

    # Traitez la dernière entité si elle existe
    if current_entity is not None:
        grouped_entities.append(current_entity)

    return grouped_entities
