---
clients:
- Canal+
- AWS
- Groupe CANAL+
- Amazon EC2
date: 2024-11-13
description: "Canal+ nous présente leur nouvelle plateforme d'encodage de fichiers
  média, qui leur permet de traiter très rapidement des milliers d'heures de contenus,
  tout en bénéficiant de la scalabilité et du faible coût de l'infrastructure Amazon
  EC2 Spot.\n\nIntervenants : Kevin Saliou, Lead Software Development Engineer, Groupe
  CANAL+ - Lionel Gattegno, Senior Solutions Architect Media & Entertainment, Games
  and Sports, AWS.\n\nEn savoir plus sur AWS pour le multimédia et le divertissement
  \U0001F449 https://aws.ama"
event: aws-media-entertainment-symposium-paris
has_transcript: true
language: fr
playlist: AWS Media & Entertainment Symposium Paris
tags:
- transcoding
- encoding
- cloud
- aws
- ec2-spot
- media-processing
- scalability
thematic: media
title: AWS Symposium Media France - Le transcodage pour la distribution de contenu
  par Canal +
url: https://www.youtube.com/watch?v=0-52LCANzW8
video_id: 0-52LCANzW8
year: 2024
---

# AWS Symposium Media France - Le transcodage pour la distribution de contenu par Canal +

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=0-52LCANzW8)
> 📅 2024-11-13 | 🎤 aws-media-entertainment-symposium-paris | 🌐 fr
> 🏢 Clients: [[Canal+]] [[AWS]] [[Groupe CANAL+]] [[Amazon EC2]]

# Le transcodage pour la distribution de contenu par Canal+

## Contexte et enjeux de la plateforme d'encodage

Lors de l'AWS Symposium Media France, Kevin Saliou, Lead Software Development Engineer chez le Groupe Canal+, accompagné de Lionel Gattegno, Senior Solutions Architect Media & Entertainment chez AWS, a présenté la nouvelle plateforme d'encodage de fichiers média développée par Canal+. Cette plateforme répond à un besoin critique du diffuseur : traiter des volumes considérables de contenus audiovisuels — plusieurs milliers d'heures — dans des délais très courts pour alimenter les différents canaux de distribution du groupe. La problématique centrale consistait à concilier puissance de calcul massive, agilité opérationnelle et maîtrise des coûts, dans un secteur où les pics de charge liés aux nouvelles productions, aux acquisitions de catalogues ou aux événements sportifs imposent une infrastructure capable de monter en charge rapidement.

## Architecture technique et choix d'infrastructure

### Exploitation d'Amazon EC2 Spot pour la scalabilité

Le cœur de la solution repose sur l'utilisation intensive des instances Amazon EC2 Spot, qui permettent à Canal+ de mobiliser des capacités de calcul considérables tout en réduisant drastiquement les coûts par rapport aux instances à la demande. Cette approche s'avère particulièrement adaptée aux charges de travail de transcodage, qui sont parallélisables et tolérantes aux interruptions lorsqu'elles sont correctement orchestrées. La plateforme tire ainsi parti de l'élasticité du cloud AWS pour absorber les pics de production sans surdimensionner l'infrastructure en période creuse.

### Orchestration et résilience des traitements

La plateforme a été conçue pour gérer la nature volatile des instances Spot, en découpant les tâches d'encodage en unités de travail capables de reprendre leur exécution en cas d'interruption. Cette architecture garantit que des milliers d'heures de contenu peuvent être traitées en parallèle, en distribuant la charge sur un parc d'instances dynamique. L'objectif est d'atteindre des temps de traitement très courts, indispensables pour respecter les fenêtres de diffusion et les exigences éditoriales du groupe.

## Bénéfices opérationnels et perspectives

### Gains en performance et en coûts

Grâce à cette nouvelle plateforme, Canal+ bénéficie d'une capacité de transcodage à la fois rapide et économiquement optimisée. La combinaison de la scalabilité quasi illimitée d'EC2 et du tarif réduit des instances Spot permet de soutenir les ambitions du groupe en matière de distribution multicanale, qu'il s'agisse de la télévision linéaire, des plateformes de streaming ou des services à la demande. Cette agilité technique se traduit par une meilleure réactivité face aux besoins métiers et par une réduction significative des coûts d'infrastructure.

### Vers une distribution de contenu modernisée

Cette transformation illustre la stratégie cloud du Groupe Canal+ pour moderniser sa chaîne de production audiovisuelle. En s'appuyant sur les briques managées et les modèles de consommation flexibles d'AWS, Canal+ se positionne pour répondre aux évolutions rapides des usages et des formats dans l'industrie médiatique, tout en conservant la maîtrise opérationnelle nécessaire à la qualité de service attendue par ses abonnés.