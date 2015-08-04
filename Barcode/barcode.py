import urllib2
from User import User
from Book import Book

import json



'''

Barcode
    readBarcode()
JsonParser
    json -> object
    parseJsonToUser
    parse
HtmlHelper
    connect(url) -> Json
RfidHelper
    rfidRead() -> String

MainClass
    url ="http://localhost"
    htmlHelper = HtmlHelper()
    jsonParser = JsonParser()

    jsonData = htmlHelper.get(url)
     user = jsonParser.parserJsonToUser(jsonData)



def barcode(barcodeNumber):

    #print barcodeNumber
    url = "http://127.0.0.1:8000/user/" + barcodeNumber

    r = urllib2.urlopen(url)
    data = json.loads(r.read())
    parsedUser = parseJsonToUser(data)
    printUserDetails(parsedUser)
'''

def parseJsonToUser(data):
    name = data['name']
    department = data['department']
    barcodeID = data['barcode']
    loanedBooks  = data['loaned_books']
    books = []
    for jsonBook in loanedBooks:
        print jsonBook
        book = Book(jsonBook['bookname'], jsonBook['year_published'], jsonBook['author'])
        books.append(book)

    user = User(name, department, barcodeID, books)
    return user

def printUserDetails(user):
    print ("name: " + user.name)
    print ("department: " + user.department)
    print ("Id:" + user.barcode_id)
    print '\n'
    print "Loaned Books: \n"

    for loan_info in user.loaned_books:
        for key, value in loan_info.iteritems():
            print key, value



hid = { 4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k', 15: 'l', 16: 'm',\
        17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v', 26: 'w', 27: 'x', 28: 'y',\
        29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7', 37: '8', 38: '9', 39: '0', 44: ' ',\
        45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';' , 52: '\'', 53: '~', 54: ',', 55: '.', 56: '/'}

hidUp = { 4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K', 15: 'L', 16: 'M',\
         17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V', 26: 'W', 27: 'X', 28: 'Y',\
         29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 34: '5', 35: '^', 36: '&', 37: '*', 38: '9', 39: ')', 44: ' ',\
         45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':' , 52: '"', 53: '~', 54: '<', 55: '>', 56: '?'}

readCode = open('/dev/hidraw0', 'r')

def readBarcode():
    shift = False
    barcodeNumber = ""
    done = False
    while not done:
            ## Get the character from the HID
            buffer = readCode.read(8)
            for c in buffer:
                if ord(c) > 0:
                    ##  40 is carriage return which signifies
                    ##  we are done looking for characters
                    if int(ord(c)) == 40:
                        #done = True
                        done = True
                        break

                    ##  If we are shifted then we have to
                    ##  use the hid2 characters.
                    if shift:

                        ## If it is a '2' then it is the shift key
                        if int(ord(c)) == 2 :
                            shift = True

                        ## if not a 2 then lookup the mapping
                        else:
                            barcodeNumber += hidUp[ int(ord(c)) ]
                            shift = False

                    ##  If we are not shifted then use
                    ##  the hid characters

                    else:

                        ## If it is a '2' then it is the shift key
                        if int(ord(c)) == 2 :
                            shift = True
                        ## if not a 2 then lookup the mapping
                        else:
                            barcodeNumber += hid[ int(ord(c)) ]
    return barcodeNumber