from django.db import models


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
        return self.name + ' - '

class Main_table(models.Model):
    title = models.CharField(max_length=255, help_text="Enter title of a book")
    author = models.ForeignKey('Authors')
    year_pb = models.CharField(max_length=255, help_text="Enter published year of a book")
    location = models.ForeignKey('Locations')
    rfid = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Image_books/')

    def publish(self):
        self.save()
    def __str__(self):
        return self.title

    def image_tag(self):
        return u'<img src="%s" />' % self.image
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


