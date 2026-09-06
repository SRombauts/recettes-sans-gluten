---
name: fiche-recette
description: >-
  Créer, réviser ou maintenir une recette ou un mélange de farines du dépôt :
  structure, notes, adaptations facultatives, calcul et présentation de
  l'analyse nutritionnelle pour 100 g.
---

# Fiches de recettes et mélanges

Les objectifs sont définis dans [AGENTS.md](../../../AGENTS.md), les vérifications
et commits dans [workflow-depot](../workflow-depot/SKILL.md).
Pour le front matter, les index et les liens,
utiliser [site-jekyll](../site-jekyll/SKILL.md).

## Structure

Un seul titre `#` par page est la convention du projet. Utiliser `##` pour les
sections et `###` pour les sous-sections de Notes. Adapter ce gabarit au type
de fiche : un mélange sec n'a pas de cuisson, un levain peut avoir une section
d'entretien. Toujours nommer la liste d'ingrédients et inclure l'analyse.

```markdown
# <Titre> sans gluten

*Variante sans beurre : [<Titre> sans beurre](XxxSansBeurre.md).*

<Une ou deux phrases sur la recette et ses écarts volontaires au classique.>

## Ingrédients (pour N personnes)

* Quantités et lien vers la fiche du mélange de farines au premier usage.

## Préparation

1. Étapes numérotées.

## Cuisson

* Four ou poêle, température, durée et repères visuels.

## Analyse nutritionnelle pour 100 g

## Notes
```

La ligne de variante n'est présente que si cette variante existe. Les recettes
existantes illustrent des choix culinaires ; le gabarit fait référence pour
la structure.

## Notes par objectif

Commencer par les indications pratiques utiles (conservation, ajustements,
première fournée à tester), puis les sous-sections pertinentes :

* Réduire le sucre ajouté lorsque la recette est trop dosée ; en option,
  remplacer tout ou partie du sucre raffiné par compote, banane ou dattes.
* Limiter les graisses saturées : réduire le beurre ou proposer une
  substitution si elle est utile, sans imposer sa suppression.
* Augmenter les protéines : whey neutre, skyr, fromage blanc, poudre
  d'amandes ; renvoi vers `Notes/AugmenterTauxProteines.md` à la racine.
* Variantes : autres fruits, salé, sans lactose ou végétal.

Expliquer l'intérêt et le compromis des substitutions. Chiffrer leur impact
nutritionnel quand le calcul est simple.

## Reprise fidèle et adaptations facultatives

Lors d'une reprise demandée telle quelle, conserver les ingrédients, quantités
et étapes de la source. Ajouter la structure du dépôt, le lien vers la source
et l'analyse nutritionnelle, sans reformuler la composition pour atteindre
les objectifs. Signaler une incohérence de la source au lieu de la corriger
silencieusement. Les suggestions éventuelles restent distinctes de la recette.

Ne pas proposer ou créer systématiquement de variante sans sucre ou sans beurre.
Une petite quantité de beurre est compatible avec les objectifs ; le beurre du
moule est accepté, y compris dans une variante dite « sans beurre ». Dans ce
cas, préciser « sans beurre dans la pâte ; beurre pour le moule » : il s'agit
d'un choix nutritionnel, pas d'une garantie d'absence d'allergènes.

Si une adaptation est demandée ou utile, expliquer son intérêt et ses effets
attendus sur le goût, la texture et la nutrition. Une suggestion simple suffit
dans les Notes ; créer une fiche distincte seulement si elle est justifiée par
la demande ou l'ampleur des changements. Pour une variante sans beurre dans la
pâte, conserver le suffixe `SansBeurre`. Si deux fiches existent, les relier
mutuellement par une ligne en italique sous le titre et les lister dans l'index
avec leurs chiffres clés. Ne pas annoncer l'absence de sucre raffiné ajouté
si les ingrédients en apportent, y compris le sucre vanillé ou le chocolat.

## Analyse nutritionnelle pour 100 g

1. Lire les lignes utiles de la [référence nutritionnelle](references/nutrition.md).
   Réutiliser les valeurs locales adaptées à l'ingrédient ; chercher une source
   externe seulement si une donnée manque, si le produit diffère ou si une
   actualisation est demandée. Enregistrer les nouvelles valeurs avec leur
   source dans cette référence. Pour un mélange du dépôt, utiliser sa fiche
   actuelle, sans recopier ses résultats dans la référence.
2. Ramener chaque quantité à la base de sa donnée (100 g ou 100 mL), en comptant
   la partie comestible. Consigner les conversions et ingrédients comptés ou
   exclus. Calculer chaque contribution : quantité × valeur pour 100 / 100,
   puis sommer par nutriment. Ne pas assimiler une donnée manquante à zéro.
3. Diviser les totaux par la masse du produit décrit, puis multiplier par 100.
   Indiquer avant les valeurs l'état sec, cru ou cuit et la masse retenue,
   estimée ou mesurée. Conserver la masse de référence existante sauf nouvelle
   mesure ou changement de recette ; ne pas imposer de pesée supplémentaire.
4. Garder les décimales pendant le calcul, arrondir seulement à l'affichage.
   Conserver dans la référence nutritionnelle les choix de données et
   conversions propres à la fiche qui ne sont pas déjà explicités sur la page.
5. Lorsqu'un ingrédient, une valeur de référence ou un mélange change, chercher
   ses usages dans le dépôt (`rg`), puis recalculer les fiches concernées, y
   compris les dépendances indirectes (mélange → levain → pain). Actualiser
   aussi les chiffres repris dans les variantes, notes, index et comparaisons.
   Vérifier les quantités, les unités et la concordance de ces reprises avant
   le commit. Une nouvelle entrée de référence seule ne justifie pas de refaire
   toutes les recettes ; signaler les données anciennes non encore vérifiées.

Pour les recettes et mélanges, mettre en gras uniquement les valeurs
numériques exprimées en grammes, virgule comprise. Cela inclut les sous-puces
et les zéros (`**0** g`). Libellés, unité `g`, kcal et quantités d'ingrédients
restent hors de cette règle. Respecter cet ordre et ces libellés, avec une
espace insécable avant `:` :

```markdown
* Énergie : XXX kcal
* Matières grasses : **X,X** g
  * dont acides gras saturés : **X,X** g
* Glucides : **XX,X** g
  * dont sucres : **X,X** g
* Fibres : **X,X** g
* Protéines : **X,X** g
* Sel : **X,XX** g
```

## Prix internes

Pour un calcul ou un choix de coût, charger uniquement la
[référence des prix](references/prix-ingredients.md). Les prix d'achat et les
tableaux de coûts restent dans cette référence, sans affichage sur le site ni
dans le README. Ce sont des repères historiques, à actualiser sur demande ou
avec un nouveau prix fourni, pas des tarifs à rechercher à chaque recette.
