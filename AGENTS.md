Ce projet contient des mélanges de farines et des recettes de boulangerie et de patisserie sans gluten.

## Objectifs

Par orde de priorité décroissante

* goût agréable, doux mais riche, subtil
* texture, consistance, légèreté, aération
* augmenter les taux de protéines pour
  * obtenir un indice glycémique (IG) modéré, en prévention du diabète de type 2
  * soutenir la pratique d'une activité physique régulière
* limiter les graisses saturées, en prévention du cholesterol
* prix contenu

## Analyse nutritionelle pour 100g

Chaque recette doit être accompagnée d'une analyse nutritionelle, à mettre à jour lors de changements d'ingrédients.

## Workflow

N'hesite pas à éditer directement les fichiers, en créer de nouveaux.
Corrige systématiquement sans demander les erreurs évidentes, les erreurs de calcul et oublis de mise à jour.
Met à jour les analyse nutritionnelles automatiquement.
Effectue systématiquement le commit à ma place immédiatement, en gardant un message court.

## Site Jekyll et navigation (`nav_order`)

Site [Jekyll](https://jekyllrb.com/) + thème
[Just the Docs](https://just-the-docs.com/), déployé sur GitHub Pages via
[`.github/workflows/pages.yml`](.github/workflows/pages.yml) (push sur
`main`). La barre latérale est entièrement pilotée par le front matter YAML
de chaque `.md`.

### Front matter d'une recette

```yaml
---
title: Crêpes sans gluten
parent: Pâtisserie
nav_order: 10
---
```

* `title` : libellé affiché dans la sidebar et la recherche.
* `parent` : `title` exact (accents et espaces compris) de l'`index.md` de la
  section : `Pâtisserie`, `Pain`, `Levain`, `Pâtes à tartiner`, `Notes`.
* `nav_order` : entier ordonnant la recette **à l'intérieur de sa section**.

Les `index.md` de section utilisent un autre front matter
(`layout: default`, `has_children: true`, `permalink: /Section/`), ne pas le
recopier dans une recette.

### Règle d'or : `nav_order` unique par section

Deux recettes d'une même section avec le même `nav_order` → ordre arbitraire
dans la sidebar, **sans erreur de build** (piège silencieux). À chaque ajout
ou réorganisation, dans chaque section touchée :

1. Lister les `nav_order` déjà pris (remplacer `Patisserie` par la section
   concernée, idem ci-dessous) :

   ```powershell
   Select-String -Path Patisserie\*.md -Pattern 'nav_order:' |
     ForEach-Object { "{0,-50} {1}" -f $_.Filename, $_.Line.Trim() } |
     Sort-Object
   ```

2. Choisir un entier libre à la position logique voulue. Si on insère au
   milieu, **renuméroter** les suivants (pas de trou, pas de doublon).

3. Vérifier l'absence de doublon (sortie attendue : vide) :

   ```powershell
   Select-String -Path Patisserie\*.md -Pattern 'nav_order:' |
     ForEach-Object { ($_.Line -replace '.*nav_order:\s*','').Trim() } |
     Group-Object | Where-Object Count -gt 1
   ```

4. Mettre à jour la liste « Recettes disponibles » de l'`index.md` de la
   section dans le **même ordre** que les `nav_order`. Si pertinent,
   référencer aussi depuis l'`index.md` racine et/ou le `README.md`.

### Liens internes et `baseurl`

* Entre recettes : chemin Markdown relatif,
  ex. `[Mix farines](MixFarinesPatisserieSansGluten.md)`.
* Depuis l'`index.md` racine (page « home » Jekyll) et pour **toutes** les
  images : `{{ '/chemin' | relative_url }}` pour respecter le `baseurl`
  GitHub Pages.

## Photos d'illustration

Photos stockées dans `Photos/` à la racine, référencées par les recettes,
l'`index.md` racine et le `README.md`.

### Toujours redimensionner avant `git add`

Pour garder le repo léger (cible `.git/` autour de quelques MB), **toute
nouvelle photo doit être redimensionnée et recompressée avant commit**. Ne
jamais commiter un JPEG brut de smartphone (typiquement 3-4 MB, 4000×3000 px).

Paramètres standards (ne pas modifier sans raison) :

* côté le plus long max : **1600 px**
* qualité JPEG : **85**, `progressive=True`, `optimize=True`
* `ImageOps.exif_transpose` puis strip EXIF (figer l'orientation, ne pas
  publier les coordonnées GPS)

Cible : ~250-500 KB par photo. **Signaler** toute photo > 1 MB après
traitement.

### Script `resize_photos.py`

`python` (≥ 3.12) et `Pillow` (≥ 12) sont installés au niveau système (pas de
venv ni de `pip install`), vérifiable avec :

```powershell
python -c "from PIL import Image; print('Pillow', Image.__version__)"
```

Recréer le script à la racine, l'exécuter, puis **le supprimer** (ne pas le
commiter) :

```python
from pathlib import Path
from PIL import Image, ImageOps

MAX_SIDE = 1600
JPEG_QUALITY = 85
PHOTOS_DIR = Path(__file__).parent / "Photos"

for jpg in sorted(PHOTOS_DIR.glob("*.jpg")):
    before = jpg.stat().st_size
    with Image.open(jpg) as img:
        img = ImageOps.exif_transpose(img)
        img.thumbnail((MAX_SIDE, MAX_SIDE), Image.Resampling.LANCZOS)
        img.convert("RGB").save(
            jpg, format="JPEG",
            quality=JPEG_QUALITY, optimize=True, progressive=True,
        )
    after = jpg.stat().st_size
    print(f"{jpg.name:<60} {before/1024:>6.0f} Ko -> {after/1024:>6.0f} Ko")
```

Si une seule photo est nouvelle, restreindre la boucle à ce fichier
(traitement idempotent mais perd un peu de qualité à chaque passe).

### Workflow d'ajout d'une nouvelle photo

1. L'utilisateur dépose le JPEG brut dans `Photos/`.
2. Exécuter `resize_photos.py` (ciblé sur le nouveau fichier).
3. Vérifier le poids final :

   ```powershell
   Get-ChildItem Photos\*.jpg | Sort-Object Length -Descending |
     Select-Object -First 5 Name, @{N='KB';E={[int]($_.Length/1KB)}}
   ```

4. Référencer la photo dans la/les recette(s) concernée(s), et selon le cas
   dans l'`index.md` racine et/ou le `README.md`. Chemins :
   * depuis une sous-section (`Pain/`, `Patisserie/`, …) : `../Photos/NOM.jpg`
   * depuis le `README.md` (racine) : `Photos/NOM.jpg`
   * depuis l'`index.md` racine (Jekyll) :
     `{{ '/Photos/NOM.jpg' | relative_url }}` (cf. section Jekyll).

5. Supprimer `resize_photos.py` puis commiter (photos + références `.md`).

### Si une photo lourde a déjà été commitée par erreur

Un commit correctif ne suffit pas : le blob lourd reste dans l'historique
git. Procéder à une réécriture d'historique (reset + cherry-pick), puis
`git gc --prune=now --aggressive`, et prévenir l'utilisateur qu'il faudra
force-pusher (`git push --force-with-lease`).