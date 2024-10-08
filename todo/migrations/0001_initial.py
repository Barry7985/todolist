# Generated by Django 5.1 on 2024-09-03 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('priority', models.CharField(choices=[('faible', 'Faible'), ('moyen', 'Moyen'), ('elevé', 'Elevé')], max_length=10)),
                ('completed', models.BooleanField(default=False)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
