from rest_framework import pagination

class RestAPIPagination(pagination.PageNumberPagination):
    page_size = 5