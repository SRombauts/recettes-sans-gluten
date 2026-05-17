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

## Photos d'illustration

Les photos sont stockées dans `Photos/` à la racine et illustrent les recettes
correspondantes ainsi que la page d'accueil (`index.md`) et le `README.md`.

### Toujours redimensionner avant `git add`

Pour garder le repo léger (cible : `.git/` autour de quelques MB), **toute
nouvelle photo doit être redimensionnée et recompressée avant d'être commitée**.
Ne jamais commiter de JPEG brut sortant d'un smartphone (typiquement 3-4 MB,
4000×3000 px).

Paramètres standards (à ne pas modifier sans raison) :

* largeur/hauteur max : **1600 px** (côté le plus long)
* qualité JPEG : **85**
* `progressive=True`, `optimize=True`
* respecter l'orientation EXIF puis la figer dans les pixels
  (`ImageOps.exif_transpose`)
* strip des métadonnées EXIF (gagne quelques Ko et évite de publier des GPS)

Cible de poids : ~250-500 KB par photo. Une photo de plus d'1 MB après
traitement doit être signalée.

### Outils disponibles

* `python` (≥ 3.12) et `Pillow` (≥ 12) sont installés au niveau système, donc
  pas besoin de venv ni de `pip install`. Vérifier avec :

  ```powershell
  python -c "from PIL import Image; print('Pillow', Image.__version__)"
  ```

### Script de référence

À recréer à la racine sous le nom `resize_photos.py` puis à supprimer après
usage (ne pas commiter le script) :

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

Si seule une photo est nouvelle, restreindre la boucle au fichier concerné
plutôt que de re-traiter l'ensemble (le traitement est idempotent mais perd
un peu de qualité à chaque passe).

### Workflow d'ajout d'une nouvelle photo

1. L'utilisateur dépose le JPEG brut dans `Photos/`.
2. Exécuter le script ci-dessus (ou son équivalent ciblé).
3. Vérifier le poids final (commande PowerShell) :

   ```powershell
   Get-ChildItem Photos\*.jpg | Sort-Object Length -Descending |
     Select-Object -First 5 Name, @{N='KB';E={[int]($_.Length/1KB)}}
   ```

4. Référencer la photo dans la/les recette(s) concernée(s) et éventuellement
   dans `index.md` / `README.md`. Chemins :
   * depuis la racine : `Photos/NOM.jpg`
   * depuis une sous-section (Pain, Patisserie, Levain…) : `../Photos/NOM.jpg`
   * dans `index.md` (Jekyll, pour passer par `baseurl`) :
     `{{ '/Photos/NOM.jpg' | relative_url }}`
5. Supprimer `resize_photos.py` puis commiter (photos + références `.md`).

### Si une photo lourde a déjà été commitée par erreur

Ne pas se contenter d'un commit correctif : les blobs lourds resteraient dans
l'historique git. Procéder à une réécriture d'historique (reset + cherry-pick),
faire un `git gc --prune=now --aggressive`, puis prévenir l'utilisateur qu'il
faudra force-pusher (`git push --force-with-lease`).