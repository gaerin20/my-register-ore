# Generated by Django 2.2.17 on 2021-04-13 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('regore', '0005_progetto_protocollo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diario0',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('testo', models.TextField()),
                ('link', models.URLField(blank=True, null=True)),
                ('tipo', models.CharField(choices=[('in', 'consegna/ricezione'), ('tr', 'incontro/colloquio/avviso/email/posta'), ('nb', 'sviluppo/nota/promemoria'), ('td', 'todo/da fare')], max_length=100)),
                ('firma', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('progetto', models.ForeignKey(blank=True, default='0', null=True, on_delete=django.db.models.deletion.CASCADE, to='regore.Progetto')),
            ],
            options={
                'verbose_name_plural': 'Diario',
            },
        ),
    ]
