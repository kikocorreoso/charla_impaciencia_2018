Charla en [impaciencia 2018](http://www.impaciencia.org/)
==========================

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/kikocorreoso/charla_impaciencia_2018/master)

Instalación en local
====================

Con `conda` instalado, se puede hacer desde la línea de comandos:

`conda env create -f environment.yml`

`conda activate impaciencia`

`jupyter notebook`

Crear las slides
================

Para regenerar las slides se puede hacer:

`jupyter nbconvert Slides.ipynb --to slides --SlidesExporter.font_awesome_url="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css" --SlidesExporter.reveal_theme="beige" --SlidesExporter.reveal_url_prefix="00.static/reveal.js-3.5.0"`
