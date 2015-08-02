from catalog.forms import ImageUpload
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render
from .models import Main_table, Locations, Authors, User_info, LoanedBook

# Create your views here.
def post_list(request):
    books = Main_table.objects.filter().order_by('id')
    locations = Locations.objects.all()
    authors = Authors.objects.all()
    return render(request, 'catalog/post_list.html', {'books':books, 'loc':locations, 'authors': authors})

def book_info(request, rfidValue):
    try:
        book = Main_table.objects.get(rfid=rfidValue)
        to_json_book = {
            "title": book.title,
            "author": book.author.name,
            "year_pb": book.year_pb,

        }

        return JsonResponse(to_json_book)
    except Main_table.DoesNotExist:
        return HttpResponse("Error, does not exist")

def user_info(request, barcodeValue):
    try:
        user = User_info.objects.get(barcode_id=barcodeValue)
        userBooks = getUserLoanedBooks(user)

        to_json = {
            "barcode": user.barcode_id,
            "name": user.name,
            "department": user.department,
            "loaned_books":userBooks
        }
        return JsonResponse(to_json)
    except User_info.DoesNotExist:
        return  HttpResponse("Error, does not exist")

def saveBookToUser (request, bookID, userID):
    user = User_info.objects.get(barcode_id=userID)
    book = Main_table.objects.get(rfid=bookID)

    loanedBooks = LoanedBook.objects.filter(user = user).all()

    ################################################################

    isTakenAlready = False

    for row in loanedBooks:
        if row.book == book:
            isTakenAlready = True
            return JsonResponse({"message":"Book is loaned already",
                                 "status": False
                                 })


    if not isTakenAlready:
        newBook = LoanedBook()
        newBook.user = user
        newBook.book = book
        newBook.save()

    userBooks = getUserLoanedBooks(user)

    ################################################################
    return JsonResponse({"user":user.name,
                         "books": userBooks,
                         "status": True
                         })

#return books#
def returnBooks (request, bookID, userID):
    user = User_info.objects.get(barcode_id=userID)
    book = Main_table.objects.get(rfid=bookID)

    returnBooks = LoanedBook.objects.filter(user = user).all()

    ################################################################

    isReturnedAlready = False

    for row in returnBooks:
        if row.book == book:
            row.book.delete()

    userBooks = getUserLoanedBooks(user)
    ################################################################
    return JsonResponse({"user":user.name,
                         "books": userBooks,
                         })



#return books end#


def getUserLoanedBooks(user):
    userBooks = []
    loanedBooks = LoanedBook.objects.filter(user = user).all()

    for item in loanedBooks:
        temp = {
            "bookname": item.book.title,
            "year_published": item.book.year_pb,
            "author": item.book.author.name,
            "created_at": item.created_at,
            "expires_at": item.expires_at,
        }
        userBooks.append(temp)
    return userBooks

def upload_pic(request):
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            m = Main_table.objects.get(pk=id)
            m.image = form.cleaned_data['image']
            form.save()
            return HttpResponse('image upload success')
        return HttpResponseForbidden('allowed only via POST')

#user photo
'''def upload_userPhoto(request):
    if request.method =='POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            p = User_info.objects.get(pk=id)
            p.user_photo=form.cleaned_data['user_photo']
            form.save()
            return HttpResponse('photo uploaded')
        return HttpResponseForbidden('Error')'''