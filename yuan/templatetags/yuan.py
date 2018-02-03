from django import template

from wagtail.wagtailcore.models import Page

from yuan.models import Content

register = template.Library()
# https://docs.djangoproject.com/en/1.9/howto/custom-template-tags/


@register.assignment_tag(takes_context=True)
def get_language_root(context):
    return context['self'].get_ancestors(inclusive=True).get(depth=3)


@register.inclusion_tag('yuan/tags/top_menu.html')
def top_menu(parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)
    return {
        'menuitems': menuitems,
    }


@register.inclusion_tag('yuan/tags/language_menu.html')
def language_menu(calling_page=None):
    page_language = calling_page.get_language()
    if calling_page.english_page() and page_language != 'en':
        language_url = calling_page.english_page().url
        language_translation = 'English'
    elif calling_page.turkish_page() and page_language != 'tr':
        language_url = calling_page.turkish_page().url
        language_translation = 'Turkish'
    else:
        language_url = None
        language_translation = None

    return {
        'language_url': language_url,
        'language_translation': language_translation,
    }


@register.inclusion_tag('yuan/tags/footer_text.html')
def footer_text():
    try:
        return {
            'footer_text': Content.objects.get(content_type__iexact="footer text").content_body,
        }
    except:
        return {
            'footer_text': '',
        }
