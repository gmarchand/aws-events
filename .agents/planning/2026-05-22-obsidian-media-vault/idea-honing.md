# Idea Honing

Requirements clarification through iterative Q&A.

## Q1: Scope des catégories

Le `playlists.yaml` contient des catégories variées : `media-symposium`, `reinvent-2025/2024/2023/2021`, `reinforce-2024`, `summit-paris-2024`, `ibc-2024/2023`, `storage-day-2023`, `me-symposium-la-2023`.

Le vault Obsidian doit-il couvrir **toutes** ces catégories, ou uniquement les catégories liées au **média** (media-symposium, ibc, me-symposium-la, media-day) ? Les sessions re:Invent/re:Inforce sont très nombreuses (~1000+ vidéos) — veux-tu les inclure toutes, ou seulement un sous-ensemble (ex: sessions M&E uniquement) ?

**A1:** Deux stratégies d'inclusion :
1. **Playlists 100% média** (media-symposium, IBC, NAB, me-symposium-la, media-day) → inclure toutes les vidéos sans filtre
2. **Autres playlists** (re:Invent, re:Inforce, Summit, storage-day, etc.) → filtrer en inspectant le titre et la description de chaque vidéo pour détecter des sujets avec des clients médias

## Q2: Moteur de résumé AI

Pour générer les résumés des transcripts, quel LLM veux-tu utiliser ?

Options possibles :
- **Amazon Bedrock** (Claude, Nova) — tu as déjà un compte AWS
- **OpenAI API** (GPT-4o)
- **Anthropic API directe** (Claude)
- Autre ?

