from django.db import models


class Locations(models.Model):
    bookCode = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    shelve = models.CharField(max_length=255)

    def publish(self):
        self.save()
    def __str__(self):
        return self.bookCode

class Authors(models.Model):
    author_id = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)

    def publish(self):
        self.save()
    def __str__(self):
        return self.author_name

class Main_table(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.CharField(max_length=255)
    author_name_id = models.CharField(max_length=255)
    year_pb = models.CharField(max_length=255)
    location_id = models.CharField(max_length=255)
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


