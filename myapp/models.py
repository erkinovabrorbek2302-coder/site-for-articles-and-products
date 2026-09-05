from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MinValueValidator

# Create your models here.
class Maqola(models.Model):
    nom = models.CharField(max_length=100, verbose_name='Nomi')
    muallifi = models.CharField(max_length=100, verbose_name='Muallifi')
    sarlavha = models.CharField(max_length=100, verbose_name='Sarlavha')
    tavsif = models.TextField(verbose_name='Mahsulot')
    slug = models.SlugField(max_length=100, verbose_name='Slug', unique=True,blank=True)
    holat_tanlash = [
        ('chop_etilmagan', 'Chop Etilmagan'),
        ('chop_etilgan', 'Chop Etilgan'),
    ]
    holat = models.CharField(max_length=20, choices=holat_tanlash, verbose_name='Holat', default='chop_etilgan')
    yaratilgan = models.DateTimeField(verbose_name='Yaratilgan', auto_now_add=True)
    yangilangan = models.DateTimeField(verbose_name='Yangilangan', auto_now=True)
    def get_absolute_url(self):
        return reverse('maqola_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nom}-{self.muallifi}"

    class Meta:
        db_table = 'maqola'
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'
        ordering = ['-yangilangan']


class Mahsulot(models.Model):
    nom = models.CharField(max_length=100,verbose_name='Nom')
    surat = models.ImageField(upload_to='mahsulot', verbose_name='Surat',null=True,blank=True)
    slug = models.SlugField(unique=True, blank=True,verbose_name='Slug')
    tavsif = models.TextField(verbose_name='Tavsif')
    narx = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], verbose_name='Narx')
    miqdor = models.PositiveIntegerField(default=0, verbose_name='Miqdor')
    brend = models.CharField(max_length=100, blank=True, null=True,default='Brend nomi qoyilmagan.', verbose_name='Brend')
    ishlab_chiqarilgan = models.CharField(max_length=100, blank=True, null=True,default="o'zbekiston", verbose_name='Ishlab chiqarilgan')
    yaroqlilik = models.CharField(max_length=50, blank=True, null=True,default='12 oy',verbose_name='Yaroqlilik')  # "12 oy"
    tarkibi = models.TextField(blank=True, null=True,verbose_name='Tarkibi',default='Tarkibi qoyilmagan.')
    holat_berilgan = [
        ('mavjud_emas', 'Mavjud emas'),
        ('majud', 'Mavjud'),
    ]
    holat = models.CharField(max_length=20, default='mavjud',verbose_name='Holat')
    yaratilgan = models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan')
    yangilangan = models.DateTimeField(auto_now=True, verbose_name='Yangilangan')

    def __str__(self):
        return f"{self.nom} - {self.narx}"

    def get_absolute_url(self):
        return reverse('mahsulot_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'mahsulotlar'
        ordering = ['-yaratilgan']
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'