# Generated by Django 4.1.7 on 2023-02-26 08:04

from django.db import migrations, models
import django.db.models.deletion
import rest_framework_simple_api_key.models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='OrganizationAPIKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('expiry_date', models.DateTimeField(default=rest_framework_simple_api_key.models._expiry_date, help_text='Once API key expires, entities cannot use it anymore.', verbose_name='Expires')),
                ('revoked', models.BooleanField(blank=True, default=False, help_text='If the API key is revoked, entities cannot use it anymore. (This cannot be undone.)')),
                ('created', models.DateTimeField(auto_now=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='api_keys', to='organization.organization')),
            ],
            options={
                'verbose_name': 'API key',
                'verbose_name_plural': 'API keys',
                'abstract': False,
            },
        ),
    ]