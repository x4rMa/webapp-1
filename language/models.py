from django.utils import translation
from django.http import HttpResponseRedirect

from wagtail.core.models import Page


class LanguageRedirectionPage(Page):

    def serve(self, request):
        # This will only return a language that is in the LANGUAGES Django setting
        language = translation.get_language_from_request(request)

        return HttpResponseRedirect(self.url + language + '/')

    parent_page_types = ['wagtailcore.Page']
    subpage_types = ['home.HomePage']
