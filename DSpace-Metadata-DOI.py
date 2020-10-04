
# Author: Yan Han
# Date: 2020-09-24
# Updated: 2020-09-28

# This program is to convert DSpace metadata export to CrossRef DOI metadata.
# DSapce  metadata output formatted as "dc.identifier.doi	dc.identifier.uri	dc.title	dc.title.alternative	dc.contributor.author	dc.date.issued	dc.identifier.journal	dc.identifier.issn	dc.source.volume	dc.source.issue	dc.source.beginpage	dc.identifier.citation	dc.description	dc.description.abstract	dc.eprint.version	dc.language.iso	dc.publisher	dc.relation.url	dc.rights	dc.rights.uri	dc.subject	dc.type"

# CrossRef sample Test file: journal_doi_sample_edit.xml
# CrossRef metadata quality check website: https://data.crossref.org/reports/parser.html
#

import csv
import xml.etree.ElementTree as ET
from datetime import datetime

date_time_str = '12/01/08'
date_time_obj = datetime.strptime(date_time_str, '%m/%d/%y')

print("the date time str", date_time_str)
print("the date is ", date_time_obj)


# debug flag
debug = True

# output file name
output = open("output1.xml", "w")

# Crossref DOI metadata elements. see the sample at
# def GenerateXML(filename):

metadata =''
journal_str =''

# input csv file name
input_filename = "test.csv"

# initializing
fields =[]
rows = []

