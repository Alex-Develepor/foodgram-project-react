from rest_framework.pagination import PageNumberPagination


class PageLimit(PageNumberPagination):
    page_size = 6
    page_size_query_description = 'limit'
