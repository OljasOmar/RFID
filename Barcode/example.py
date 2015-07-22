import as3992_api
import urllib2
import json
from Book import Book


def rfid(rfidNumber):

    url = "http://127.0.0.1:8000/book/" + rfidNumber
    response = urllib2.urlopen(url)
    data = json.load(response)
    parsedBook = parseJsonToBook(data)
    printBookDetails(parsedBook)

def parseJsonToBook(data):
    author = data['author']
    year_published = data['year_pb']
    title = data['title']
    book = Book(title, year_published, author)
    return book

def printBookDetails(book):
    print ('Title: ' + book.title)
    print ('Author: ' + book.author)
    print ('Year: ' + book.year_published)



    

    
def main():
    ann = as3992_api.AntennaDevice()
    
    ann.set_antenna_state(True)

    print ("Book Info:")
    for epc, rssi in ann.iter_epc_rssi():
        a= str(epc.encode("HEX"))
        #b = str(rssi)
        print a
        rfid(a)
        
    ann.set_antenna_state(False)

if __name__ == "__main__":
    main()
