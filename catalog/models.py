from datetime import date, timedelta
from django.db import models
import datetime

class Locations(models.Model):
    bookCode = models.CharField(max_length=255, help_text="Enter code of the book. use UPPERCASE")
    department = models.CharField(max_length=255, help_text="Specify the department. Use UPPERCASE")
    shelve = models.CharField(max_length=255, help_text="Specify the shelve")

    def publish(self):
        self.save()
    def __str__(self):
        return self.bookCode + ' ' + self.department + ' ' + self.shelve

class Authors(models.Model):
    name = models.CharField(max_length=255, help_text="Enter name of the author")

    def publish(self):
        self.save()
    def __str__(self):
        return self.name + ' '

class Loaning_period(models.Model):
    period = models.CharField(max_length=255, help_text="Enter loaning period")
    calendar_days = models.IntegerField(default=0)

    def publish(self):
        self.save()
    def __str__(self):
        return self.period + " "

class User_info(models.Model):
    name = models.CharField(max_length=255, help_text="Enter user name")
    department = models.CharField(max_length=255, help_text="Name of the department")
    barcode_id = models.CharField(max_length=255, help_text="user id")
    #loanedBooks =
    #userImage check
    #user_photo = models.ImageField(upload_to='')

    def publish(self):
        self.save()
    def __str__(self):
        return self.name + ' '

class Main_table(models.Model):
    title = models.CharField(max_length=255, help_text="Enter title of a book")
    author = models.ForeignKey('Authors')
    year_pb = models.CharField(max_length=255, help_text="Enter published year of a book")
    location = models.ForeignKey('Locations')
    rfid = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Image_books/')
    loaning_period = models.ForeignKey('Loaning_period', default=0)

    def publish(self):
        self.save()
    def __str__(self):
        return self.title

    def image_tag(self):
        return u'<img src="%s" />' % self.image
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class LoanedBook(models.Model):
    user = models.ForeignKey(User_info)
    book = models.ForeignKey(Main_table)
    created_at = models.DateTimeField(auto_now = True)
    expires_at = models.DateTimeField(default= datetime.datetime.now(), editable=False)

    def save(self, *args, **kwargs):
        self.expires_at = datetime.datetime.now()+timedelta(days=self.book.loaning_period.calendar_days)
        super(LoanedBook, self).save(*args, **kwargs)

    def publish(self):
        self.save()

