
# Mars One <img src="http://www.lasdepique.fr/mars-one/noun_269594_cc-cut.png" width="100" align="center">

Robot avec caméra embarquée piloté à distance via une manette et rendu dans un casque de réalité virtuelle.

[![Prototype Mars One](http://www.lasdepique.fr/mars-one/IMG_6432-compressee.jpg)](http://www.lasdepique.fr/mars-one/IMG_6432-compressee.jpg)

## Objectif

Reproduire l'experience de pilotage d'un rover sur Mars. Le rover doit être placé dans un environnement ressemblant au sol martien. La vidéo transmise par le rover est traitée avec un filtre rouge/orangé pour donner l'impression de l'atmosphère martienne.

Projet réalisé en 24 heures par 4 personnes dans le cadre du hackathon [fHacktory](http://www.fhacktory.com/).

## Présentation de la team

Paul & Gabriel : team Rover

Conception et production du hardware et de l’interface homme machine de déplacement haute précision.

Mission : assurer la mobilité du rover à tout épreuve via une interface ayant fait le fruit de plusieurs années de R&D (steam contrôleur)

Thomas & Yann : team Virtual Reality

Echantillonnage graphique 360 degrés de l’environnement martien et restitution en réalité augmentée ultra haute définition.

Mission : permettre un retour visuel de l’environnement du rover, récupérer les premières preuves de vie intelligente sur la planète rouge.

## Sources :
Lego model : conception hardware du rover
Mars-One-Camera : sources de l’application permettant la prise de photo depuis le smartphone sur le rover
Mode module : sources de l’interface rover (lego) steam contrôleur.

## Genèse du projet :
Inspiré par le robot Beam, le projet Mars One s’adresse aux enfants rêveur avec un peu d’imagination parfois bloqué sur un lit d’hôpital.
On voit souvent Beam dans des musées. On aimerait que ces gamins puissent visiter Mars avec la même techno un peu hackée.

## Roadmap du projet :
Brainstorm, répartition des charges et constitution des deux teams de binômes (rover et VR).

### Road map team rover
- Conception du hardware à partir de plan lego officiel
- Hack pour permettre le support d’un smartphone sur le rover
- Premiers tests sur le sol terrien : Robot agile et rapide, mobilité réduite en milieu accidenté
- Hack pour monter des chenilles tout terrain plus grosses
- Tests de la version 2 des chenilles : Capacité de franchissement accrue au détriment de la maniabilité du rover et requière beaucoup plus d’énergie. Les moteurs légo atteignent leur limite en terme de couple. Décision de retourner à la V1 des chenilles.
- En parallèle, établissement une connexion basic avec les legos. Linux sur le boitier EV3
- Premières requêtes de déplacement
- Interfaçage avec le clavier de l’ordinateur du client
- Conception du détecteur de proximité à l’avant du rover.
- Intefaçage avec le steam contrôleur

### Road map team VR
- Conception en parallèle de deux applications : l’une destinée au smartphone embarqué sur le rover, l’autre embarqué dans le cardboard
- Simulation de l’environnement martien avec filtre rouge-orangé, faux sol et faux ciel pour masquer les zones d’ombres de la lentille BubbleScope. Affichage de métriques et jauges, sur l’interface pour ajouter un petit côté un peu hi-tech
- Essais avec Cordova pour la récupération du flux vidéo du smartphone (getUserMedia pas supporté sur iOS, usage de polyfil).
- On a jamais réussi à builder l’app avec les les polyfil pour cordova
- Après brainstorm on a décidé de passer les deux applications sur Unity
- Récupération de la vidéo via webcamTexture
- Essai d’envoi des images sur le réseau
- Unity n’est finalement pas fait pour streamer autant de data
- Reception d’insulte de la part de unity rapport au point de nos data et le nombre de requêtes par seconde
- Découpage de nos images en tuiles de la taille maximale supportée par unity
- Ajustement du nombre d’envoi de tuiles par secondes
- Constatation que pour avoir un rendu fluide on doit avoir une image beaucoup trop dégradée
- Finalement, envoi image par image vers un serveur node et réception côté VR une fois par seconde (on va mettre ça sur le compte de la latence entre Mars et la Terre)
- Application de la texture « donut » fournie par la lentille BubbleScope sur une sphère dans unity pour essayer de retrouver la vue 360
- Test avec un fisheye à la place du BubbleScope

## Technologies utilisées Rover :
Lego Mindstorm EV3
Linux embarqué sur le module EV3
Python pour les échanges entre EV3 et interface homme machine
Bash pour lancer et fermer proprement le programme gérant les IO EV3 / interface homme machine
Steam controller pour l’interface homme machine.

## Technologies utilisées VR :
BubbleScope, lentille permettant la prise de photo et video à 360 degrés
ou Lentille Fisheye pour iPhone à la place du BubbleScope pour avoir une image moins large mais de meilleur qualité
Unity webcamTexture pour la prise de photo
Unity pour le rendu VR
NodeJS pour l’échange de données entre smartphone embarqué sur le rover et celui embarqué dans le casque VR
deux iPhone embarqué sur le Rover et dans le casque VR
Equivalent Cardboard pour le casque de réalité virtuelle

## Next steps :
Gérer le streaming entre les deux téléphones via une solution swift adaptée pour avoir une meilleur vitesse de transfert, meilleur qualité d’image  (unity et cordova n’étants pas prévu pour ça ou basé sur des polyfil encore mal supportés).
Amélioration de la stabilité du smartphone embarqué sur le Rover.
Création d’une commande spéciale pour le Rover : retour à la base.
Et tellement plein d’autres trucs…

## Bonus :
3 parties Forza en écran splité dont une de 3 tours sur un circuit japonais de plus de 13 Km/tour : 30 minutes de jeu.
130,680 Sextillions de cookies cuisinés sur CookieClicker

## Crédits images
<img src="http://www.lasdepique.fr/mars-one/noun_269594_cc.png" width="300">
