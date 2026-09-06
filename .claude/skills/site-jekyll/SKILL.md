---
name: site-jekyll
description: >-
  Maintenir le site Jekyll du dépôt lors de la création, du déplacement ou du
  renommage de pages, ou de changements de navigation, d'index et de liens,
  y compris les références aux photos.
---

# Navigation et liens du site

Site Jekyll avec le thème Just the Docs, configuré dans
[_config.yml](../../../_config.yml). Le push sur `main` déclenche le déploiement
GitHub Pages via [pages.yml](../../../.github/workflows/pages.yml).

## Front matter

Pour une fiche, utiliser le titre exact de l'index de section comme `parent`
(accents et espaces compris), et un entier `nav_order` :

```yaml
---
title: Crêpes sans gluten
parent: Pâtisserie
nav_order: 15
---
```

Le numéro ci-dessus est un exemple : lire les valeurs existantes avant de
choisir le numéro réel. Les index de section ont leur propre front matter
(`layout: default`, `has_children: true`, `permalink: /Section/`) ; ne pas
le recopier dans une recette.

## Ordre de navigation

À chaque ajout, suppression, déplacement ou réorganisation :

1. Lister les `title`, `parent` et `nav_order` des pages concernées.
2. Garder des entiers consécutifs et uniques entre pages du même `parent`.
   Renuméroter les suivantes si nécessaire. L'index de section est ordonné
   avec les autres pages de premier niveau, pas avec ses recettes.
3. Vérifier l'absence de doublon dans chaque groupe concerné ; le build ne
   signale pas nécessairement les collisions. Exemple pour les fiches de
   `Patisserie/` (sortie attendue vide) :

   ```powershell
   Get-ChildItem Patisserie -Filter *.md |
     Where-Object Name -ne 'index.md' |
     Select-String -Pattern '^nav_order:\s*(\d+)\s*$' |
     ForEach-Object { $_.Matches[0].Groups[1].Value } |
     Group-Object | Where-Object Count -gt 1
   ```

4. Aligner la liste « Recettes disponibles » de l'index de section sur cet
   ordre. Mettre à jour aussi les références de l'index racine, du README et
   des autres fiches si elles sont affectées.

## Liens et images

* Entre fiches : lien Markdown relatif vers le fichier `.md`, par exemple
  `[Mix farines](MixFarinesPatisserie.md)`.
* Depuis l'index racine du site : utiliser `relative_url`, par exemple
  `[Pain]({{ '/Pain/' | relative_url }})`.
* Pour toutes les images des pages Jekyll, y compris les recettes :
  `![Description]({{ '/Photos/NOM.jpg' | relative_url }})`.
* Exception pour le README racine, affiché directement sur GitHub :
  `![Description](Photos/NOM.jpg)` ; ne pas y utiliser Liquid.

Écrire un texte alternatif descriptif. Vérifier les cibles et, lors d'un
renommage, remplacer les références existantes. Pour préparer une image,
utiliser [photos-recettes](../photos-recettes/SKILL.md).
