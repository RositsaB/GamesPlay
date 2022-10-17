from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    AGE_MIN_VALUE = 12
    PASSWORD_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    email = models.EmailField()

    age = models.IntegerField(
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        )
    )
    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=FIRST_NAME_MAX_LEN,
    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=LAST_NAME_MAX_LEN,
    )

    picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Game(models.Model):
    TITLE_MAX_LEN = 30
    CATEGORY_MAX_LEN = 15
    CATEGORY = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other'),
    )
    RATING_MAX_LEN = 5.0
    RATING_MIN_LEN = 0.1
    MAX_LEVEL_MIN_VALUE = 1

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        unique=True,
    )

    category = models.CharField(
        max_length=CATEGORY_MAX_LEN,
        choices=CATEGORY,
    )

    rating = models.FloatField(
        validators=(
            MinValueValidator(RATING_MIN_LEN),
            MaxValueValidator(RATING_MAX_LEN),
        )
    )

    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(MAX_LEVEL_MIN_VALUE),
        )
    )

    image = models.URLField()

    summary = models.TextField(
        null=True,
        blank=True,
    )
