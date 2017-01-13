"""An example program that uses the elsapy module"""

from elsapy import *

## Load configuration
conFile = open("config.json")
config = json.load(conFile)
conFile.close()

## Initialize client
myCl = ElsClient(config['apikey'])
myCl.inst_token = config['insttoken']

## Author example
# Initialize author with uri
myAuth = ElsAuthor(uri = 'https://api.elsevier.com/content/author/AUTHOR_ID/7004367821')
# Read author data, then write to disk
if myAuth.read(myCl):
    print ("myAuth.full_name: ", myAuth.full_name)
    myAuth.write()
else:
    print ("Read author failed.")

## Affiliation example
# Initialize affiliation with ID as string
myAff = ElsAffil(affil_id = '60101411')
if myAff.read(myCl):
    print ("myAff.name: ", myAff.name)
    myAff.write()
else:
    print ("Read affiliation failed.")

## Scopus (Abtract) document example
# Initialize document with ID as integer
scpDoc = AbsDoc(scp_id = 84872135457)
if scpDoc.read(myCl):
    print ("scpDoc.title: ", scpDoc.title)
    scpDoc.write()   
else:
    print ("Read document failed.")

## ScienceDirect (full-text) document example using PII
piiDoc = FullDoc(sd_pii = 'S1674927814000082')
if piiDoc.read(myCl):
    print ("piiDoc.title: ", piiDoc.title)
    piiDoc.write()   
else:
    print ("Read document failed.")

## ScienceDirect (full-text) document example using DOI
doiDoc = FullDoc(doi = '10.1016/S1525-1578(10)60571-5')
if doiDoc.read(myCl):
    print ("doiDoc.title: ", doiDoc.title)
    doiDoc.write()   
else:
    print ("Read document failed.")


## Load list of documents from the API into affilation and author objects.
# Since a document list is retrieved for 25 entries at a time, this is
#  a potentially lenghty operation - hence the prompt.
print ("Load documents (Y/N)?")
s = input('--> ')

if (s == "y" or s == "Y"):

    ## Read all documents for example author, then write to disk
    if myAuth.readDocs(myCl):
        print ("myAuth.doc_list has " + str(len(myAuth.doc_list)) + " items.")
        myAuth.writeDocs()
    else:
        print ("Read docs for author failed.")

    ## Read all documents for example affiliation, then write to disk
    if myAff.readDocs(myCl):
        print ("myAff.doc_list has " + str(len(myAff.doc_list)) + " items.")
        myAff.writeDocs()
    else:
        print ("Read docs for affiliation failed.")

## Initialize author search object and execute search
myAuthSrch = ElsSearch('authlast(keuskamp)','author')
myAuthSrch.execute(myCl)
print ("myAuthSrch has", len(myAuthSrch.results), "results.")

## Initialize affiliation search object and execute search
myAffSrch = ElsSearch('affil(amsterdam)','affiliation')
myAffSrch.execute(myCl)
print ("myAffSrch has", len(myAffSrch.results), "results.")

## Initialize doc search object and execute search, retrieving all results
myDocSrch = ElsSearch('star+trek+vs+star+wars','scopus')
myDocSrch.execute(myCl, get_all = True)
print ("myDocSrch has", len(myDocSrch.results), "results.")

