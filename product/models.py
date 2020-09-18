from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField("Категорія", max_length=255)
    slug = models.SlugField("Псевдонім", max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Color(models.Model):
    name = models.CharField("Колір", max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Колір"
        verbose_name_plural = "Кольора"

class Size(models.Model):
    name = models.CharField("Розмір", max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Розмір"
        verbose_name_plural = "Розміри"


class Action(models.Model):
    name = models.CharField("Назва акції", max_length=20)
    color = models.CharField("Колір", max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Акція"
        verbose_name_plural = "Акції"

class Brand(models.Model):
    name = models.CharField("Бренд", max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренди"

class Tag(models.Model):
    name = models.CharField("Тег", max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

class Product(models.Model):
    name = models.CharField("Продукт", max_length=255)
    slug = models.SlugField("Псевдонім", max_length=255)
    price = models.PositiveIntegerField("Ціна", default=0)
    product_code = models.CharField("Код продукту", max_length=20)
    shipping_tax = models.PositiveSmallIntegerField("Податок за доставку", default=0)
    description = models.TextField("Опис")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag, blank=True)
    public = models.BooleanField("Публікація", default=True)
    created_at = models.DateTimeField("Дата створення", auto_now_add=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    def get_price_discount(self):
        discount = self.productaction_set.filter(product_id=self.id).exclude(value=0).first()
        if discount:
            price = self.price - self.price * discount.value / 100
        else:
            price = self.price
        return price

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"


class ProductAction(models.Model):
    value = models.PositiveIntegerField("Значення", default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Акція продукта"
        verbose_name_plural = "Акції продуктів"


class Quantity(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Кількість", default=0)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Кількість"
        verbose_name_plural = "Кількості"


class Image(models.Model):
    name = models.ImageField("Назва", upload_to="img/")
    root = models.BooleanField("Головне фото", default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Фотографія"
        verbose_name_plural = "Фотографії"


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField("Значення зірок", default=0)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Рейтингава зірка"
        verbose_name_plural = "Рейтингові зірки"
        ordering = ["-value"]

class Rating(models.Model):
    ip = models.CharField("IP адреса", max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

class SocialNetwork(models.Model):
    name = models.CharField("Назва", max_length=40)
    url = models.CharField("URL силка", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Соціальна мережа"
        verbose_name_plural = "Соціальні мережі"


class Reviews(models.Model):
    """Отзиви"""
    email = models.EmailField("Email")
    name = models.CharField("І'мя", max_length=100)
    text = models.TextField("Повідомлення", max_length=5000)
    created_at = models.DateTimeField("Дата створення", auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Отзив"
        verbose_name_plural = "Отзиви"

