from django.db import models

from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import (
    InlinePanel, MultiFieldPanel, StreamFieldPanel
)

from modelcluster.fields import ParentalKey

from language.links import TranslatablePageMixin

from theme.models import CarouselItem

from theme.blocks import BaseStreamBlock


class HomePageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey(
        'HomePage', on_delete=models.CASCADE,related_name='carousel_items'
        )


class HomePage(Page, TranslatablePageMixin):
    body = StreamField(
        BaseStreamBlock(), verbose_name="Page body", blank=True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(TranslatablePageMixin.panels, 'Language links'),
        StreamFieldPanel('body'),
        InlinePanel('carousel_items', label="Carousel items"),
    ]

    parent_page_types = ['language.LanguageRedirectionPage']
    subpage_types = []
