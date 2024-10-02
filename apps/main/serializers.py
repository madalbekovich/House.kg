from rest_framework import serializers
from apps.main import models
from apps.house import mixins

class CommentSerializer(serializers.ModelSerializer):
    content = serializers.CharField(required=True)
    model = serializers.CharField()
    object_id = serializers.CharField()
    parent = serializers.IntegerField(required=False)    
    class Meta:
        model = models.Comments
        fields = ['content', 'parent', 'model', 'object_id']

    def create(self, validated_data):
        model_name = validated_data.pop('model')
        object_id = validated_data.pop('object_id', None)
        parent = validated_data.pop('parent', None)
        try:
            content_type = models.ContentType.objects.get(model=model_name.lower())
            comment, created =models.Comments.objects.get_or_create(
                user=self.context['request'].user,
                content_type=content_type,
                object_id=object_id,
                content=validated_data['content'],
                parent=parent,
            )
        except models.ContentType.DoesNotExist:
            raise serializers.ValidationError({"model": "Invalid model name!"})
        return comment


class CommentListSerializer(serializers.ModelSerializer, mixins.HierarchicalMixin):
    subcomment = serializers.SerializerMethodField()

    class Meta:
        model = models.Comments
        fields = ['id', 'content_type', 'object_id',  'parent', 'content', 'subcomment']
    
    def get_subcomment(self, instance):
        return super().base_method(instance)