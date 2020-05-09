from archlinux

# Install package dependencies
run pacman --noconfirm -Syu
run pacman --noconfirm -S \
    git nodejs npm make python python-pip \
    python-pygame python-pyaudio pandoc jupyterlab \
    lilypond openssh fluidsynth soundfont-fluid \
    sudo vim

# Install jupyter extension
run jupyter labextension install @pyviz/jupyterlab_pyviz

# Install python packages
run pip install "holoviews[recommended]"
run pip install plotly
run pip install sphinx
run pip install nbsphinx
