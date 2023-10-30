# FastAPI CRF-XelKoomIA

Ceci est une API permettant d'exposer un modèle NER basé sur le CRF en fournissant les entités nommées d'un texte envoyé ou d'un fichier pdf uploader.

## Table des matières

- [À Propos](#à-propos)
- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)

## À Propos

Le FastAPI CRF-XelKoomIA (Reconnaissance d'Entités Nomées) est un projet conçu pour le compte du challenge PAS par le groupe XelKoom-API afin de simplifier l'extraction d'entités nommées à partir de texte et de fichiers PDF. Cette API est basée sur FastAPI, un framework Python moderne pour le développement d'API web rapide.

## Fonctionnalités

Cette API FastAPI offre les fonctionnalités suivantes :

- **Extraction d'Entités Nomées (NER) :** Elle permet d'extraire les entités nommées d'un texte en utilisant un modèle NER pré-entrainé.

- **Traitement de Fichiers PDF :** Elle prend également en charge l'envoi de fichiers PDF pour l'extraction d'entités nommées à partir de ces fichiers.

- **Réponses Structurées :** Les réponses renvoyées par l'API sont structurées et bien formatées pour une intégration facile dans d'autres applications.

## Installation

Pour utiliser cette API sur votre propre système, suivez ces étapes :

1. Clônez le référentiel depuis GitHub :
   ```bash
    git clone https://github.com/abdoulahadi/api-pas-challenge.git
    cd api-pas-challenge

2. Installez les dépendances en créant un environnement virtuel :
   ```bash
    python -m venv venv
    source venv/bin/activate  # Sous Windows, utilisez 'venv\Scripts\activate'
    pip install -r requirements.txt

3. Lancez l'application FastAPI :
   ```bash
    uvicorn run:app --reload
L'API sera maintenant accessible localement à l'adresse http://127.0.0.1:8000.

## Utilisation
Vous pouvez utiliser cette API pour extraire des entités nommées à partir de texte ou de fichiers PDF en envoyant des requêtes HTTP POST.

- Pour extraire des entités nommées à partir d'un texte, envoyez une requête POST à l'URL http://127.0.0.1:8000/annotate-text avec le texte à analyser dans le corps de la requête.

- Pour extraire des entités nommées à partir d'un fichier PDF, envoyez une requête POST à l'URL http://127.0.0.1:8000/annotate-pdf en utilisant le champ de formulaire file pour téléverser le fichier PDF.
  
- Pour avoir une documentation de l'API, vous pouvez naviguer sur l'url offerte par FastAPI http://127.0.0.1:8000/docs

Assurez-vous de respecter le format de la requête et d'analyser les réponses structurées renvoyées par l'API.


