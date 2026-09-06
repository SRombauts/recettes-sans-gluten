# Recettes sans gluten

Ce dépôt contient des mélanges de farines et des recettes de boulangerie,
pâtisserie et cuisine sans gluten. Ce fichier porte les règles communes ;
les skills ci-dessous portent les procédures et exemples.

## Objectifs

Par ordre de priorité décroissante :

1. Goût agréable, doux mais riche, subtil.
2. Texture, consistance, légèreté et aération.
3. Éviter autant que possible le sucre raffiné ajouté ; privilégier les fruits
   (banane, compote) ou une sucrosité minimale.
4. Augmenter les protéines, avec un objectif d'IG modéré en prévention du
   diabète de type 2 et pour soutenir une activité physique régulière.
5. Limiter les graisses saturées, en prévention du cholestérol.
6. Garder un prix contenu.

## Travail dans le dépôt

* Éditer et créer directement les fichiers nécessaires. Corriger sans demander
  les erreurs évidentes, de calcul et les oublis de mise à jour.
* Chaque recette et mélange doit avoir une analyse nutritionnelle pour 100 g,
  à actualiser lorsque sa composition change, selon `fiche-recette`.
* Après vérification, effectuer le commit sans attendre, avec un message court.
  Un commit correspond à un sujet cohérent ; garder ensemble les éléments
  indissociables, par exemple une photo et ses références.
* Si une demande modifie les instructions et les applique au contenu, faire
  deux commits : d'abord les instructions et skills vérifiés, puis leur
  application aux recettes ou autres contenus vérifiés. Ne les regrouper que
  sur demande explicite.

## Skills à charger

Lire les skills applicables avant d'agir ; ne pas recopier leurs règles ici.

| Quand | Skill |
| --- | --- |
| Début de toute tâche : ton et évaluation critique | [agent-response-style](.claude/skills/agent-response-style/SKILL.md) |
| Créer ou réviser une recette, un mélange ou son analyse nutritionnelle | [fiche-recette](.claude/skills/fiche-recette/SKILL.md) |
| Créer, déplacer ou renommer une page ; modifier navigation, index ou liens | [site-jekyll](.claude/skills/site-jekyll/SKILL.md) |
| Ajouter, remplacer, préparer ou vérifier une photo avant `git add` | [photos-recettes](.claude/skills/photos-recettes/SKILL.md) |
| Rédiger ou relire la prose française des fiches | [boileau](.claude/skills/boileau/SKILL.md) |

## Ressource externe

`.claude/skills/boileau/` est une copie de
[alxbd/boileau](https://github.com/alxbd/boileau). Ne jamais modifier,
reformater, traduire, raccourcir ni adapter localement ses fichiers. Seule une
mise à jour par copie fidèle de la source amont est autorisée ; indiquer la
version ou le commit amont dans le message de commit. Toute consigne propre
au projet doit rester hors de ce dossier.
