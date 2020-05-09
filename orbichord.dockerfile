from archlinux

# Install package dependencies
run pacman --noconfirm -Syu
run pacman --noconfirm -S \
    git python python-pip python-pygame \
    python-pyaudio nodejs npm jupyterlab \
    lilypond openssh fluidsynth soundfonts \
    sudo vim

# Install jupyter extension
run jupyter labextension install @pyviz/jupyterlab_pyviz

# Install python packages
run pip install "holoviews[recommended]"
run pip install plotly