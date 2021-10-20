# Generated by Django 3.2.8 on 2021-10-19 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ecole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ecole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecole.ecole')),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('classe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecole.classe')),
                ('ecole', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecole.ecole')),
                ('niveau', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecole.niveau')),
            ],
        ),
        migrations.AddField(
            model_name='classe',
            name='niveau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecole.niveau'),
        ),
    ]
