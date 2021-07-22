from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    """Клиенты."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Клиент - {self.user.username}'


class Worker(models.Model):
    """Работники."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.TextField(null=False, blank=False)

    def __str__(self):
        return f'Работник - {self.user.username}, должность - {self.position}'


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
        return f'Заявка №{self.id}, клиент - {self.client.user.username}'
