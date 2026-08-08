# projects/serializers.py
from rest_framework import serializers
from .models import ProjectSection, ProjectCard

class ProjectCardSerializer(serializers.ModelSerializer):
    points_list = serializers.SerializerMethodField()
    technologies_list = serializers.SerializerMethodField()
    key_results_list = serializers.SerializerMethodField()
    
    class Meta:
        model = ProjectCard
        fields = [
            'id',
            'number',
            'heading',
            'description',
            'icon',
            'image',
            'points',
            'points_list',
            'technologies',
            'technologies_list',
            'key_results',
            'key_results_list',
            'order',
            'is_active',
            'created_at',
            'updated_at'
        ]
    
    def get_points_list(self, obj):
        return obj.get_points_list()
    
    def get_technologies_list(self, obj):
        return obj.get_technologies_list()
    
    def get_key_results_list(self, obj):
        return obj.get_key_results_list()

class ProjectSectionSerializer(serializers.ModelSerializer):
    projects = ProjectCardSerializer(many=True, read_only=True)
    
    class Meta:
        model = ProjectSection
        fields = ['id', 'heading', 'description', 'is_active', 'projects', 'created_at', 'updated_at']