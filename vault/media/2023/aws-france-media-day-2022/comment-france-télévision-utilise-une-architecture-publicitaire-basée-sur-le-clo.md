---
clients:
- France Télévision
- France TV
- AWS
- France Television
date: 2023-02-07
description: "France TV a mis en place une architecture permettant de remplacer les
  publicités antennes par des publicités numériques (\"ad switching\" ou \"ad replacement\").
  Cette solution permet de garantir la meilleure expérience utilisateur tout en augmentant
  les revenus publicitaires des chaines linéaires, diffusées sur l'offre france.tv.
  Le remplacement de publicité s’opère coté server et repose sur la suite AWS Media
  Services. \n\nGuillaume Postaire : Director, MediaFactory, France Television\nYoann
  Guennegu"
event: aws-france-media-day-2022
has_transcript: true
language: fr
playlist: AWS France Media Day 2022
tags:
- advertising
- cloud
- aws
- streaming
- broadcast
- ad-replacement
- linear-tv
thematic: media
title: Comment France Télévision utilise une architecture publicitaire basée sur le
  cloud AWS
url: https://www.youtube.com/watch?v=84eaXZULXsk
video_id: 84eaXZULXsk
year: 2023
---

# Comment France Télévision utilise une architecture publicitaire basée sur le cloud AWS

> [!info] Video
> 📺 [Watch on YouTube](https://www.youtube.com/watch?v=84eaXZULXsk)
> 📅 2023-02-07 | 🎤 aws-france-media-day-2022 | 🌐 fr
> 🏢 Clients: [[France Télévision]] [[France TV]] [[AWS]] [[France Television]]

# Architecture publicitaire cloud de France Télévisions sur AWS

## Contexte et enjeux du remplacement publicitaire

France Télévisions a déployé une architecture cloud sur AWS afin de moderniser la diffusion publicitaire de ses chaînes linéaires disponibles sur la plateforme france.tv. L'objectif central de ce projet consiste à remplacer dynamiquement les publicités diffusées à l'antenne par des publicités numériques ciblées lors de la consommation en streaming. Cette technique, communément appelée *ad switching* ou *ad replacement*, répond à un double impératif stratégique : améliorer significativement l'expérience des téléspectateurs en ligne tout en augmentant les revenus publicitaires générés par les flux linéaires diffusés sur internet.

L'équipe projet, composée de Guillaume Postaire (Directeur MediaFactory), Yoann Guennegues (Chef de projet OTT) et Fatima Mekkaoui (Chef de projet transverse), a porté cette transformation en s'appuyant sur l'expertise interne de France Télévisions et sur les services managés d'AWS pour répondre aux contraintes spécifiques du média audiovisuel public.

## Architecture technique fondée sur AWS Media Services

### Principe du remplacement côté serveur

Le remplacement publicitaire s'effectue intégralement côté serveur, une approche qui présente plusieurs avantages décisifs par rapport à un remplacement côté client. Cette architecture serveur garantit une homogénéité de traitement quel que soit le terminal utilisé par le téléspectateur, qu'il s'agisse d'un téléviseur connecté, d'un mobile ou d'un navigateur web. Elle assure également une meilleure résistance aux bloqueurs de publicités et offre un contrôle plus fin sur la qualité de l'insertion, évitant les ruptures visuelles ou les latences perceptibles lors des transitions entre contenu éditorial et créations publicitaires.

### Suite AWS Media Services comme socle technologique

L'architecture mise en œuvre repose sur la suite AWS Media Services, qui fournit les briques essentielles à la chaîne de traitement du flux : ingestion du signal antenne, identification des marqueurs publicitaires, substitution dynamique des spots, encodage adaptatif et distribution vers les utilisateurs finaux. Ce choix technologique permet à France Télévisions de bénéficier d'une infrastructure scalable, capable d'absorber les pics d'audience caractéristiques de la diffusion linéaire, tout en maintenant la qualité de service attendue d'un diffuseur public national.

L'utilisation de services managés réduit par ailleurs la charge opérationnelle des équipes techniques et accélère la mise en production de nouvelles fonctionnalités, un atout essentiel dans un marché publicitaire numérique en constante évolution.

## Bénéfices et résultats obtenus

La solution déployée permet à France Télévisions de monétiser plus efficacement ses audiences numériques en proposant aux annonceurs des inventaires publicitaires ciblés et mesurables, là où les publicités antenne traditionnelles ne pouvaient être valorisées de la même manière dans l'environnement OTT. L'expérience utilisateur s'en trouve améliorée grâce à des publicités mieux adaptées au contexte de visionnage en ligne et à une qualité de diffusion préservée.

Cette architecture constitue ainsi un levier stratégique pour l'avenir de la diffusion linéaire sur internet, démontrant comment un acteur du service public audiovisuel peut tirer parti des technologies cloud pour conjuguer modernisation technique, performance économique et qualité de service.