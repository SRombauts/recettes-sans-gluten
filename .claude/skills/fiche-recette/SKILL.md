---
name: fiche-recette
description: >-
  Rédiger, réviser ou maintenir une fiche recette du dépôt recettes-sans-gluten :
  structure du corps de la fiche, section « Notes » organisée par objectif,
  méthodologie de l'analyse nutritionnelle pour 100 g, et liens entre variantes
  (avec / sans beurre). À utiliser dès qu'on ajoute une recette, qu'on en révise
  une, ou qu'on recalcule une analyse nutritionnelle. Le front matter Jekyll, le
  `nav_order`, les liens internes et les photos sont décrits dans `AGENTS.md` —
  ne pas les dupliquer ici, s'y référer.
---

# Rédiger / réviser une fiche recette

Conventions du **corps** d'une fiche (le front matter YAML, `nav_order`, liens
`relative_url` et photos sont dans `AGENTS.md`, section Jekyll/Photos). Objectifs
du projet, par priorité : goût → texture → sans sucre raffiné → protéines (IG
modéré) → moins d'AGS → prix.

## Squelette d'une fiche

Un seul `#` (H1) par page ; les sections sont en `##`, les sous-points de Notes
en `###`. La fiche la plus aboutie à recopier est `Patisserie/ClafoutisCerises.md`.

```markdown
# <Titre> sans gluten[ (avec beurre)]

[*Variante sans beurre : [<Titre> sans beurre](XxxSansBeurre.md).*]

<1-2 phrases : ce qui caractérise la recette + écarts volontaires vs la version
classique, motivés par les objectifs.>

## Ingrédients[ (pour N personnes)]

* quantités alignées, lien vers `MixFarinesPatisserie.md` au premier usage

## Préparation

1. étapes numérotées

## Cuisson

* four/poêle, températures, durées, repères visuels

## Analyse nutritionnelle pour 100 g

## Notes
```

Pièges déjà rencontrés :

* **Plusieurs `#` (H1) dans une page** = erreur Markdown ; les vieilles fiches
  (`Crepes.md`, `Gaufres.md` à l'origine) en avaient, à corriger en `##`.
* Liste d'**ingrédients sans en-tête** `## Ingrédients` : toujours l'ajouter.

## Section « Notes » par objectif

Gabarit le plus utile (cf. Clafoutis / Crêpes) : d'abord quelques puces
**pratiques** (conservation, ajustements, « première fournée = test »), puis des
`###` classés **par objectif du projet** :

* `### Réduire / Parfumer sans sucre raffiné` — sucre complet (rapadura,
  muscovado : **non raffiné**, donne une teinte caramel via Maillard), vanille,
  zestes, compote pour remplacer le sucre, etc.
* `### Limiter les graisses saturées` — version sans beurre inline, beurre
  noisette à gras égal, lait écrémé.
* `### Augmenter les protéines / baisser l'IG` — whey neutre, Skyr/fromage
  blanc, poudre d'amandes ; renvoyer vers `Notes/AugmenterTauxProteines.md`.
* `### Variantes` — autres fruits, salé/sarrasin, sans lactose/végétal.

Chiffrer l'impact quand c'est simple (« ~ +1 g de sucres / 100 g, négligeable »).

## Variantes avec / sans beurre

Deux variantes **quand c'est pertinent** (cf. objectif du projet) : fichier de
base = avec beurre, suffixe `SansBeurre` = gras issu de purées d'oléagineux,
compote ou chocolat. Les deux restent sans sucre raffiné.

* Se **renvoient mutuellement** par une ligne en italique sous le titre.
* L'`index.md` de section liste les deux avec leurs chiffres clés
  (protéines / 100 g, parfois sucres ou AGS).
* **Ne pas créer** de fichier `SansBeurre` quand le beurre est anecdotique
  (ex. crêpes : 20 g) — le traiter en Note inline.

## Analyse nutritionnelle pour 100 g

Toujours présente, **mise à jour à chaque changement d'ingrédient**. Méthode :

1. Sommer chaque nutriment sur tous les ingrédients (utiliser
   `MixFarinesPatisserie.md` pour le mix : 355 kcal, MG 2,3 / AGS 0,5, glucides
   77,8 / sucres 1,3, fibres 4,0, prot 6,1, sel 0 pour 100 g).
2. Diviser par la **masse totale** et ramener à 100 g.
3. **Énoncer les hypothèses** juste avant le tableau : avant ou après cuisson,
   % d'eau évaporée et masse cuite estimée, ce qui est **compté ou non**
   (ex. « beurre du moule non compté », « hors matière grasse de la poêle »),
   masse totale obtenue.

Ordre et libellés exacts du bloc (espace insécable avant `:` typographique FR) :

```markdown
* Énergie : XXX kcal
* Matières grasses : X,X g
  * dont acides gras saturés : X,X g
* Glucides : XX,X g
  * dont sucres : X,X g
* Fibres : X,X g
* Protéines : X,X g
* Sel : X,XX g
```

Repères de cohérence : œuf ≈ 50 g ; lait demi-écrémé ≈ 46 kcal, 1,6 g MG (dont
~1 g AGS), 4,8 g sucres, 3,3 g prot / 100 mL ; beurre ≈ 81 g MG dont ~51 g AGS /
100 g (donc 20 g de beurre ≈ 10 g AGS) ; huile ≈ 90 kcal/10 g.

## Workflow (rappel `AGENTS.md`)

Éditer directement, corriger sans demander les erreurs évidentes / de calcul /
d'oubli de mise à jour, recalculer l'analyse, **committer immédiatement** avec un
message court. Pour `nav_order`, liens et photos : voir `AGENTS.md`.
