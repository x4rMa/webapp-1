from django.db import migrations


def create_content(apps, schema_editor):
    Content = apps.get_model('theme.content')

    content = Content.objects.create(
        content_type='footer text',
        content_body='© 2017-2018 Company, Inc.',
    )


def remove_content(apps, schema_editor):
    Content = apps.get_model('theme.content')

    Content.objects.filter(content_type='footer_text').delete()

class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0002_create_initial_superuser'),
    ]

    operations = [
        migrations.RunPython(create_content, remove_content),
    ]
