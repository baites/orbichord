# orbichord

Orbichord is a tool to explore the n-pitch quotient spaces (orbifolds) of music.

The inspiration for this tool is from the following references:

* Callender, Clifton, Ian Quinn, and Dmitri Tymoczko. "Generalized voice-leading spaces." Science 320.5874 (2008): 346-348.
* A Dmitri Tymoczko. Geometry of Music: Harmony and Counterpoint in the Extended Common Practice. Oxford Studies in Music Theory. Oxford University Press, 2010. ISBN	0199714355, 9780199714353.

# Installation

* Cloning and creating docker image

**NOTE**: This installation requires installed docker server.

```bash
$ mkdir orbichord
$ cd orbichord
$ git clone https://github.com/orbichord/documentation.git
$ git clone https://github.com/orbichord/orbichord.git
$ docker build -t orbichord -f orbichord.dockerfile .
...
Successfully tagged orbichord:latest
```

* Creating container

```bash
$ USER_ID=$(id -u)
$ USER_NAME=$(id -un)
$ GROUP_ID=$(id -g)
$ GROUP_NAME=$(id -gn)
$ docker create \
--name orbichord-$USER_NAME \
--mount type=bind,source=$PWD,target=/home/$USER_NAME/orbichord \
--mount type=bind,source=$HOME/.ssh,target=/home/$USER_NAME/.ssh \
--workdir /home/$USER_NAME/orbichord \
-t -p 8888:8888 orbichord
$ docker start orbichord-$USER_NAME
```

* Mirror user and group to the container

```bash
$ CMD="useradd -u $USER_ID -N $USER_NAME && \
groupadd -g $GROUP_ID $GROUP_NAME && \
usermod -g $GROUP_NAME $USER_NAME &&\
echo '$USER_NAME ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/$USER_NAME &&\
chown -R $USER_NAME:$GROUP_NAME /home/$USER_NAME"
docker exec orbichord-$USER_NAME /bin/bash -c "$CMD"
```

* Entering in the container install orbichord

```bash
$ docker exec -it -u $USER_NAME orbichord-$USER_NAME /bin/bash
$USER_NAME@bcfa7ea7eb52 orbichord$ sudo pip install orbichord
...
$USER_NAME@bcfa7ea7eb52 orbichord$ jupyter lap --ip 0.0.0.0
...
```
* Open *browser* in the localhost url.

* Examples:
  * Pure python examples in orbichord/example directory.
  * Jupyter notebook examples in documentation/source/user_guide directory.

# Generating documentation

**Note**: I this step assumes previous steps were executed.

```bash
$USER_NAME@bcfa7ea7eb52 orbichord$ cd documentation
$USER_NAME@bcfa7ea7eb52 documentation$ make html
```