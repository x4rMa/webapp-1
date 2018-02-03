from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import MultiFieldPanel, PageChooserPanel


class TranslatablePageMixin(models.Model):
    language_link = models.ForeignKey(Page, null=True, on_delete=models.SET_NULL, blank=True, related_name='+')

    panels = [
        PageChooserPanel('language_link'),
    ]

    def get_language(self):
        language_homepage = self.get_ancestors(inclusive=True).get(depth=3)

        return language_homepage.slug


    def language_page(self):
        language = self.get_language()
        return type(self).objects.filter(language_link=self).first()


    class Meta:
        abstract = True
