#!/bin/bash
set -e 

BIBLIOGRAPY="../bibliograpy/bibliogra.py"
BIB="./blockchain.bib"

rm -rf blockchainbib_html/*.html

python2 ${BIBLIOGRAPY} -f "${BIB}" blockchainbib_html

cp blockchainbib_html/year_reverse.html blockchainbib_html/index.html
