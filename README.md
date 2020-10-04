# DSpace-Metadata-DOI
# Author: Yan Han   Updated Oct 3, 2020

Converting DSpace metadata to CrossRef DOI metadata

This program is to convert DSpace metadata export to CrossRef DOI metadata.
DSapce's exported metadata is formatted as a CSV file with the following columns:
"dc.identifier.doi	dc.identifier.uri	dc.title	dc.title.alternative	dc.contributor.author	dc.date.issued	dc.identifier.journal	dc.identifier.issn	dc.source.volume	dc.source.issue	dc.source.beginpage	dc.identifier.citation	dc.description	dc.description.abstract	dc.eprint.version	dc.language.iso	dc.publisher	dc.relation.url	dc.rights	dc.rights.uri	dc.subject	dc.type"


-- Sample CrossRef DOI files for journal:  CrossRef sample Test file: journal_doi_sample_edit.xml
  Also at https://gitlab.com/crossref/schema/-/blob/master/examples/journal_article_4.4.2.xml
-- CrossRef metadata quality check website: https://data.crossref.org/reports/parser.html


How to Run:
1. > python3 DSpace-Metadata-doi

Output is an XML file compliant with CrossRef metadata
