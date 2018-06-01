from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse

from .models import Marketplace, MWSCredentials


class MWSMixin(LoginRequiredMixin):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.marketplace = None
        self.mws_credentials = None

    def dispatch(self, request, *args, **kwargs):
        if isinstance(request.user, AnonymousUser):
            return HttpResponse(status=403)
        self.marketplace = \
            Marketplace.objects.get(
                code=request.GET.get(
                    'marketplace', settings.DEFAULT_MARKETPLACE,
                )
            )
        try:
            self.mws_credentials = MWSCredentials.objects.get(
                region=self.marketplace.region,
                user=request.user,
            )
        except MWSCredentials.DoesNotExist:
            return HttpResponse(status=401)
        return super().dispatch(request, *args, **kwargs)
