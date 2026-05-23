---
clients:
- AWS
date: 2022-08-02
description: Retour d'expérience pour la production d'évenements broadcast live sur
  le cloud AWS
event: aws-france-media-day-2022
has_transcript: true
language: fr
playlist: AWS France Media Day 2022
tags:
- live
- cloud
- sport
- broadcast
- aws
- production
thematic: media
title: Production de “Live” dans le Cloud - Sport et Broadcast
url: https://www.youtube.com/watch?v=0_qY47GAjGk
video_id: 0_qY47GAjGk
year: 2022
---

# Production de “Live” dans le Cloud - Sport et Broadcast

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=0_qY47GAjGk)
> 📅 2022-08-02 | 🎤 aws-france-media-day-2022 | 🌐 fr
> 🏢 Clients: [[AWS]]

# Production de « Live » dans le Cloud : Sport et Broadcast

## Contexte et enjeux de la production live cloud

La production d'événements broadcast en direct, notamment dans le domaine sportif, connaît une transformation profonde grâce aux infrastructures cloud. Cette session présente un retour d'expérience concret sur l'utilisation d'AWS pour produire des événements live à grande échelle, en mettant en lumière les bénéfices opérationnels, les défis techniques rencontrés et les solutions mises en œuvre pour répondre aux exigences strictes du secteur audiovisuel.

Le passage au cloud répond à plusieurs problématiques majeures du broadcast traditionnel : la lourdeur logistique des cars-régie, les coûts élevés de déploiement sur site, le manque de flexibilité face à des calendriers d'événements fluctuants, et la difficulté à mobiliser des équipes dispersées géographiquement. Les diffuseurs sportifs, en particulier, recherchent des solutions permettant de couvrir davantage de compétitions tout en maîtrisant leurs investissements.

## Architecture technique et services AWS mobilisés

### Chaîne de production de bout en bout

L'architecture présentée s'appuie sur une chaîne complète de services AWS Media Services. La captation des flux sur site est acheminée vers le cloud via des protocoles de contribution sécurisés et fiables comme SRT ou Zixi, garantissant une transmission de qualité broadcast malgré les contraintes des réseaux publics. Une fois dans le cloud, les flux sont ingérés, traités et mixés à l'aide de services comme AWS Elemental MediaLive pour l'encodage en direct, MediaConnect pour le transport sécurisé, et MediaPackage pour la préparation des flux destinés à la distribution multi-écrans.

La régie virtuelle constitue le cœur du dispositif : elle permet aux opérateurs — réalisateurs, mixeurs, monteurs — de travailler à distance via des interfaces web ou des stations virtualisées sur EC2, en accédant aux mêmes flux et outils qu'en régie physique. Cette désagrégation des fonctions de production ouvre la voie à des modèles collaboratifs où les talents techniques peuvent intervenir depuis n'importe quel site, sans déplacement.

### Latence, qualité et fiabilité

La maîtrise de la latence représente l'un des défis centraux de cette approche. Les architectures déployées visent à maintenir des délais bout-en-bout compatibles avec les exigences du live, notamment pour les retours studio, les commentaires et les interactions avec le public. Des mécanismes de redondance multi-AZ et multi-régions assurent la continuité de service, élément non négociable lors d'événements à forte audience.

## Bénéfices, retours d'expérience et perspectives

Les retours opérationnels confirment plusieurs gains tangibles. La scalabilité à la demande permet d'absorber des pics d'activité lors de saisons sportives chargées sans surdimensionner les infrastructures en permanence. Le modèle économique à l'usage transforme des CAPEX importants en OPEX maîtrisés, rendant accessibles des productions auparavant réservées aux plus grandes compétitions. La flexibilité géographique des équipes améliore la qualité de vie des collaborateurs tout en élargissant le vivier de talents disponibles.

Plusieurs points de vigilance ont néanmoins été identifiés : la nécessité d'une connectivité robuste entre les sites de captation et le cloud, la formation des équipes traditionnelles aux nouveaux outils, et l'importance d'une conception minutieuse des workflows pour éviter toute interruption en direct. La conduite du changement auprès des équipes broadcast historiques constitue un facteur clé de succès, au même titre que la maîtrise technique.

À terme, les intervenants soulignent que la production cloud n'est plus une expérimentation mais devient un standard opérationnel pour de nombreux diffuseurs. Les évolutions à venir porteront sur l'intégration de l'intelligence artificielle pour l'automatisation de la production (détection d'événements, génération de highlights, sous-titrage), la baisse continue des latences et l'enrichissement des expériences interactives pour les spectateurs.