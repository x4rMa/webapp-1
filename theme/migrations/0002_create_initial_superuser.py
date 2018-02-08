from django.db import migrations


def create_superuser(apps, schema_editor):
    User = apps.get_model('auth.user')

    user = User.objects.create(
        username='admin',
        password='pbkdf2_sha256$36000$k5EI3Ee3tQbh$+n17tTaZMuyzd0qKVCiFPC4ntbk2fRgpE6z3F8AwEXk=',
        is_superuser=True,
        is_staff= True,
        is_active= True,
    )


def remove_superuser(apps, schema_editor):
    User = apps.get_model('auth.user')

    User.objects.filter(username='admin').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser, remove_superuser),
    ]
