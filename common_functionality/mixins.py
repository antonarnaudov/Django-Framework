class SerializerRequestSwitchMixin(object):
    """
    serializers = {
        'show': ShowSerializer,
        'create': CreateSerializer,
        'update': UpdateSerializer,
        'detailed': RetrieveSerializer
    }
    """

    serializers = {}

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            if 'detailed' in self.serializers.keys():
                return self.serializers['detailed']

            return self.serializers['show']

        elif self.action == 'update':
            return self.serializers['update']

        return self.serializers['create']
