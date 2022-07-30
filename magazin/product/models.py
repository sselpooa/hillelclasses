from django.db import models


class Product(models.Model):
    DEFAULT_FORMAT = 'choose_the_format'
    FORMAT_CHOICES = (
        (DEFAULT_FORMAT, 'Choose the format'),
        ('cd', 'CD'),
        ('lp', 'LP'),
        ('digital', 'Digital'),
        ('casette', 'Casette')
    )
    NONDEF_CHOICE = 'non defined'
    GENRE_CHOICES = (
        (NONDEF_CHOICE, 'Non defined'),
        ('rock', 'Rock'),
        ('synth_wave', 'Synth wave'),
        ('post_punk','Post punk'),
        ('heavy_metal','Heavy metal')
    )
    UNS_STATUS = "unseen"
    PRODUCT_STATUSES = (
        (UNS_STATUS, 'Unseen'),
        ('recntly_seen', 'Recently seen'),
        ('ad_in_cart', 'Add in cart')
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    description = models.TextField()
    performer = models.CharField(max_length=50,default='Artist')
    image = models.ImageField(upload_to='images/')
    updated_at = models.DateTimeField(auto_now=True)
    format = models.CharField(
        max_length=40,
        choices=FORMAT_CHOICES,
        default=DEFAULT_FORMAT,
    )
    status = models.CharField(
        max_length=40,
        choices=PRODUCT_STATUSES,
        default=UNS_STATUS,
    )
    genre = models.CharField(
        max_length=255,
        choices=GENRE_CHOICES,
        default=NONDEF_CHOICE
    )
    song_list = models.TextField(default='Not Mentioned')
    created_at = models.DateTimeField(auto_now_add=True)
    in_stock = models.BooleanField(default=True)




    def __str__(self):
        return f'{self.id}-{self.title}-{self.performer}'



