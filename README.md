# orbichord

Orbichord is a tool to explore the n-pitch quotient spaces (orbifolds) of music.

The inspiration for this tool is from the following references:

* Callender, Clifton, Ian Quinn, and Dmitri Tymoczko. "Generalized voice-leading spaces." Science 320.5874 (2008): 346-348.
* A Dmitri Tymoczko. Geometry of Music: Harmony and Counterpoint in the Extended Common Practice. Oxford Studies in Music Theory. Oxford University Press, 2010. ISBN	0199714355, 9780199714353.

# Installation

```bash
$ mkvirtualenv orbichord
(orbichord)$ git clone https://github.com/orbichord/orbichord.git
(orbichord)$ pip install -U .
```

# Integration with holoviews and jupyter notebooks

* Install jupyter

```bash
$ sudo pacman -S jupyterlab
$ sudo jupyter labextension install @pyviz/jupyterlab_pyviz
```

* Enable ipykernel in virtualenv orbichord

```bash
$ workon orbichord
(orbichord)$ pip install ipykernel
(orbichord)$ python -m ipykernel install --user --name=orbichord
```

* Check ipykernel in virtualenv

```bash
$ jupyter kernelspec list
```

* ONLY IF YOU HAVE TO: how to remove a kernel
```bash
jupyter kernelspec remove myenv
```

* Intall holoviews

```bash
$ workon orbichord
(orbichord)$ pip install "holoviews[recommended]"
(orbichord)$ pip install networkx
```
