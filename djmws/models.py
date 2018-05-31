from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


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


class MWSCredentials(models.Model):
    user = models.ForeignKey(User, models.CASCADE,
                             related_name='mws_credentials')
    region = models.ForeignKey(Region, models.PROTECT)
    seller_id = models.CharField(max_length=32, verbose_name='Seller ID')
    access_key = models.CharField(max_length=32)
    secret_key = models.CharField(max_length=64)

    class Meta(object):
        verbose_name = 'MWS Credentials'
        verbose_name_plural = 'MWS Credentials'
        unique_together = (
            ('user', 'region', )
        )

    def get_api(self, API, marketplace_code):
        # assert issubclass(API, MWS) and type(marketplace) is Marketplace
        return API(
            region=marketplace_code,
            domain=self.region.endpoint,
            access_key=self.access_key,
            secret_key=self.secret_key,
            account_id=self.seller_id,
        )

    def __str__(self):
        return 'Credentials for {} ({})'.format(self.user, self.region)
