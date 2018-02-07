from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import (
    InlinePanel, MultiFieldPanel, StreamFieldPanel
)

from modelcluster.fields import ParentalKey

from language.links import TranslatablePageMixin

from yuan.models import CarouselItem

from yuan.blocks import BaseStreamBlock


class HomePageCarouselItem(Orderable, CarouselItem):
    carousel = ParentalKey('HomePage', related_name='carousel_items')


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
