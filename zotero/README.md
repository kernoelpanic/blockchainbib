# Zotero enhancements 

## Update BibTeX.js export

Merge changes with current `BibTeX.js` Zotero exporter:
```bash
$ meld /home/$USER/snap/zotero-snap/common/Zotero/translators/BibTeX.js snap_zotero-snap_common_Zotero_translators_BibTeX_v2.js
```

Export with `BibTeX` and encoding `Western` 
![screenshot](./screenshot.png)

## Add custom PDF resolver

Go to `Edit -> Preferences -> Advanced -> Config Editor` and
then to `extensions.zotero.findPDFs.resolvers` and add the following json string:

```json
[{     "name": "URL Source",     "method": "GET",     "url": "{url}/#doi={doi}",     "mode": "html",     "selector": "#pdf",     "attribute": "href",     "automatic": false},{     "name":"Sci-Hub",     "method":"GET",     "url":"https://sci-hub.se/{doi}",     "mode":"html",     "selector":"#pdf",     "attribute":"src",     "automatic":false }]
```
