from django.db import models
# from ocr import OCR
from .imageProcess import OCR

# class ImgUpload(models.FileField):
    

# Create your models here.
class Photo(models.Model):

    TEXT_IDENTIFIED = ""
    # def __init__(self):
    #     self.TEXT_IDENTIFIED = ""

    def save(self, **kwargs):
        super(Photo, self).save(**kwargs)
        ocr = OCR()
        text_identified = ocr.img2txt()
        

    input_image = models.FileField()
    # image = input_image.
    # print(input_image.__dict__)
    # print(f"input_image type: {type(input_image.read())}")
    # text = ocr.img2txt(image=input_image)
    # print(text)
    number_identified = models.CharField(max_length=30)

class Owner(models.Model):
    name = models.CharField(max_length=50)
    numberplate = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    registration_year = models.IntegerField(max_length=4)