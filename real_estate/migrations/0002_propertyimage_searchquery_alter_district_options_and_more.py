# Generated by Django 4.2.7 on 2025-07-20 18:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_file_id', models.CharField(max_length=200, unique=True)),
                ('file_size', models.PositiveIntegerField(blank=True, null=True)),
                ('width', models.PositiveIntegerField(blank=True, null=True)),
                ('height', models.PositiveIntegerField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('is_main', models.BooleanField(default=False)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Property Image',
                'verbose_name_plural': 'Property Images',
                'ordering': ['order', 'uploaded_at'],
            },
        ),
        migrations.CreateModel(
            name='SearchQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=500)),
                ('search_type', models.CharField(choices=[('keyword', 'Keyword Search'), ('location', 'Location Search'), ('filters', 'Advanced Filters')], max_length=50)),
                ('filters_used', models.JSONField(blank=True, default=dict)),
                ('results_count', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Search Query',
                'verbose_name_plural': 'Search Queries',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'ordering': ['region__order', 'order', 'name_uz'], 'verbose_name': 'District', 'verbose_name_plural': 'Districts'},
        ),
        migrations.AlterModelOptions(
            name='favorite',
            options={'ordering': ['-created_at'], 'verbose_name': 'Favorite', 'verbose_name_plural': 'Favorites'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ['-is_premium', '-created_at'], 'verbose_name': 'Property', 'verbose_name_plural': 'Properties'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['order', 'name_uz'], 'verbose_name': 'Region', 'verbose_name_plural': 'Regions'},
        ),
        migrations.AlterModelOptions(
            name='telegramuser',
            options={'ordering': ['-created_at'], 'verbose_name': 'Telegram User', 'verbose_name_plural': 'Telegram Users'},
        ),
        migrations.AddField(
            model_name='district',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='property',
            name='admin_notes',
            field=models.TextField(blank=True, help_text='Internal admin notes'),
        ),
        migrations.AddField(
            model_name='property',
            name='approval_status',
            field=models.CharField(choices=[('pending', 'На рассмотрении'), ('approved', 'Одобрено'), ('rejected', 'Отклонено')], default='pending', max_length=20),
        ),
        migrations.AddField(
            model_name='property',
            name='channel_message_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='favorites_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='property',
            name='posted_to_channel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='premium_expires_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useractivity',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useractivity',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='real_estate.property'),
        ),
        migrations.AddField(
            model_name='useractivity',
            name='user_agent',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='key',
            field=models.CharField(db_index=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='district',
            name='name_en',
            field=models.CharField(max_length=100, verbose_name='Name (English)'),
        ),
        migrations.AlterField(
            model_name='district',
            name='name_ru',
            field=models.CharField(max_length=100, verbose_name='Name (Russian)'),
        ),
        migrations.AlterField(
            model_name='district',
            name='name_uz',
            field=models.CharField(max_length=100, verbose_name='Name (Uzbek)'),
        ),
        migrations.AlterField(
            model_name='property',
            name='area',
            field=models.DecimalField(decimal_places=2, help_text='Area in m²', max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='property',
            name='condition',
            field=models.CharField(blank=True, choices=[('new', 'Новое'), ('good', 'Хорошее'), ('repair_needed', 'Требует ремонта')], max_length=20),
        ),
        migrations.AlterField(
            model_name='property',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='district',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='is_approved',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='property',
            name='photo_file_ids',
            field=models.JSONField(blank=True, default=list, help_text='Telegram file IDs'),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='property',
            name='region',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='rooms',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='property',
            name='views_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='region',
            name='key',
            field=models.CharField(db_index=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='name_en',
            field=models.CharField(max_length=100, verbose_name='Name (English)'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name_ru',
            field=models.CharField(max_length=100, verbose_name='Name (Russian)'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name_uz',
            field=models.CharField(max_length=100, verbose_name='Name (Uzbek)'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='telegram_id',
            field=models.BigIntegerField(db_index=True, unique=True),
        ),
        migrations.AlterField(
            model_name='useractivity',
            name='action',
            field=models.CharField(choices=[('start', 'Запуск бота'), ('post_listing', 'Размещение объявления'), ('view_listing', 'Просмотр объявления'), ('search', 'Поиск'), ('favorite_add', 'Добавление в избранное'), ('favorite_remove', 'Удаление из избранного'), ('contact', 'Обращение к продавцу'), ('language_change', 'Смена языка'), ('premium_purchase', 'Покупка премиум')], max_length=20),
        ),
        migrations.AlterField(
            model_name='useractivity',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AddIndex(
            model_name='property',
            index=models.Index(fields=['is_approved', 'is_active'], name='real_estate_is_appr_673216_idx'),
        ),
        migrations.AddIndex(
            model_name='property',
            index=models.Index(fields=['property_type', 'status'], name='real_estate_propert_8c72e9_idx'),
        ),
        migrations.AddIndex(
            model_name='property',
            index=models.Index(fields=['region', 'district'], name='real_estate_region_622239_idx'),
        ),
        migrations.AddIndex(
            model_name='property',
            index=models.Index(fields=['-created_at'], name='real_estate_created_b178b6_idx'),
        ),
        migrations.AddIndex(
            model_name='property',
            index=models.Index(fields=['price'], name='real_estate_price_d2712e_idx'),
        ),
        migrations.AddIndex(
            model_name='useractivity',
            index=models.Index(fields=['user', '-created_at'], name='real_estate_user_id_b158a8_idx'),
        ),
        migrations.AddIndex(
            model_name='useractivity',
            index=models.Index(fields=['action', '-created_at'], name='real_estate_action_4fc2f4_idx'),
        ),
        migrations.AddField(
            model_name='searchquery',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='searches', to='real_estate.telegramuser'),
        ),
        migrations.AddField(
            model_name='propertyimage',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='real_estate.property'),
        ),
    ]
