from django.db import models


class RegionManager(models.Manager):
    def get_by_natural_key(self, code):
        return self.get(code=code)


class Region(models.Model):
    objects = RegionManager()

    code = models.CharField(unique=True, max_length=2)
    endpoint = models.URLField()

    def __str__(self):
        return self.code


class MarketplaceManager(models.Manager):
    def get_by_natural_key(self, amazon_id):
        return self.get(amazon_id=amazon_id)


class Marketplace(models.Model):
    objects = MarketplaceManager()

    amazon_id = models.CharField(unique=True, max_length=16,
                                 verbose_name='Amazon ID')
    region = models.ForeignKey(Region, models.PROTECT)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.code
