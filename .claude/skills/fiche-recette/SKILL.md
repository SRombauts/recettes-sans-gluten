---
name: fiche-recette
description: >-
  Créer, réviser ou maintenir une recette ou un mélange de farines du dépôt :
  structure, notes, variantes avec ou sans beurre, calcul et présentation de
  l'analyse nutritionnelle pour 100 g.
---

# Fiches de recettes et mélanges

Les objectifs et le workflow commun sont définis dans
[AGENTS.md](../../../AGENTS.md). Pour le front matter, les index et les liens,
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

* Réduire ou parfumer sans sucre raffiné : fruits, compote, vanille, zestes,
  ou sucre complet en quantité minimale.
* Limiter les graisses saturées : substitutions du beurre, lait écrémé.
* Augmenter les protéines : whey neutre, skyr, fromage blanc, poudre
  d'amandes ; renvoi vers `Notes/AugmenterTauxProteines.md` à la racine.
* Variantes : autres fruits, salé, sans lactose ou végétal.

Expliquer l'intérêt et le compromis des substitutions. Chiffrer leur impact
nutritionnel quand le calcul est simple.

## Variantes avec et sans beurre

Pour les pâtisseries, proposer deux variantes quand c'est pertinent :

* Avec beurre : plus gourmande, pour les enfants ; nom de fichier de base.
* Sans beurre : variante visant moins de graisses saturées, avec purée
  d'oléagineux, compote ou chocolat selon la recette ; suffixe `SansBeurre`.

Les deux restent sans sucre raffiné ajouté. Les fiches se renvoient
mutuellement par une ligne en italique sous le titre. L'index de section
liste les deux avec leurs chiffres clés (protéines pour 100 g, parfois
sucres ou acides gras saturés).

Quand le beurre est anecdotique (ex. 20 g dans les crêpes), expliquer la
substitution dans les Notes plutôt que créer un fichier `SansBeurre`.

## Analyse nutritionnelle pour 100 g

1. Sommer chaque nutriment sur tous les ingrédients. Pour un mélange du
   dépôt, lire sa fiche actuelle, par exemple
   [Mix farines pâtisserie](../../../Patisserie/MixFarinesPatisserie.md) ;
   ne pas maintenir une seconde copie de ses valeurs dans ce skill.
2. Diviser les totaux par la masse du produit décrit (sec, cru ou cuit),
   puis multiplier par 100.
3. Préciser avant les valeurs : état cru ou cuit, masse retenue et hypothèse
   de perte à la cuisson si elle est estimée, ingrédients comptés ou exclus
   (ex. beurre du moule ou matière grasse de la poêle).

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

Repères de cohérence : œuf sans coquille environ 50 g ; lait demi-écrémé
environ 46 kcal, 1,6 g de matières grasses dont 1 g d'acides gras saturés,
4,8 g de sucres et 3,3 g de protéines pour 100 mL ; beurre environ 81 g de
matières grasses dont 51 g d'acides gras saturés pour 100 g ; huile environ
90 kcal pour 10 g. Ces repères ne remplacent pas les données des ingrédients.
