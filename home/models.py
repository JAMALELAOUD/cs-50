from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class allhomeworks(models.Model):
    title = models.CharField(verbose_name=_("homework title"), max_length=50)
    date = models.DateTimeField(auto_now_add=True , auto_now=False)
    desc = models.TextField(verbose_name=_("Description"))
    img = models.ImageField()
    img1 = models.ImageField(_("exercice"), null=True)
    img2 = models.ImageField(_("solution"), null=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = _("homework")



