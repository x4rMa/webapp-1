from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet


class CarouselItem(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    caption_head = models.CharField(max_length=255, blank=True)
    caption_paragraph = models.CharField(max_length=255, blank=True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption_head'),
        FieldPanel('caption_paragraph'),
    ]

    class Meta:
        abstract = True


@register_snippet
class Content(models.Model):
    content_type = models.CharField(max_length=32)
    content_body = models.CharField(max_length=255)

    panels = [
        FieldPanel('content_type'),
        FieldPanel('content_body'),
    ]

    def __str__(self):
        return self.content_type

    class Meta:
        verbose_name_plural = 'Content'
