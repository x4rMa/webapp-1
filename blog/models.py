from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from language.links import TranslatablePageMixin


class BlogPage(Page, TranslatablePageMixin):
    body = RichTextField()
    date = models.DateField("Post date")
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
        ImageChooserPanel('feed_image'),
    ]

    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []


class BlogIndexPage(Page, TranslatablePageMixin):
    parent_page_types = ['home.HomePage']
    subpage_types = ['blog.BlogPage']

    content_panels = Page.content_panels + [
        PageChooserPanel('language_link'),
    ]
