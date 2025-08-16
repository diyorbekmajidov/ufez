from django.db import models
from ckeditor.fields import RichTextField

from django.forms import ValidationError

def validate_file_size(value):
    filesize = value.size

    if filesize > 1000 * 2024:
        raise ValidationError("The maximum file size that can be uploaded is 2mb")
    else:
        return value
    

class Menu(models.Model):
    title = models.CharField(max_length=200)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    page = models.ForeignKey("Page", null=True, blank=True, on_delete=models.CASCADE)  # Sahifa uchun bog'lanish
    url = models.CharField(max_length=20, blank=True, null=True)  # URL uchun
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Menyu"
        verbose_name_plural = "Menyular"

    def __str__(self):
        return self.title
    
    def get_url(self):
        if self.page:
            return self.page.get_absolute_url()  # Sahifa uchun URL
        elif self.url:
            return self.url  # Faqat URL manzil bo'lsa
        else:
            return '#'  # Agar URL yoki sahifa bo'lmasa, hech narsa qilmasin

    def has_children(self):
        return self.children.filter(is_active=True).exists()  # Sub-menularda faollashtirish



class Page(models.Model):
    title = models.CharField("Sahifa nomi", max_length=200)
    slug = models.SlugField("Slug (URL uchun)", unique=True)
    content = RichTextField("Kontent")
    template = models.CharField("Shablon fayli", max_length=100, default="default.html")
    seo_title = models.CharField("SEO sarlavhasi", max_length=255, blank=True)
    seo_description = models.TextField("SEO tavsifi", blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Sahifa"
        verbose_name_plural = "Sahifalar"

    def get_absolute_url(self):
        return f'/{self.slug}/'  # Sahifa uchun URL (masalan: /about/)

    def __str__(self):
        return self.title

    

class News(models.Model):
    title = models.CharField("Yangilik sarlavhasi", max_length=200)
    views = models.IntegerField("Ko'rishlar soni", default=0)
    body = RichTextField("Matn")
    image = models.ImageField("Rasm", upload_to='news/', validators=[validate_file_size])
    created_at = models.DateTimeField("Yaratilgan vaqt", auto_now_add=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

    def __str__(self):
        return self.title
    
class Event(models.Model):
    title = models.CharField("E'lonlar sarlavhasi", max_length=200)
    views = models.IntegerField("Ko'rishlar soni", default=0)
    body = RichTextField("Matn")
    image = models.ImageField("Rasm", upload_to='news/', validators=[validate_file_size])
    created_at = models.DateTimeField("Yaratilgan vaqt", auto_now_add=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "E'lon"
        verbose_name_plural = "E'lonlar"

    def __str__(self):
        return self.title

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/', verbose_name='Rasm', validators=[validate_file_size])
    title = models.CharField(max_length=255, verbose_name='Sarlavha')
    description = models.TextField(verbose_name='Tavsif')

    class Meta:
        verbose_name = "Rasm"
        verbose_name_plural = "Rasmlar"

    def __str__(self):
        return self.title
class PhotoGallery(models.Model):
    title = models.CharField("Galereya sarlavhasi", max_length=200)
    images = models.ManyToManyField("Photo", verbose_name="Rasmlar")

    class Meta:
        verbose_name = "Rasm galereyasi"
        verbose_name_plural = "Rasm galereyalari"

    def __str__(self):
        return self.title
    


class VideoGallery(models.Model):
    title         = models.CharField(max_length=255, verbose_name='sarlavha')
    video         = models.CharField(max_length = 10055, verbose_name='Video URL', help_text="YouTube yoki boshqa video platformalardan video URL manzilini kiriting")
    image         = models.ImageField(upload_to='img/', verbose_name='Rasm', validators=[validate_file_size]) 
    views         = models.IntegerField(default=0, verbose_name="ko'rishlar soni")
    date_created  = models.DateField(auto_now_add=True)
    date_update   = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Video galereyasi"
        verbose_name_plural = "Video galereyalari"

    def __str__(self):
        return self.title

class Faq(models.Model):
    question = models.CharField(max_length=255, verbose_name="Savol")
    answer = models.TextField(verbose_name="Javob")
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    

class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ism")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Xabar")
    phone = models.CharField(max_length=20, verbose_name="Telefon raqami", blank=True, null=True)
    subject = models.CharField(max_length=200, verbose_name="Mavzu", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Block(models.Model):
    key = models.CharField("Blok kaliti", max_length=100, unique=True)
    content = RichTextField("Kontent")

    class Meta:
        verbose_name = "Kontent bloki"
        verbose_name_plural = "Kontent bloklari"

    def __str__(self):
        return self.key
