from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(max_length=32)),
                ('content_body', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Content',
            },
        ),
    ]
