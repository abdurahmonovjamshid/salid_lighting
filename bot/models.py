from django.db import models


class TgUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15, default='-')

    is_bot = models.BooleanField(default=False)
    language_code = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Joined')

    step = models.IntegerField(default=0)

    deleted = models.BooleanField(default=False)

    def __str__(self):
        if self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return f'{self.first_name}'


class Car(models.Model):
    owner = models.ForeignKey(TgUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    year = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    region = models.ForeignKey(
        "Region", on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(
        "District", on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    contact_number = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    complate = models.BooleanField(default=False)
    post = models.BooleanField(default=False)

    seen = models.ManyToManyField(TgUser, related_name='seen_cars')
    likes = models.ManyToManyField(TgUser, related_name='liked_cars')
    dislikes = models.ManyToManyField(TgUser, related_name='disliked_cars')

    delete = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} {self.model} ({self.year})"

    # @property
    # def seen_count(self):
    #     return self.seen.count()


class CarImage(models.Model):
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE, related_name='images')
    image_link = models.CharField(max_length=100)

    telegraph = models.URLField(
        default='https://telegra.ph/file/6529587f8e3bd7a9b0c56.jpg')

    def __str__(self):
        return f"Image for {self.car.name} {self.car.model} ({self.car.year})"


class Search(models.Model):
    text = models.CharField(max_length=250)
    user = models.ForeignKey(TgUser, on_delete=models.CASCADE)
    currnet_page = models.IntegerField(default=1)

    complate = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Region(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
