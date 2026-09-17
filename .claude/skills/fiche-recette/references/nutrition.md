# Référence nutritionnelle interne

## Utilisation

Charger les lignes nécessaires au calcul, pas une base entière. Cette table
contient des valeurs réutilisables ; les URL servent à leur traçabilité et à
leur mise à jour, sans devoir rouvrir la source à chaque utilisation.
Privilégier l'étiquette du produit exact lorsqu'elle est disponible ; sinon
utiliser l'aliment générique correspondant et expliciter une assimilation.
Une purée d'oléagineux n'est pas automatiquement identique au fruit entier,
et une farine de riz complète n'est pas interchangeable avec toute farine de riz.

Pour ajouter une donnée : conserver le nom exact du produit ou le code aliment,
l'état, la base (100 g ou 100 mL), les huit valeurs du tableau, la source
(étiquette ou URL avec identifiant/version), la date de consultation et les
éventuelles approximations. Une valeur inconnue reste `—`, jamais zéro.
Conserver les mentions `traces` et `<` de la source ; documenter la valeur
retenue pour le calcul si nécessaire. Distinguer sucres et glucides, sel et
sodium ; si seul le sodium est disponible, sel = sodium × 2,5 dans la même unité.

## Extrait Ciqual vérifié

Source : Anses, **Table de composition nutritionnelle des aliments Ciqual 2025**,
Du Chaffaut, Oseredczuk et Gauvreau-Béziat, Recherche Data Gouv, V1,
[DOI 10.57745/RDMHWY](https://doi.org/10.57745/RDMHWY).
Extrait consulté le **6 septembre 2026**, fichiers `alim_2025_11_03.xml`,
`compo_2025_11_03.xml` et `const_2025_11_03.xml` (identifiants de fichiers
666252, 666249 et 666246). Réutilisation sous Licence Ouverte Etalab 2.0.

Valeurs pour **100 g de partie comestible** : énergie en kcal, autres colonnes
en g. Noms et teneurs conservés tels que publiés. Constituants Ciqual :
328 (énergie UE), 40000 (lipides), 40302 (AGS), 31000 (glucides), 32000 (sucres),
34100 (fibres), 25003 (protéines N × 6,25), 10004 (sel).
Le signe `-` de Ciqual désigne une donnée manquante ; il est conservé.
Les cellules vides sont représentées par `—`. Aucun des deux ne vaut zéro.

| Code | Aliment | kcal | Lipides | AGS | Glucides | Sucres | Fibres | Protéines | Sel |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 4090 | Fécule de pomme de terre | 348 | 0,2 | 0,039 | 86,3 | - | 0,55 | 0 | 0,0094 |
| 9510 | Amidon de maïs ou fécule de maïs | 365 | 0,05 | 0,009 | 90,4 | 0 | 0,9 | 0,26 | 0,023 |
| 9520 | Farine de riz | 357 | 2,5 | 0,46 | 73,9 | 0,9 | 3,3 | 8 | < 0,13 |
| 9540 | Farine de sarrasin | 348 | 2,19 | 0,58 | 68,4 | 0,03 | 4,2 | 11,5 | 0,06 |
| 9545 | Farine de maïs | 362 | 1,39 | 0,17 | 80,9 | 0,64 | 1,9 | 5,59 | 0,0025 |
| 9555 | Farine de millet | 350 | 4,1 | 0,76 | 63,2 | 0,5 | 9,7 | 10,2 | < 0,13 |
| 9570 | Farine de châtaigne | 362 | 3,43 | 0,52 | 70,4 | - | 12,6 | 6,1 | - |
| 9580 | Farine de pois chiche | 359 | 6,69 | 0,69 | 47 | 10,9 | 10,8 | 22,4 | 0,16 |
| 11017 | Sel blanc alimentaire, non iodé, non fluoré (marin, ignigène ou gemme) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 97,8 |
| 11060 | Herbes de Provence, séchées | 283 | 7,2 | 1,88 | 23,1 | - | 40,1 | 11,5 | 0,088 |
| 13005 | Banane, chair sans peau, crue | 87,6 | < 0,5 | < 0,01 | 19,7 | 15,6 | 2,7 | 1,06 | < 0,013 |
| 13008 | Ceriser, chair et peau, sans noyau, crue | 53,7 | < 0,3 | < 0,01 | 13 | 10 | 1,6 | 0,81 | < 0,013 |
| 13011 | Datte, chair et peau, sans noyau, sèche | 287 | 0,25 | 0,075 | 64,7 | 64,7 | 7,3 | 1,81 | 0,098 |
| 13014 | Fraise, crue | 35,1 | < 0,5 | < 0,01 | 6,03 | 5,6 | 3,8 | 0,63 | < 0,013 |
| 13047 | Rhubarbe, tige, crue | 18,1 | 0,16 | 0,041 | 1,12 | 1,1 | 1,8 | 0,73 | 0,0075 |
| 13187 | Purée de pommes, type "compote sans sucres ajoutés", rayon ambiant | 56,4 | 0,28 | 0,082 | 11,6 | 11,6 | 1,7 | 1,13 | < 0,013 |
| 15000 | Amande, avec peau, sans sel ajouté | 615 | 51,3 | 4,11 | 9,51 | 4,2 | 12,5 | 22,6 | < 0,013 |
| 15004 | Noisette, sans sel ajouté | 632 | 56,9 | 4,75 | 7,16 | 4,9 | 11,6 | 17 | < 0,013 |
| 16400 | Beurre à 80% MG minimum, doux | 753 | 83 | 60 | 0,71 | 0,71 | 0 | 0,63 | 0,035 |
| 16402 | Beurre à 80% MG, demi-sel | 725 | 80 | 56,5 | 0,5 | 0,5 | 0 | 0,75 | 1,9 |
| 17130 | Huile de colza | 900 | 100 | 7,26 | 0 | 0 | 0 | 0 | < 0,0028 |
| 17270 | Huile d'olive vierge extra | 899 | 99,9 | 15,2 | traces | 0 | 0 | 0,25 | < 0,013 |
| 18100 | Cacao, sans sucres ajoutés, poudre soluble | 387 | 20,6 | 12,4 | 11,6 | 0,9 | 29,5 | 22,4 | 0,11 |
| 19041 | Lait demi-écrémé, UHT | 47,7 | 1,56 | 0,97 | 5 | 4,96 | 0 | 3,41 | 0,088 |
| 20020 | Courgette, chair et peau, crue | 16,7 | 0,32 | 0,084 | 1,75 | 1,74 | 1 | 1,21 | 0,02 |
| 20034 | Oignon, cru | 39 | 0,62 | 0,2 | 6,25 | 4,8 | 1,7 | 1,1 | 0,098 |
| 20041 | Poivron, vert, jaune ou rouge, cru | 22,6 | 0,27 | 0,071 | 3,5 | 1,5 | 1,5 | 0,8 | 0,021 |
| 20053 | Aubergine, crue | 22,9 | 0,18 | 0,034 | 2,7 | 2,7 | 3 | 0,98 | 0,005 |
| 20385 | Tomate sans précision, crue (aliment moyen) | 19,2 | < 0,5 | < 0,01 | 3,69 | 3,22 | 1,02 | 0,6 | < 0,013 |
| 22000 | Oeuf cru | 140 | 9,83 | 2,64 | 0,06 | 0,06 | 0 | 12,8 | 0,31 |
| 22001 | Oeuf, blanc (blanc d'oeuf), cru | 48,1 | 0,17 | 0 | 0,73 | 0,71 | 0 | 10,9 | 0,42 |
| 22002 | Oeuf, jaune (jaune d'oeuf), cru | 307 | 26,7 | 9,55 | 1,09 | 0,56 | 0 | 15,5 | 0,048 |
| 31016 | Sucre blanc | 399 | 0 | 0 | 99,7 | 99,7 | 0 | 0 | 0,0054 |

## Repères anciens non vérifiés

Ces repères proviennent du dépôt avant cette extraction ; ils ne constituent
pas des étiquettes vérifiées. Employer les données Ciqual ci-dessus lorsqu'elles
correspondent au produit, ou obtenir son étiquette. Ne pas attribuer
rétroactivement les anciens calculs à Ciqual.

* Whey concentrée neutre : environ 365 kcal, 5 g de lipides dont 3 g d'AGS,
  7 g de glucides, 78 g de protéines et 0,3 g de sel pour 100 g. Sucres et
  fibres non renseignés. Origine : `Notes/AugmenterTauxProteines.md`, qui cite
  Décathlon sans étiquette ni date. À vérifier avant un nouveau calcul.
* Conversion usuelle héritée : un œuf sans coquille ≈ 50 g. Utiliser une
  masse fournie lorsqu'elle existe. Pour les liquides, une valeur par 100 mL
  s'applique au volume ; pour passer à une donnée par 100 g, noter la densité
  ou l'approximation choisie dans le calcul, sans conversion implicite.

## Traçabilité des fiches

Pour chaque calcul nouveau ou révisé, ajouter ici une courte entrée par chemin
avec les codes Ciqual/produits utilisés et les choix non visibles dans la fiche.
Ne pas dupliquer les compositions, résultats des mélanges ou analyses finales.

* `Cuisine/Ratatouille.md` : la fiche cite déjà Ciqual 2025 ; oignon 20034,
  aubergine 20053, poivron moyen 20041, courgette 20020, tomate moyenne 20385,
  huile d'olive 17270, herbes de Provence 11060 sont les correspondances
  disponibles dans cet extrait. Les tomates pelées sont assimilées à la tomate
  moyenne. La fiche exclut les sucres non renseignés des herbes. Ces
  correspondances sont documentées ici sans recalcul de la fiche historique.
* `PateATartiner/PateATartinerChocolatNoirAmande.md` : purée d'amandes complètes
  assimilée à l'amande avec peau 15000 ; huile de colza 17130. Les autres
  contributions sont reprises de l'analyse historique de la fiche, faute de
  traçabilité plus précise ; masse finale retenue : 451 g, sans perte.
* Autres fiches : provenance détaillée des calculs historiques non consignée.
  Compléter lors de leur prochaine révision, sans inventer leurs sources.
