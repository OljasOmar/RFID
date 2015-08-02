from types import ListType
import StatusMessage
import LoanedBook
import barcode
import urllib2
import json
import as3992_api


def rfid(rfidNumber):

    barcodeNumber = barcode.mBarcodeNumber
    url = "http://127.0.0.1:8000/book/" + rfidNumber + "/user/" + barcodeNumber
    response = urllib2.urlopen(url)
    data = json.load(response)
    parsedLoanedBook = parseJsonToLoanedBook(data)

    if type(parsedLoanedBook) is ListType:
        for book in parsedLoanedBook:
            printLoanedBookDetails(book)
    else:
        printAlreadyLoanedDetails(parsedLoanedBook)

def parseJsonToLoanedBook(data):
    if data['status']:
        bookList = data['books']
        books = []
        for book in bookList:
            book_name = book['bookname']
            author = book['author']
            year_published = book['year_published']
            due_to = book['expires_at']
            loaned_book = LoanedBook.LoanedBook(book_name, author, year_published, due_to)
            books.append(loaned_book)
        return books
    else:
        message = data['message']
        s1 = StatusMessage.StatusMessage(message)
        return s1


def printLoanedBookDetails(loaned_book):
    print ('Title: ' + loaned_book.book_name)
    print ('Author: ' + loaned_book.author)
    print ('Year: ' + loaned_book.year_published)

def printAlreadyLoanedDetails(statusMessage):
    print ("Book status: " + statusMessage.message)

def main():
    print ("Book Info:")
    ann = as3992_api.AntennaDevice()

    ann.set_antenna_state(True)


    for epc, rssi in ann.iter_epc_rssi():
        a= str(epc.encode("HEX"))
        b = str(rssi)
        print a
        rfid(a)

    ann.set_antenna_state(False)

'''def fortest():
    print("This is fortest")
    rfid("123456")'''

if __name__ == "__main__":
    main()


