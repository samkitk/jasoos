from django.db import models
# from ocr import OCR
from .imageProcess import OCR

# Create your models here.
class Photo(models.Model):

    ocr = OCR()
    input_image = models.ImageField()
    print(f"input_image type: {type(input_image)}")
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