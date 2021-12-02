import django_filters
from accounts.models import Member
from django_filters import DateFilter, CharFilter


class MemberFlilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name='created', lookup_expr='gte')
    # end_date = DateFilter(field_name='created', lookup_expr='lte')
    firstname_search = CharFilter(field_name='first_name',
                                  lookup_expr='icontains')
    lastname_search = CharFilter(field_name='last_name',
                                 lookup_expr='icontains')

    # membership_search = CharFilter(field_name='membership_no')

    class Meta:
        model = Member
        fields = ['status']


class Member_id_no(django_filters.FilterSet):
    # start_date = DateFilter(field_name='created', lookup_expr='gte')
    # end_date = DateFilter(field_name='created', lookup_expr='lte')
    membership_no = CharFilter(field_name='id_number', lookup_expr='icontains')

    class Meta:
        model = Member
        fields = ['id_number']