# reading the csv
with open(input_filename, mode='r') as csvfile:
    # creating a csv reader
    csvreader = csv.reader(csvfile)

    # extracting filed names
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

    print("Total no. of rows: %d"%(csvreader.line_num))

    # printing the field names
    print("Field names are:" + ','.join(field for field in fields))

    if debug:
        num_row = 10
    else:
        num_row = csvreader.line_num

    #i = 0
    for row in rows[:num_row]:
        print ("row =", row)

        journal= ET.Element("journal")

        #journal_metadata_str =''

        # Section 1 of the Journal metadata. This is fixed for one journal
        journal_metadata = ET.SubElement(journal, 'journal_metadata')
        journal_metadata.set('language', 'en')

        journal_full_title = ET.SubElement(journal_metadata, 'full_title')
        journal_abbrev_title = ET.SubElement(journal_metadata, 'abbrev_title')
        journal_issn = ET.SubElement(journal_metadata, 'issn')
        journal_issn.set('media_type', 'print')

        journal_full_title.text='Rangelands'
        journal_abbrev_title.text='Rangelands'
        journal_issn.text='0190-0528'

        # Section 2 of the DOI metadata. This varies for each article
        journal_issue  = ET.SubElement (journal, 'journal_issue')

        publication_date = ET.SubElement(journal_issue, 'publication_date')
        publication_date_year = ET.SubElement(publication_date, 'year')
        publication_date.set('media_type', "print")
        journal_volume = ET.SubElement(journal_issue, 'journal_volume')
        journal_volume_volume = ET.SubElement(journal_volume, 'volume')
        journal_issue_issue  = ET.SubElement(journal_issue, 'issue')

        # Section 3 of the DOI metadata
        journal_article = ET.SubElement(journal, 'journal_article')
        journal_article.set('publication_type', 'full_text')

        titles = ET.SubElement(journal_article, 'titles')
        title = ET.SubElement(titles, 'title')
        contributors = ET.SubElement(journal_article, 'contributors')


        # each row, assigning to each field
        for col in row:
            id_doi     = row[0]
            id_url     = row[1]
            csv_title  = row[2]
            title_alt  = row[3]
            author_list= row[4]
            date_str   = row[5]
            id_journal = row[6]
            issn       = row[7]
            volume     = row[8]
            issue      = row[9]
            begin_pg   = row[10]
            id_citation= row[11]
            desc       = row[12]
            desc_abst  = row[13]
            lang       = row[14]
            publisher  = row[15]
            relation_url=row[16]
            rights_uri = row[17]
            subject    = row[18]
            article_type=row[19]

        journal_volume_volume.text = volume
        journal_issue_issue.text= issue

        title.text = csv_title

        if debug:
            print("author_list : ", author_list)
            print("author_list len", len(author_list))

        if (len(author_list.strip()) != 0): # no author, only corp author
            authors = author_list.strip().split("||")
            #print ("authors list len =", len(authors))

            if (len(authors) == 1):
                person_name = ET.SubElement(contributors, 'person_name')
                person_name.set('sequence', 'first')
                person_name.set('contributor_role', 'author')
                given_name = ET.SubElement(person_name, 'given_name')
                surname = ET.SubElement(person_name, 'surname')

                a1_name = authors[0].split(',')
                given_name.text  = a1_name[1].strip()
                surname.text     = a1_name[0].strip()
                print("author1 name =", a1_name)
            elif (len(authors) == 2):
                person_name = ET.SubElement(contributors, 'person_name')
                person_name.set('sequence', 'first')
                person_name.set('contributor_role', 'author')
                given_name = ET.SubElement(person_name, 'given_name')
                surname = ET.SubElement(person_name, 'surname')

                a2_person_name = ET.SubElement(contributors, 'person_name')
                a2_person_name.set('contributor_role', 'author')
                a2_person_name.set('sequence', 'additional')
                a2_given_name = ET.SubElement(a2_person_name, 'given_name')
                a2_surname = ET.SubElement(a2_person_name, 'surname')

                a1_name = authors[0].split(',')
                given_name.text = a1_name[1].strip()
                surname.text    = a1_name[0].strip()
                a2_name  = authors[1].split(',')
                a2_given_name.text = a2_name[1].strip()
                a2_surname.text    = a2_name[0].strip()
                print("author 2 name =", a2_name)
            else: # more than 3 authors, use only 3
                person_name = ET.SubElement(contributors, 'person_name')
                person_name.set('sequence', 'first')
                person_name.set('contributor_role', 'author')
                given_name = ET.SubElement(person_name, 'given_name')
                surname = ET.SubElement(person_name, 'surname')

                a2_person_name = ET.SubElement(contributors, 'person_name')
                a2_person_name.set('contributor_role', 'author')
                a2_person_name.set('sequence', 'additional')
                a2_given_name = ET.SubElement(a2_person_name, 'given_name')
                a2_surname = ET.SubElement(a2_person_name, 'surname')

                a3_person_name = ET.SubElement(contributors, 'person_name')
                a3_person_name.set('contributor_role', 'author')
                a3_person_name.set('sequence', 'additional')
                a3_given_name = ET.SubElement(a3_person_name, 'given_name')
                a3_surname = ET.SubElement(a3_person_name, 'surname')

                a1_name = authors[0].split(',')
                given_name.text = a1_name[1].strip()
                surname.text    = a1_name[0].strip()
                a2_name  = authors[1].split(',')
                a2_given_name.text = a2_name[1].strip()
                a2_surname.text    = a2_name[0].strip()

                a3_name  = authors[2].split(',')
                a3_given_name.text = a3_name[1].strip()
                a3_surname.text    = a3_name[0].strip()
                print("author 3 =", a3_name)

        # handle contributor's organization
        organization = ET.SubElement(contributors, 'organization')
        organization.set('sequence', "additional")
        organization.set('contributor_role', "author")
        organization.text = "Society for Range Management"

        # handle abstract
        if (len(desc) !=0):
            jats_abstract = ET.SubElement(journal_article, 'jats:abstract')
            jats_p = ET.SubElement(jats_abstract, 'jats:p')
            jats_p.text = desc
        else:
            if (len(desc_abst) !=0):
                jats_abstract = ET.SubElement(journal_article, 'jats:abstract')
                jats_p = ET.SubElement(jats_abstract, 'jats:p')
                jats_p.text = desc_abst

        # insert these data into journal issue elements
        ja_publication_date = ET.SubElement(journal_article, 'publication_date')
        ja_publication_date_year = ET.SubElement(ja_publication_date, 'year')
        ja_publication_date.set('media_type', "print")

        date_issued = date_time_obj.strptime(date_str, '%m/%d/%y')
        date_issued_year = date_issued.year
        publication_date_year.text= str(date_issued_year)
        ja_publication_date_year.text = publication_date_year.text

        ## begin_pg (according to Crossref Schema) must be integer. DSpace output has uncleared data. ignore this for now
        #pages = ET.SubElement(journal_article, 'pages')
        #first_page = ET.SubElement(pages, 'first_page')
        #first_page.text = begin_pg

        doi_data = ET.SubElement(journal_article, 'doi_data')
        doi = ET.SubElement(doi_data, 'doi')
        resource = ET.SubElement(doi_data, 'resource')
        doi.text = id_doi
        resource.text = id_url

        # finally, convert one XML object to string at one time
        journal_str += ET.tostring(journal).decode()
        #print ("record = ", journal_str)
        # end for loop

# Crossref DOI metadata Head
article_metadata = ''

doi_batch_head ='<?xml version="1.0" encoding="UTF-8"?><doi_batch xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.crossref.org/schema/4.4.2 https://www.crossref.org/schemas/crossref4.4.2.xsd" xmlns="http://www.crossref.org/schema/4.4.2" xmlns:jats="http://www.ncbi.nlm.nih.gov/JATS1" xmlns:fr="http://www.crossref.org/fundref.xsd" version="4.4.2">'

doi_batch_depositor = '<head> <doi_batch_id>Rangelands_2020_09_15</doi_batch_id> <timestamp>20200915123306</timestamp><depositor> <depositor_name>Yan Han</depositor_name><email_address>yhan@arizona.edu</email_address></depositor><registrant>The University of Arizona Libraries</registrant></head><body>'

#journal_info = '<body> <journal> <journal_metadata language="en"> <full_title>Rangelands</full_title><abbrev_title>Rangelands</abbrev_title><issn media_type="print">0190-0528</issn> </journal_metadata>'

metadata = doi_batch_head + doi_batch_depositor
metadata += journal_str
metadata += "</body></doi_batch>"

if debug:
    print(metadata)

output.write(metadata)
output.close()
