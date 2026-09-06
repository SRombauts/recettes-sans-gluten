# Recettes sans gluten

Ce dépôt contient des mélanges de farines et des recettes de boulangerie,
pâtisserie et cuisine sans gluten. Ce fichier porte les règles communes ;
les skills ci-dessous portent les procédures et exemples.

## Objectifs

Par ordre de priorité décroissante :

1. Goût agréable, doux mais riche, subtil.
2. Texture, consistance, légèreté et aération.
3. Limiter l'apport de sucre raffiné ajouté, en réduisant les quantités
   excessives ; le remplacement par des fruits reste une option.
4. Augmenter les protéines, avec un objectif d'IG modéré en prévention du
   diabète de type 2 et pour soutenir une activité physique régulière.
5. Limiter les graisses saturées, en prévention du cholestérol.
6. Garder un prix contenu.

Ces objectifs guident les adaptations ; ils n'imposent ni suppression du sucre
ou du beurre, ni création de variantes. Respecter une demande de reprise
fidèle d'une recette, notamment depuis un site web.

## Travail dans le dépôt

* Éditer et créer directement les fichiers nécessaires. Corriger sans demander
  les erreurs évidentes, de calcul et les oublis de mise à jour.
* Chaque recette et mélange doit avoir une analyse nutritionnelle pour 100 g,
  à actualiser lorsque sa composition change, selon `fiche-recette`.
* Vérifier et commiter sans attendre selon `workflow-depot`.

## Skills à charger

Lire les skills applicables avant d'agir ; ne pas recopier leurs règles ici.

| Quand | Skill |
| --- | --- |
| Début de toute tâche : ton et évaluation critique | [agent-response-style](.claude/skills/agent-response-style/SKILL.md) |
| Modifier des fichiers, vérifier et préparer des commits | [workflow-depot](.claude/skills/workflow-depot/SKILL.md) |
| Créer ou réviser une recette, un mélange ou son analyse nutritionnelle | [fiche-recette](.claude/skills/fiche-recette/SKILL.md) |
| Créer, déplacer ou renommer une page ; modifier navigation, index ou liens | [site-jekyll](.claude/skills/site-jekyll/SKILL.md) |
| Ajouter, remplacer, préparer ou vérifier une photo avant `git add` | [photos-recettes](.claude/skills/photos-recettes/SKILL.md) |
| Réécrire substantiellement la prose française d'une fiche, ou sur demande explicite d'humanisation | [boileau](.claude/skills/boileau/SKILL.md) |

Boileau ne se charge pas pour une simple mise à jour de quantités, de calculs,
de liens, de mise en forme ou une correction ponctuelle de formulation. Le
charger si la tâche comporte aussi une véritable réécriture de passages.

## Ressource externe

`.claude/skills/boileau/` est une copie de
[alxbd/boileau](https://github.com/alxbd/boileau). Ne jamais modifier,
reformater, traduire, raccourcir ni adapter localement ses fichiers. Seule une
mise à jour par copie fidèle de la source amont est autorisée ; indiquer la
version ou le commit amont dans le message de commit. Toute consigne propre
au projet doit rester hors de ce dossier.
