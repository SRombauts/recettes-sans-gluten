---
name: workflow-depot
description: >-
  Organiser les modifications du dépôt, leurs vérifications et leur découpage
  en commits atomiques. À charger pour toute tâche modifiant des fichiers
  ou préparant des commits.
---

# Modifications et commits

Lire le statut et les diffs existants avant d'éditer. Préserver les changements
hors du périmètre de la demande ; indexer explicitement les fichiers ou portions
relevant du sujet traité.

## Séparer les sujets sans casser le projet

* Un commit porte un seul sujet cohérent. Séparer les modifications indépendantes,
  même si elles viennent d'une même demande ou touchent un même fichier.
* Chaque commit doit laisser le projet cohérent et utilisable, sans dépendre
  d'un commit ultérieur pour fonctionner. Ordonner les commits selon leurs
  dépendances ; regrouper les changements indissociables.
* Garder ensemble une photo et ses références, une recette et son analyse
  nutritionnelle actualisée, ou un déplacement de page et les liens affectés.
  Une extraction de règles inclut leurs destinations et les renvois nécessaires.
* Si la demande modifie des instructions puis les applique au contenu, commiter
  d'abord les instructions et skills vérifiés, puis leur application aux recettes
  ou autres contenus vérifiés. Ne regrouper ces étapes que sur demande explicite.

## Vérifier et commiter

Pour chaque commit, effectuer les contrôles adaptés au sujet selon les skills
concernés : calculs nutritionnels, liens et navigation, photos ou tests de scripts.
Vérifier l'état réellement indexé avec `git diff --cached` et
`git diff --cached --check` : un contrôle du répertoire de travail seul ne suffit
pas si certaines modifications restent hors du commit.

Après vérification, effectuer le commit sans attendre, avec un message court
décrivant le changement. Contrôler ensuite `git status` et signaler les éventuels
changements restants ou vérifications impossibles. L'autorisation de commiter
n'implique pas celle de pousser vers le dépôt distant.
