from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from PIL import Image
# Create your models here.
class allhomeworks(models.Model):
    title = models.CharField(verbose_name=_("homework title"), max_length=50)
    date = models.DateTimeField(auto_now_add=True , auto_now=False)
    desc = models.TextField(verbose_name=_("Description"))
    image = models.ImageField(default='default.jpg')
    img1 = models.ImageField(_("exercice"), null=True)
    img2 = models.ImageField(_("solution"), null=True)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        width, height = img.size  # Get dimensions

        if width > 300 and height > 300:
            # keep ratio but shrink down
            img.thumbnail((width, height))

        # check which one is smaller
        if height < width:
            # make square by cutting off equal amounts left and right
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))

        elif width < height:
            # make square by cutting off bottom
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))

        if width > 300 and height > 300:
            img.thumbnail((300, 300))

        img.save(self.image.path)
    class Meta:
        verbose_name = _("homework")



