#!/bin/bash
set -e 

BIBLIOGRAPY="../bibliograpy/bibliogra.py"
BIB="./blockchain.bib.webexport"

cat ./blockchain_peerreviewed.bib ./blockchain_eprint.bib > "${BIB}"

rm -rf blockchainbib_html/*.html
cp Changelog.txt blockchainbib_html/

python2 ${BIBLIOGRAPY} -f "${BIB}" blockchainbib_html

cp blockchainbib_html/year_reverse.html blockchainbib_html/index.html
