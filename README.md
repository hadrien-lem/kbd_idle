# kbd_idle

## Présentation
Petit service en python pour éteindre le rétro-éclairage du clavier de mon ordinateur portable Asus après un certain temps d'inactivité. Il se rallume à la dernière valeur après un mouvement de la souris ou si une touche du clavier est appuyée.

## Installation
### Dépendances
* Python 3
* aiofiles

### Emplacements des fichiers
1. Copier/coller le fichier python où vous voulez
2. Copier/coller le fichier service dans `/etc/systemd/system/`

### Contenu des fichiers
1. `cat /proc/bus/input/devices` pour identifier les différents événements `/dev/input/eventX`
2. Identifier le clavier et éditer le fichier python en conséquence
3. La souris n'est normalement pas à modifier
4. Vérifier que le rétro-éclairage est controlé par le fichier `/sys/class/leds/asus::kbd_backlight/brightness`
5. Modifier ce chemin si besoin
6. Éditer le chemin du fichier python à l'intérieur du fichier service

Testé sur Arch-Gnome Wayland
