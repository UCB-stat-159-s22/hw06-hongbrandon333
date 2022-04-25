.PHONY : clean
clean :
	rm -f figurs/*.png
	rm -f audio/*.wav
	rm -rf _build/*
 

.PHONY : env
env:
	mamba env create -f environment.yml --name ligo
	conda activate ligo
	bash -ic 'conda activate ligo;python -m ipykernel install --user --name ligo --display-name "IPython -ligo"'

.PHONY : html
html:
	jupyter-book build .
    
.PHONY : html-hub
html-hub:
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
	@echo "Start the Python http server and visit:
	@echo "https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html"
  