from django.db import models
from core.settings import MEDIA_URL

class Device(models.Model):
    title = models.CharField(
		verbose_name ="Название",
        max_length=50)

    address = models.CharField(
		verbose_name ="Адресс",
        max_length=50)

    port = models.CharField(
		verbose_name ="Порт",
        max_length=10,
        null=True,
        blank=True)

    login = models.CharField(
		verbose_name ="Логин",
        max_length=50)

    password = models.CharField(
		verbose_name ="Пароль",
        max_length=50)

    status = models.CharField(
	    choices=[
		    ('online', 'онлайн'),
		    ('offline', 'не активен'),
		    ('undefined', 'не определено')
		],
		verbose_name ="Статус",
        max_length=50,
	    default = 'undefined',
	)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"

class Group(models.Model):
    name = models.CharField(
		verbose_name ="Название",
        max_length=100)
    
    # template = models.TextField(
    #     choices=[
	# 	    ('all_day_authorized', 'авторизован на весь день'),
	# 	    ('all_day_denied', 'откланено на весь день')
	# 	],
	# 	verbose_name ="доступ",
    #     max_length=100,
	#     default = 'undefined')
    
    # people_number = models.IntegerField(verbose_name ="Число людей", blank=True, null=True)
    
    # status = models.CharField(
	#     choices=[
	# 	    ('all_applied', 'все изменения загружены'),
	# 	    ('not_applied', 'изменения не загружены'),
	# 	    ('error_catched', 'ошыбка загрузки')
	# 	],
	# 	verbose_name ="Сохранение изменений",
    #     max_length=50,
	#     default = 'undefined')

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

class Person(models.Model):
    status_choices = (
        (True,'Активен'),
        (False,'Заблоктрован')
    )

    group = models.ForeignKey(
        verbose_name ="Группа",
        to=Group,
        on_delete=models.PROTECT,
        default=1)

    name = models.CharField(
		verbose_name ="Имя",
        max_length=50,)

    photo = models.ImageField(
        upload_to = MEDIA_URL,
        null=True,
        default=False)

    active = models.BooleanField(
		verbose_name ="Статус активности",
        max_length=10,
        default=True,
        choices=status_choices)
    
    time = models.DateTimeField(auto_now=True)

    def photo_tag(self):
        from django.utils.safestring import mark_safe
        return mark_safe('<img src="{}" width="100" />'.format(self.photo.url))

    photo_tag.short_description = 'Фото'
    photo_tag.allow_tags = True

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Event(models.Model):
    source = models.CharField(
		verbose_name ="Источник-устройство",
        max_length=100)

    details = models.TextField(
		verbose_name = "Подробности",
        blank = True)

    type = models.TextField(
		verbose_name ="Тип Уведомления")

    address = models.CharField(
		verbose_name ="Адресс",
        max_length=50,
        null=True,
        blank=True)

    time = models.DateTimeField(            
        verbose_name ="Время",
        auto_now=True)

    def __str__(self):
        return f'{self.type}'
    
    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

