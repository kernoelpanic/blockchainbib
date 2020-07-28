# Blocks & Chains Bibliography 

A Bibtex bibliography including eprints/pre-prints and peer-reviewed publications related to, or of relevance in, the field of cryptocurrencies and distributed ledger technologies, commonly referred to as *blockchains*.

Papers in `blockchain.bib` are currently exported as `.html` to
[https://allquantor.at/blockchainbib](https://allquantor.at/blockchainbib).

The topics of the papers in this bibliography encompass various aspects that are directly or indirectly related to this interdisciplinary field e.g.,:
* Bitcoin and other cryptocurrencies
* Credit networks and payment channels
* Smart contract platforms
* Smart contract analysis and applications
* Distributed systems aspects
* Applied cryptography applicable in this context
* Economics and game theory
* Privacy and transparency
* General IT-Security related issues
* Regulatory and legal issues
* Usability and usable-security
* ...

## Usage of this bibliography 

Just reference the `blockchain.bib` in your bibtex `\bibliography{}` and compile your latex files as usual.
See the `test` folder for an example based on an IEEE template.

### Advanced usage: Download all papers
Make sure python 2 is running on your system

    python2 --version

Make sure [Pybtex!](https://pybtex.org/) is installed

    pip install pybtex

To download the papers into the `./papers` folder type:
```bash
$ python fetch_pdfs.py ./blockchain.bib papers/
```

### Advanced usage: Generate html files
To generate a html paper list you need to clone/install the [bibloograpy](https://github.com/NullHypothesis/bibliograpy) tool by Philipp Winter.
```bash
$ git clone https://github.com/NullHypothesis/bibliograpy
$ cd blockchainbib
$ bash generate.sh
```


## Contribute 

Generally contributions are welcome and might fall in the one of the following categories.

### Contribute by adding/updating an entry in the blockchain.bib file

The requirements for a paper to be added to the bib are:
* It must be **open-access** and not locked behind a pay-wall
* It is either:
  1. A peer-reviewed paper which has been published on an academic venue (e.g., conferences proceeding, journal, workshop )
  2. A pre-print/eprint of a paper (published for example on http://arxiv.org) that has not been published at an peer-reviewed venue (yet). The criteria for a paper in this category are:
      + based on facts
      + systematic structure
      + no marketing
      + not pure speculation
      + written in comprehensible English

#### How to add/update an entry

1. Add or update the bib entry in `blockchain.bib`

2. Run the `test/Makefile` to see if
everything builds as expected.
```shell
$ cd ./test
$ make test
...
  COMPILED SUCCESSFULLY!
...
```

3. issue pull request on github

### Contribute code 
This project is a *quick-and-dirty* approach and various evolutionary steps are possible e.g., :
  * Migrate to another dataformat for entries (e.g., JSON-LD)
    + Add abstract to entries
    + Add tags to entries
  * Migrate to a github.io page and use some lightweight JavaScript to filter entries
  * Provide a simple (local) interface to add entries
  * Generate the resulting .bib files based on custom selection

## Notes 
Note that only papers in `blockchain.bib` are currently exported as `.html` to
[https://allquantor.at/blockchainbib](https://allquantor.at/blockchainbib).
There are also references in `blockchain_online.bib` to online resources like for example:
+ github projects
+ block explorer websites
+ developer references (wiki entries, etc.)
+ Again the requirements form above hold:
 - not purely marketing (some banners on websites are acceptable)
 - not pure speculation
 - written in comprehensible English


## Related bibliographies 
A list of other (possibly outdated) collections of resources on this topic:

* Collection by Christian Decker:
  + https://github.com/cdecker/btcresearch

* Collection by Jeremy Clark:
    + http://users.encs.concordia.ca/~clark/biblio.php#bitcoin

* Collection by Brett Scott:
    + https://docs.google.com/spreadsheets/d/1VaWhbAj7hWNdiE73P-W-wrl5a0WNgzjofmZXe0Rh5sg/htmlview?usp=sharing&pli=1&sle=true

* Collection in the Bitcoin wiki (subset of the above)
    + https://en.bitcoin.it/wiki/Research

* Reading list repository of *Blockstack*:
  + https://github.com/blockstack/reading-list

* Publications section of IC3:
  + http://www.initc3.org/publications

* Collection in the Bitcoinbyte blog (outdated):
    + https://thebitcoinbyte.wordpress.com/annotated-bibliography/

## Related Projects

* OpenCitations (in RDF or JSON-LD respectively)
	+ https://github.com/essepuntato/opencitations
	+ http://opencitations.net/
	+ https://json-ld.org/
* Paper on citation in RDF
	+ http://ceur-ws.org/Vol-1155/paper-05.pdf
* Zotero
	+ https://de.wikipedia.org/wiki/Zotero

## License

Bibliography license: CC BY
[![CC](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

Python code and `.tpl` templates license: GNU GENERAL PUBLIC LICENSE

## Credits  

* All authors that created the publications listed in this bibliography
* Philipp Winter (phw[at]nymity.ch) for the python fetch code and the `.tpl` templates
* Aljosha Judmayer (ajudmayer[at]sba-research[dot]org) initiator of this endeavor
* Nicolas Christin (Suggestion of publications)
* Daniel Kraft (Suggestion of publications)
* Nicholas Stifter (Suggestion of publications)
* Philipp Schindler (Suggestion of publications)
* Alexei Zamyatin (Suggestion of publications)
* Bernhard Haslhofer (Suggestion of publications)
* Andreas Kern (Suggestion of publications & code)
