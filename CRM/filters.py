import django_filters
from django_filters import FilterSet, DateFilter

from CRM.models import Query


class QueriesFilter(FilterSet):
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

    type = django_filters.ChoiceFilter(label='Тип', choices=FIELD_TYPE)
    status = django_filters.ChoiceFilter(label='Статус', choices=FIELD_STATUS)
    query_date_creation = django_filters.IsoDateTimeFromToRangeFilter(label='Промежуток даты и времени')
