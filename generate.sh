#!/bin/bash

BIBLIOGRAPY="../bibliograpy/bibliogra.py"
BIB="./blockchain_peerreviewed.bib"

rm -rf blockchainbib_html/*.html
cp Changelog.txt blockchainbib_html/

python2 ${BIBLIOGRAPY} -f "${BIB}" blockchainbib_html

cp blockchainbib_html/year_reverse.html blockchainbib_html/index.html
