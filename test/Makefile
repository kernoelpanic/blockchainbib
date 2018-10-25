####################################################
# ------------------------------------------------------------------------
# Minimalistic Makefile 
# ------------------------------------------------------------------------
####################################################

# You have to change this if you use latex instead of pdflatex.
# However, this also requires to update the build rules.
LATEX = pdflatex

# Change this to the file name of your LaTex source
FILE = bare_jrnl
INPUTS = inputs

.PHONY: all
all: clean inputs latex clean2 fetch 

.PHONY: inputs
inputs: $(wildcard inputs/*.tex) 
	ls inputs/*.tex | awk '{printf "\\input{%s}\n",latex  $$1}' > inputs.tex

.PHONY: latex 
latex: 
	$(LATEX) $(FILE).tex
	bibtex $(FILE)
	$(LATEX) $(FILE).tex
	$(LATEX) $(FILE).tex

.PHONY: clean
clean:
	-rm -f $(FILE).aux inputs.aux $(FILE).log 
	-rm -f $(FILE).bbl $(FILE).blg
	-rm -f $(FILE).nav $(FILE).out
	-rm -f $(FILE).toc $(FILE).snm

.PHONY: clean2
clean2: 
	-rm -f $(FILE).aux inputs.aux $(FILE).log 
	-rm -f $(FILE).bbl $(FILE).blg
	-rm -f $(FILE).nav $(FILE).out
	-rm -f $(FILE).toc $(FILE).snm


.PHONY: fetch
fetch:
	cd ../ && python2 fetch_pdfs.py blockchain.bib papers
