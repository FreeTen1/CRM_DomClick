from django.db import models


class Client(models.Model):
    """Клиенты."""
    name = models.CharField(max_length=255, default='clientname')
    last_name = models.CharField(max_length=255, default='clientlastname')
    email = models.EmailField(null=True)

    def __str__(self):
        return f'Клиент - {self.name} {self.last_name}'


class Worker(models.Model):
    """Работники."""
    name = models.CharField(max_length=255, default='workername')
    last_name = models.CharField(max_length=255, default='workerlastname')
    email = models.EmailField(null=True)
    position = models.TextField()

    def __str__(self):
        return f'Работник - {self.name} {self.last_name}, должность - {self.position}'


class Query(models.Model):
    """Заявки."""

    # Типы заявок
    repair = 'RE'
    service = 'SE'
    consultation = 'CO'

    FIELD_TYPE = [
        (repair, 'Ремонт'),
        (service, 'Обслуживание'),
        (consultation, 'Консультация')
    ]

    # Типы статусов
    open = 'OP'
    in_work = 'IW'
    close = 'CL'

    FIELD_STATUS = [
        (open, 'Открыта'),
        (in_work, 'В работе'),
        (close, 'Закрыта')
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=FIELD_TYPE)
    query_date_creation = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=FIELD_STATUS)

    def __str__(self):
        return f'Заявка №{self.id}, клиент - {self.client}'
