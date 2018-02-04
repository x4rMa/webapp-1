from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel

from modelcluster.fields import ParentalKey

from language.links import TranslatablePageMixin

from yuan.models import CarouselItem


class HomePageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('HomePage', related_name='carousel_items')


class HomePage(Page, TranslatablePageMixin):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        MultiFieldPanel(TranslatablePageMixin.panels, 'Language links'),
        InlinePanel('carousel_items', label="Carousel items"),
    ]

    parent_page_types = ['language.LanguageRedirectionPage']
    subpage_types = []
