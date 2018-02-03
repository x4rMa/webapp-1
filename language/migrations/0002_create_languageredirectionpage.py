from django.db import migrations


def create_languageredirectionpage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model('contenttypes.ContentType')
    Page = apps.get_model('wagtailcore.Page')
    Site = apps.get_model('wagtailcore.Site')
    LanguageRedirectionPagePage = apps.get_model('language.LanguageRedirectionPage')

    # Delete the default homepage
    # If migration is run multiple times, it may have already been deleted
    Page.objects.filter(id=2).delete()

    # Create content type for languageredirectionpage model
    languageredirectionpage_content_type, __ = ContentType.objects.get_or_create(
        model='languageredirectionpage', app_label='language'
    )

    # Create a new languageredirectionpage
    languageredirectionpage = LanguageRedirectionPagePage.objects.create(
        title='Language Redirection Page',
        draft_title="Language Redirection Page",
        slug='language-redirection-page',
        content_type=languageredirectionpage_content_type,
        path='00010001',
        depth=2,
        numchild=0,
        url_path='/language-redirection-page/',
    )

    # Create a site with the new languageredirectionpage set as the root
    Site.objects.create(
        hostname='localhost',
        root_page=languageredirectionpage,
        is_default_site=True,
    )


def remove_languageredirectionpage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model('contenttypes.ContentType')
    LanguageRedirectionPagePage = apps.get_model('language.LanguageRedirectionPagePage')

    # Delete the default languageredirectionpage
    # Page and Site objects CASCADE
    LanguageRedirectionPagePage.objects.filter(slug='language-redirection-page', depth=2).delete()

    # Delete content type for languageredirectionpage model
    ContentType.objects.filter(model='languageredirectionpage', app_label='language').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_languageredirectionpage, remove_languageredirectionpage),
    ]
