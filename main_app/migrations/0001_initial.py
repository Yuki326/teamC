# Generated by Django 3.2.9 on 2021-11-21 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question_radio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question_text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Answer_text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='作成日')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.question_text')),
            ],
        ),
        migrations.CreateModel(
            name='Answer_radio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, choices=[(1, 'とても悪い'), (2, '悪い'), (3, '普通'), (4, 'まあまあ'), (5, 'とても良い')], verbose_name='種類名')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='作成日')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.question_radio')),
            ],
        ),
    ]
