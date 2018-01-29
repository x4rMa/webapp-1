from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel

from language.links import TranslatablePageMixin


class HomePage(Page, TranslatablePageMixin):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        MultiFieldPanel(TranslatablePageMixin.panels, 'Language links'),
    ]

    parent_page_types = ['language.LanguageRedirectionPage']
    subpage_types = []
