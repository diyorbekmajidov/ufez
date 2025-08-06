from django.db import models
from ckeditor.fields import RichTextField

class Menu(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    page = models.ForeignKey("Page", null=True, blank=True, on_delete=models.CASCADE)
    url = models.URLField(blank=True, null=True)
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
            return self.page.get_absolute_url()
        elif self.url:
            return self.url
        else:
            return f'/{self.slug}/'

    def has_children(self):
        return self.children.filter(is_active=True).exists()

        
    def has_children(self):
        return self.children.filter(is_active=True).exists()


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
        return f'/{self.slug}/'
    
    def __str__(self):
        return self.title
    

class News(models.Model):
    title = models.CharField("Yangilik sarlavhasi", max_length=200)
    slug = models.SlugField("Slug (URL uchun)", unique=True)
    body = RichTextField("Matn")
    image = models.ImageField("Rasm", upload_to='news/')
    created_at = models.DateTimeField("Yaratilgan vaqt", auto_now_add=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

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
