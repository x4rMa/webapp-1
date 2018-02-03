from django.db import migrations


def create_homepage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model('contenttypes.ContentType')
    HomePage = apps.get_model('home.HomePage')
    LanguageRedirectionPage = apps.get_model('language.LanguageRedirectionPage')

    # Create content type for homepage model
    homepage_content_type, __ = ContentType.objects.get_or_create(
        model='homepage', app_label='home')

    # Create a new Turkish homepage
    homepage_tr = HomePage.objects.create(
        title="Ana Sayfa",
        draft_title="Ana Sayfa",
        slug='tr',
        content_type=homepage_content_type,
        path='000100010001',
        depth=3,
        numchild=0,
        url_path='/tr/',
        show_in_menus=1,
    )

    # Create a new English homepage
    homepage_en = HomePage.objects.create(
        title="Home",
        draft_title="Home",
        slug='en',
        content_type=homepage_content_type,
        path='000100010002',
        depth=3,
        numchild=0,
        url_path='/en/',
        show_in_menus=1,
    )

    LanguageRedirectionPage.objects.filter(title='Language Redirection Page').update(numchild=2)


def remove_homepage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model('contenttypes.ContentType')
    HomePage = apps.get_model('home.HomePage')
    LanguageRedirectionPage = apps.get_model('language.LanguageRedirectionPage')

    # Delete the default homepage
    # Page and Site objects CASCADE
    HomePage.objects.all.delete()

    # Delete content type for homepage model
    ContentType.objects.filter(model='homepage', app_label='home').delete()

    LanguageRedirectionPage.objects.filter(title='Language Redirection Page').update(numchild=0)


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('language', '0002_create_languageredirectionpage'),
    ]

    operations = [
        migrations.RunPython(create_homepage, remove_homepage),
    ]
