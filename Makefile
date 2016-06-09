
all: bib

bib:
	cat blockchain_* > blockchain.bib
	cat blockchain_peerreviewed.bib blockchain_eprint.bib > blockchain.bib.webexport
