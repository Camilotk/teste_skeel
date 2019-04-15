from rest_framework import pagination
 
class VacancyPaginator(pagination.PageNumberPagination):
    page_size = 8
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 8

class CompanyPaginator(pagination.PageNumberPagination):
    page_size = 5
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 9
