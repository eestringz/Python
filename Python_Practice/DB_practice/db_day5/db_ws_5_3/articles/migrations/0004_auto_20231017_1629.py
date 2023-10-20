# Generated by Django 3.2.7 on 2023-10-17 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_comment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='hashtags',
            field=models.ManyToManyField(blank=True, to='articles.Hashtag'),
        ),
    ]
