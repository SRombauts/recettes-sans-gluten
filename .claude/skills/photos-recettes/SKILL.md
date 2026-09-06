---
name: photos-recettes
description: >-
  Ajouter, remplacer, redimensionner ou vérifier les photos du dépôt avant
  leur indexation Git. Utiliser le script fourni pour préparer les JPEG
  explicitement sélectionnés, puis référencer les images dans les fiches.
---

# Photos des recettes

Les photos sont stockées dans `Photos/` à la racine. Traiter toute nouvelle
photo avant `git add` pour éviter d'introduire un JPEG lourd dans l'historique.

## Interpréteur

Vérifier Python et Pillow avec l'interpréteur disponible :

```powershell
python -c "import sys; from PIL import Image; print(sys.version); print('Pillow', Image.__version__)"
```

Si `python` est absent, chercher `py -3` ou un interpréteur fourni par
l'environnement de l'agent, puis utiliser son chemin absolu. Ne pas supposer
qu'un environnement virtuel ou une installation système existe. Réutiliser
un interpréteur disposant de Pillow ; sinon signaler la dépendance manquante.
Le script est prévu pour Python 3.12 ou supérieur et Pillow 12 ou supérieur.

## Préparer les fichiers sélectionnés

Depuis la racine du dépôt, lancer le
[script conservé dans ce skill](scripts/resize_photos.py) avec les chemins
exacts des nouvelles photos ; ne pas lancer de traitement global de `Photos/` :

```powershell
python .claude/skills/photos-recettes/scripts/resize_photos.py "Photos/NOUVELLE.jpg"
python .claude/skills/photos-recettes/scripts/resize_photos.py --check "Photos/NOUVELLE.jpg"
```

Plusieurs chemins peuvent être fournis. Avec un chemin d'interpréteur sous
PowerShell, employer `& 'C:/chemin/python.exe'` à la place de `python`.
Les chemins des photos sont relatifs au répertoire courant, ou absolus.

Le script traite les JPEG (`.jpg` ou `.jpeg`, casse indifférente) et remplace
chaque fichier après avoir écrit le résultat dans un fichier temporaire :

* orientation corrigée d'après EXIF, puis métadonnées supprimées, dont GPS ;
* proportions conservées, côté le plus long limité à 1600 px sans agrandir ;
* JPEG RGB, qualité 85, progressif et optimisé.

Ces paramètres sont les standards du projet ; ne les changer que pour une
raison explicite. Viser environ 250 à 500 Ko, sans agrandir ni dégrader
inutilement une image pour atteindre cette plage. Signaler tout résultat
supérieur à 1 Mio (1 048 576 octets).

`--check` ne modifie rien : il contrôle le format, les dimensions, le mode,
les métadonnées et le poids, mais ne peut pas certifier la qualité JPEG 85.
Un code de sortie non nul signale une erreur ou un contrôle non conforme.
Une recompression JPEG n'est pas idempotente : ne pas retraiter une photo
déjà préparée. Les chemins répétés dans une même commande sont dédupliqués.

## Vérification et insertion

1. Vérifier le résultat visuellement (orientation, détails, couleurs) et lire
   les dimensions et poids affichés. Le mode `--check` permet de contrôler
   une photo existante sans la recompresser.
2. Référencer la photo dans les fiches concernées, puis dans les index ou le
   README si pertinent. Suivre les conventions de
   [site-jekyll](../site-jekyll/SKILL.md#liens-et-images).
3. Vérifier le diff avant `git add` : seules les photos sélectionnées et leurs
   références doivent être concernées. Le script reste versionné dans ce
   skill ; les photos et leurs références forment un même changement.
