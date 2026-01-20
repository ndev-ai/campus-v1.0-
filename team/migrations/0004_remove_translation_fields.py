# Generated migration to remove translation fields

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_add_translation_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teammember',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='name_uz',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='role_en',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='role_uz',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='role_ru',
        ),
    ]
