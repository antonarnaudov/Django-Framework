from rest_framework.pagination import CursorPagination, LimitOffsetPagination


class CursorPaginationSettings(CursorPagination):
    page_size = 1


class LimitOffsetPaginationSettings(LimitOffsetPagination):
    default_limit = 1
    max_limit = 100
