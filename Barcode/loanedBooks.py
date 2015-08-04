from types import ListType
import User
import StatusMessage
import LoanedBook
import barcode
import urllib2
import json
import as3992_api
from barcode import parseJsonToUser, printUserDetails
import time

lastUserBarcodeNumber = ""
userSession = None

def rfid(rfidNumber):

    barcodeNumber = barcode.readBarcode()
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

def welcomeScreen():
    print "Welcome"
    print "Please, scan your barcode:"
    userID = barcode.readBarcode()
    # serverge user turaly info al
    url = "http://127.0.0.1:8000/user/" + userID
    r = urllib2.urlopen(url)
    data = json.loads(r.read())
    global userSession
    userSession = parseJsonToUser(data)
    if userSession != None:
        infoScreen()

def infoScreen():
    global userSession
    print "Hello, ", userSession.name
    print "Your book list:"
    for index, book in enumerate(userSession.loaned_books):
        print "Bookname:",index + 1, book.title + ' | ' + book.author + ' | ' + book.year_published


    print "========================================================"
    print "1. Loan a book"
    print "0. Back"

    choice = raw_input("Choose an option:")

    if choice == "1":
        #open new session to read RFID
        print "1"
    elif choice == "0":
        userSession = None
        welcomeScreen()
    else:
        print "Your choice was incorrect"

def main():
    welcomeScreen()
    '''print ("Book Info:")
    ann = as3992_api.AntennaDevice()

    ann.set_antenna_state(True)


    for epc, rssi in ann.iter_epc_rssi():
        a= str(epc.encode("HEX"))
        b = str(rssi)
        print a
        rfid(a)

    ann.set_antenna_state(False)'''

'''def fortest():
    print("This is fortest")
    rfid("123456")'''

if __name__ == "__main__":
    main()


