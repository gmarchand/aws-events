# Rough Idea

## Context

Le repo `aws-events` centralise des playlists YouTube d'événements AWS (re:Invent, Media Symposium, IBC, Summit Paris, etc.) dans un fichier `playlists.yaml`. Un script Python (`youtube_extractor.py`) extrait les vidéos et génère des fichiers markdown par playlist + des fichiers individuels par vidéo avec transcript.

## Objectif

Refactorer complètement ce repo pour créer un **vault Obsidian** dédié aux vidéos médias, organisé par année et par événement. Chaque vidéo devient une note markdown avec :

### Frontmatter
- Titre
- Description
- Événement
- Année
- Client (si applicable)

### Contenu
- Résumé AI du transcript (pas le transcript brut)
- URL de la vidéo

### Règles du résumé AI
1. Écriture en voix active, phrases complètes, paragraphes fluides organisés par thème. Supprimer tout filler. Ton formel mais engageant. Prose narrative, pas de bullet points.
2. Utiliser Markdown avec 3 niveaux de titres pour organiser les thématiques. Paragraphes développés avec transitions logiques. Les notes doivent être compréhensibles sans avoir vu la vidéo.
3. Focus sur les décisions clés, action items, discussions importantes et résultats. Notes concises et claires tout en maintenant l'information essentielle.
4. Rechercher sur la documentation AWS si besoin de contexte supplémentaire.

## État actuel du repo
- ~100 fichiers `playlist-*.md` (listes de vidéos par playlist)
- `playlists.yaml` : fichier central avec catégories (media-symposium, reinvent-2025, reinvent-2024, etc.)
- `youtube_extractor.py` : script CLI (click) qui extrait playlists, transcripts (via Supadata API), génère markdown/PDF
- `extract_videos.py` : ancien script qui parse les playlist-*.md et extrait les transcripts (via youtube-transcript-api)
- `decks/` : PDFs de présentations re:Invent 2021/2023
- Scripts Node.js obsolètes (package.json)
- Pas de structure vault Obsidian

## Résultat attendu
- Un vault Obsidian propre, navigable, avec des résumés AI de qualité
- Pipeline automatisé : playlist YAML → extraction → transcript → résumé AI → note Obsidian
- Repo nettoyé des fichiers obsolètes
