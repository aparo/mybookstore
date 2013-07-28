from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

    class Meta:
        unique_together = [("name", "surname")]
        ordering = ["name", "surname"]
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    def __unicode__(self):
        return u'%s %s' % (self.name, self.surname)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


    def __unicode__(self):
        return u'%s' % self.name


class Book(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(default=””, blank=True, null=True)
    release = models.DateField(auto_now_add=True)
    in_stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    price = models.FloatField(default=0.0)
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    class Meta:
        ordering = ["title", "author"]
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __unicode__(self):
        return _(u'%s of %s' % (self.title, self.author))