Et une question liée : le résumé doit-il être généré en **français**, en **anglais**, ou dans la **langue de la vidéo** (certaines sont en français, d'autres en anglais) ?

**A2:** Amazon Bedrock. Résumé dans la langue de la vidéo.

## Q3: Détection des vidéos média dans les playlists génériques

Pour filtrer les vidéos média dans les playlists re:Invent/re:Inforce/etc., quels critères de détection ?

Options :
- **Mots-clés statiques** dans titre/description (ex: "media", "broadcast", "streaming", "OTT", "CDN", "video", "M&E", noms de clients connus comme TF1, Canal+, France TV, Netflix, Disney+, etc.)
- **Classification par LLM** — envoyer titre+description à Bedrock pour décider si c'est média ou non
- **Les deux** — mots-clés d'abord (rapide/gratuit), puis LLM en cas de doute

As-tu une liste de clients médias ou de mots-clés que tu veux cibler en priorité ?

**A3:** Classification par LLM (Bedrock) — envoyer titre+description pour décider si la vidéo est pertinente média ou non.

## Q4: Structure du vault Obsidian

Tu as mentionné "classé par année et par événement". Quelle hiérarchie de dossiers préfères-tu ?

Option A :
```
vault/
├── 2025/
│   ├── reinvent/
│   │   ├── video-titre.md
│   ├── media-symposium/
│   │   ├── video-titre.md
├── 2024/
│   ├── ibc/
│   ├── reinvent/
│   ├── reinforce/
```

Option B :
```
vault/
├── reinvent/
│   ├── 2025/
│   ├── 2024/
│   ├── 2023/
├── media-symposium/
│   ├── 2025/
│   ├── 2024/
├── ibc/
│   ├── 2024/
│   ├── 2023/
```

Option C : Flat avec tags/frontmatter uniquement (pas de sous-dossiers, navigation via Dataview/tags dans Obsidian)

**A4:** Option A — Année d'abord, puis événement en sous-dossier.

## Q5: Champ "Client" dans le frontmatter

Le frontmatter inclut un champ "Client". Comment le déterminer ?

- Extraction automatique par LLM depuis le titre/description/transcript (ex: "TF1", "Canal+", "France Télévisions", "Netflix")
- Si pas de client identifiable (ex: session purement technique AWS sans customer story), que mettre ? `null` / vide / "AWS" ?

Et question liée : le champ Client doit-il être une liste (une vidéo peut mentionner plusieurs clients) ou une valeur unique ?

**A5:** Extraction automatique par LLM. Si pas de client identifiable, on ne met pas le champ (ou liste vide). Le champ est une liste (plusieurs clients possibles par vidéo).

## Q6: Source du transcript

Le script actuel utilise Supadata API pour les transcripts. Alternatives :
- **Supadata** (actuel) — API payante, fiable, gère le rate limiting
- **youtube-transcript-api** (Python, gratuit) — utilisé dans l'ancien script, peut être instable (scraping)
- **Les deux en fallback** — Supadata d'abord, youtube-transcript-api si échec

Quelle stratégie pour les transcripts ?

**A6:** youtube-transcript-api (gratuit) comme source principale.

## Q7: Gestion de l'exécution et idempotence

Le pipeline va traiter potentiellement des centaines de vidéos. Questions pratiques :

- **Idempotence** : si on relance le script, doit-il skip les vidéos déjà traitées (note markdown existante) ou tout régénérer ?
- **Exécution incrémentale** : veux-tu pouvoir ajouter une nouvelle playlist au YAML et ne traiter que les nouvelles vidéos ?
- **Gestion des erreurs** : si un transcript échoue ou si Bedrock rate-limit, on skip la vidéo et on continue, ou on s'arrête ?

**A7:** Idempotent — skip les vidéos déjà traitées. Retry avec exponential backoff sur les erreurs (transcript, Bedrock). Continue le traitement des autres vidéos en cas d'échec persistant.

## Q8: Modèle Bedrock et coût

Pour le résumé AI via Bedrock, quel modèle ?

- **Claude Sonnet 4** — bon rapport qualité/coût, contexte 200K tokens (largement suffisant pour un transcript)
- **Claude Haiku** — moins cher, plus rapide, qualité légèrement inférieure
- **Nova Lite/Micro** — le moins cher, suffisant pour du résumé ?

Considérant qu'un transcript de 1h fait ~15K tokens et qu'il y a potentiellement des centaines de vidéos, le coût est un facteur. Préférence ?

**A8:** Claude Opus 4 via Bedrock. (Note: modèle le plus puissant, coût élevé mais qualité maximale pour les résumés.)

## Q9: Nettoyage du repo

Tu as mentionné "complètement refactorer et correctement ranger". Que fait-on des fichiers existants ?

- Les ~100 fichiers `playlist-*.md` → supprimer ? garder dans un dossier legacy ?
- `package.json` + Node.js → supprimer (obsolète)
- `extract_videos.py`, `find_reinvent_playlists.py`, `feedly_to_markdown.py` → supprimer
- `youtube-playlist-markdown.py` → supprimer
- `decks/` (PDFs re:Invent) → garder dans le vault ? séparer ? supprimer ?
- `my-playlist-reinvent-2023.md`, `my-playlist-reinvent-2022.md` → supprimer ?

En gros : on fait table rase et le repo ne contient plus que le vault + le pipeline, ou on garde un historique ?

**A9:** Réorganisation :
1. `playlist-*.md` → déplacer dans un dossier propre (ex: `playlists/`)
2. `package.json` + Node.js → supprimer
3. `extract_videos.py`, `find_reinvent_playlists.py`, `feedly_to_markdown.py`, `youtube-playlist-markdown.py` → déplacer dans `scripts/` (legacy, pas supprimer)
4. `decks/` → garder tel quel
5. `my-playlist-reinvent-2023.md`, `my-playlist-reinvent-2022.md` → supprimer

## Q10: Interface CLI et workflow d'exécution

Comment veux-tu lancer le pipeline ? Options :

- **Un seul script CLI** avec sous-commandes (comme l'actuel `youtube_extractor.py`) : `python pipeline.py extract --category media-symposium`
- **Taskfile** avec des tasks : `task extract`, `task summarize`, `task build-vault`
- **Les deux** — Taskfile qui orchestre le script Python

Et question liée : le pipeline doit-il tourner en une seule passe (extract → classify → transcript → summarize → write note) ou en étapes séparées qu'on peut relancer indépendamment ?

**A10:** Les deux — Taskfile comme entry point + script Python CLI avec sous-commandes. Pipeline en étapes séparées qu'on peut relancer indépendamment (idempotence).

## Q11: Emplacement du vault Obsidian

Le vault Obsidian généré doit vivre :

- **Dans ce même repo** (ex: `vault/` à la racine) — simple, tout au même endroit
- **Dans un repo séparé** — le pipeline génère les notes et les pousse vers un autre repo
- **Sur un chemin local** configurable — le script écrit les notes où on veut (ex: ton vault Obsidian principal)

Préférence ?

**A11:** Dans ce même repo, dossier `vault/` à la racine.

## Q12: Frontmatter additionnel et features Obsidian

Au-delà des champs mentionnés (Titre, Description, Événement, Année, Client), veux-tu :

- **Tags** dans le frontmatter ? (ex: `tags: [streaming, live, sports]`) — utile pour la navigation Obsidian
- **Liens entre notes** (wikilinks Obsidian) ? Ex: `[[TF1]]` dans le body pour lier vers une note client
- **Un index/MOC** (Map of Content) auto-généré par événement ou par année ?
- **Dataview queries** pré-configurées ? (ex: une note qui liste toutes les vidéos d'un client)

Ou on reste minimaliste : frontmatter de base + résumé + URL, et tu enrichis manuellement après ?

**A12:** Tout inclure :
- Tags auto-générés par LLM dans le frontmatter
- Wikilinks Obsidian vers les clients (`[[TF1]]`, `[[Canal+]]`)
- Index/MOC auto-généré par événement et par année
- Dataview queries pré-configurées

## Q13: Gestion des vidéos sans transcript

Certaines vidéos n'auront pas de transcript disponible (vidéo privée, pas de sous-titres, langue non supportée). Que faire ?

- **Exclure** la vidéo du vault (pas de note créée)
- **Créer la note quand même** avec frontmatter + description YouTube mais sans résumé (mention "transcript non disponible")
- **Résumer à partir de la description seule** si elle est suffisamment détaillée

**A13:** Résumer à partir de la description seule si suffisamment détaillée. Sinon créer la note avec frontmatter + mention "transcript non disponible".

## Q14: Pivot architectural — MCP Server

**Décision majeure** : L'architecture change fondamentalement.

**Problème** : On a besoin de 1) migrer l'existant et 2) alimenter le vault quotidiennement.

**Solution** : Créer un **MCP Server "youtube-to-vault"** qui :
- Prend en entrée une vidéo YouTube OU une playlist
- Détecte automatiquement la thématique (sinon demande à l'utilisateur)
- Génère les notes Obsidian dans le vault

**Structure vault révisée** : `thematic → year → playlist → notes`
```
vault/
├── media/
│   ├── 2024/
│   │   ├── ibc/
│   │   │   ├── _index.md
│   │   │   ├── video-slug.md
│   │   ├── reinvent/
│   │   │   ├── _index.md
│   │   │   ├── video-slug.md
├── ai/
│   ├── 2024/
│   │   ├── reinvent/
```

**Deux composants** :
1. **MCP Server** (`youtube-to-vault`) — outil réutilisable, utilisable depuis n'importe quel client MCP (Claude Desktop, Kiro, etc.) pour ajouter des vidéos au vault au quotidien
2. **Script de migration** — utilise le MCP/API pour initialiser le vault avec l'existant (playlists.yaml, focus média)

**A14:** Confirmé par l'utilisateur.

## Q15: MCP Server — Résumé AI intégré

**A15:** Le MCP Server gère tout le pipeline en interne : extraction metadata → transcript → résumé Bedrock → écriture note. C'est un outil autonome.

## Q16: MCP Server — Interaction avec l'utilisateur

Quand le MCP ne peut pas détecter la thématique automatiquement, il "demande". En MCP, ça se traduit comment ?

Options :
- **Retourner un résultat avec `isError: false`** mais un message demandant la thématique, et l'utilisateur relance avec le paramètre `thematic` explicite
- **Paramètre optionnel `thematic`** — si fourni, pas de détection ; si absent, le MCP tente la détection et échoue proprement si impossible
- **Le MCP propose des thématiques candidates** dans sa réponse et l'utilisateur confirme au prochain appel

Et question liée : le vault path doit-il être configurable (paramètre du server) ou hardcodé à `vault/` dans le repo ?

**A16:** Paramètre `thematic` optionnel — si absent, détection auto ; si détection échoue, retourne les candidates pour que l'agent client relance. Vault path configurable (paramètre du server).

## Q17: MCP Server — Technologie

Pour le MCP Server Python, quel SDK/framework ?

- **mcp** (SDK officiel Python MCP) — `pip install mcp`
- **FastMCP** — wrapper simplifié au-dessus du SDK officiel

Et : le MCP Server tourne en mode **stdio** (lancé par le client MCP) ou **SSE/HTTP** (serveur persistant) ?

**A17:** FastMCP, mode stdio.

## Q18: Script de migration — Scope

Le script de migration initialise le vault à partir de l'existant. Clarifications :

1. **Source** : il lit `playlists.yaml` et traite les playlists listées ?
2. **Filtre** : pour les playlists 100% média (media-symposium, IBC, etc.) → tout prendre. Pour les autres (re:Invent, etc.) → classification LLM. Correct ?
3. **Implémentation** : le script de migration appelle-t-il directement les mêmes fonctions internes que le MCP Server (code partagé), ou il invoque le MCP Server comme client ?

**A18:**
1. Oui, source = `playlists.yaml`
2. Playlists NAB/IBC/Symposium/Media Day → tout prendre. Autres playlists → regarder les titres pour détecter un client média (classification LLM).
3. (En attente)

## Q19: Architecture code — partage MCP / migration

Le script de migration et le MCP Server partagent la même logique (fetch metadata, transcript, résumé, écriture note). Comment structurer ?

- **Bibliothèque partagée** : un package Python `core/` avec la logique métier, importé par le MCP Server ET le script de migration
- **Le script de migration est un client MCP** qui invoque le serveur via stdio (plus complexe, mais teste le MCP end-to-end)

Je recommande la bibliothèque partagée — plus simple, testable, et le MCP Server n'est qu'un thin wrapper autour du core.

**A19:** Bibliothèque partagée `core/`. Le script de migration appelle directement les fonctions Python du core (même code que le MCP Server utilise). Le MCP Server est un thin wrapper FastMCP autour du core.

