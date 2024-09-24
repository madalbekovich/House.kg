
class HierarchicalMixin:
    
    def base_method(self, instance):
        """ Method to get child objects """
        queryset = instance.get_children()
        if queryset.exists():
            return self.__class__(queryset, many=True).data
        return "empty ㋡"