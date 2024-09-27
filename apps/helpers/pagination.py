from rest_framework.pagination import PageNumberPagination

class PropertyResultsPagination(PageNumberPagination):
    page_size = 10