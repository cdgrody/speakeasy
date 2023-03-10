# Generated by Django 4.1.6 on 2023-02-16 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='flag',
            field=models.CharField(choices=[('United States', '🇺🇸'), ('Canada', '🇨🇦'), ('Mexico', '🇲🇽'), ('Brazil', '🇧🇷'), ('Argentina', '🇦🇷'), ('France', '🇫🇷'), ('Germany', '🇩🇪'), ('Italy', '🇮🇹'), ('Spain', '🇪🇸'), ('China', '🇨🇳'), ('Japan', '🇯🇵'), ('South Korea', '🇰🇷'), ('India', '🇮🇳'), ('Australia', '🇦🇺'), ('New Zealand', '🇳🇿')], default='Mexico', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='primary_language',
            field=models.CharField(choices=[('ZH', '中文'), ('ES', 'Español'), ('EN', 'English'), ('HI', 'हिन्दी-उर्दू'), ('AR', 'العربية'), ('BN', 'বাংলা'), ('PT', 'Português'), ('RU', 'Русский'), ('FR', 'Français'), ('HE', 'עברית')], default='EN', max_length=20),
        ),
    ]
