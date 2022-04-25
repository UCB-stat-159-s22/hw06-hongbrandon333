.PHONY : clean
clean :
    rm -f figurs/*.png
    rm -f audio/*.wav
    rm -rf _build/*
 

.PHONY : env
env:
    mamba env create -f environment.yml -p ~/envs/ligo
    bash -ic 'conda activate ligo;python -m ipykernel install --user --name ligo --display-name "IPython - ligo"'

.PHONY : html
html:
    jupyter-book build .
    
.PHONY : html-hub
html-hub:
    jupyter-book config sphinx .
    sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
  