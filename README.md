# Blockchain Bib

A Bibtex bibliography for **Bitcoin** and **blockchain** related papers and publications. 


## Structure of this bibliography
The scientific community adapted relatively slow to this emerging and fast moving field of cryptographic currencies and blockchains. 
This was the reason that for quite a while the only resources available have been the Bitcoin source code, blog/forum/mailing list posts, and other online publications. 
Also the original Bitcoin [paper](https://bitcoin.org/bitcoin.pdf) which initiated the hype was published online without any prior peer-review. 

Meanwhile a constant flow of scientific publications can be observed. 
This leads to an increasing number of available peer-reviewed publications. 
Although peer-review is *not* always a guaranty for best quality, we initially distinguish publications in this field into three different
categories. 
The nonnegotiable hard requirement for any category is that the work must be **open-access** and not locked behind pay-walls. 

**Note:** that only papers in `blockchain_peerreviewed.bib` and `blockchain_eprint.bib` are currently exported as `.html` to
[https://allquantor.at/blockchainbib](https://allquantor.at/blockchainbib).

* `blockchain_peerreviewed.bib`
References in this category are peer-reviewed papers which have been published on scientific venues 
(e.g. conferences proceedings, journals, workshops, etc.)

* `blockchain_eprint.bib`
References in this category are preprints/eprints of papers (for example on http://arxiv.org) that have not been published at an peer-reviewed venue (yet).
The criteria for a paper/publication in this category is:
    + based on facts 
    + systematic structure 
    + no marketing
    + not pure speculation
    + written in comprehensible English 

* `blockchain_online.bib`
References in this category are online resources like for example:  
    + github projects
    + block explorer websites
    + developer references (wiki entries, etc.) 

Again the requirements form above hold:
    + not purely marketing (some banners on websites are acceptable)
    + not pure speculation
    + written in comprehensible English 

In respect to the original *publication spirit* of Bitcoin, we combine all
references into a single blob file called `blockchain.bib` when executing 
`make` in the projects root directory.


### Download papers

To download the papers into the `./papers` folder type:
```bash
$ python fetch_pdfs.py ./blockchain_peerreviewed.bib papers/
```

### Generate html list

To generate a html paper list you need to clone/install the [bibloograpy](https://github.com/NullHypothesis/bibliograpy) tool by Philipp Winter. 
```bash
$ git clone https://github.com/NullHypothesis/bibliograpy 
$ cd blockchainbib
$ bash generate.sh
```


## Related work
A list of other collections of resources on this topic:

* Jeremy Clacks collection:
    + http://users.encs.concordia.ca/~clark/biblio.php#bitcoin

* Brett Scott collection (huge):
    + https://docs.google.com/spreadsheets/d/1VaWhbAj7hWNdiE73P-W-wrl5a0WNgzjofmZXe0Rh5sg/htmlview?usp=sharing&pli=1&sle=true

* Collection in the Bitcoin wiki (subset of the above)
    + https://en.bitcoin.it/wiki/Research

* Collection in the Bitcoinbyte blog (outdated)
    + https://thebitcoinbyte.wordpress.com/annotated-bibliography/



## Contribute 

### Add/Update an entry in the .bib file

1. Add or update the bib entry in one of the three files: `blockchain_peerreviewed.bib`, `blockchain_eprint.bib` or
`blockchain_online.bib`. **Note:** that only papers in `blockchain_peerreviewed.bib` and `blockchain_eprint.bib` are currently exported as `.html` to 
[https://allquantor.at/blockchainbib](https://allquantor.at/blockchainbib). 
Do not edit the `blockchain.bib` file it will be auto generated when running `make` in the root of the project. 

2. Run the `test/Makefile` to see if 
everything works as expected. 
```shell
$ cd ./test
$ make 
$ evince bare_jrnl.pdf
```

## License

Bibliography license: CC BY
[![CC](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

Python code and `.tpl` templates license: GNU GENERAL PUBLIC LICENSE

## Credits 

* All authors that created the publications listed in this bibliography
* Philipp Winter (phw[at]nymity.ch) for the python fetch code and the `.tpl` templates
* Aljosha Judmayer (ajudmayer[at]sba-research[dot]org)
