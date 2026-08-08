# about/serializers.py
from rest_framework import serializers
from .models import AboutSection, TeamMember, Publication, Patent, AboutStat

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = [
            'id',
            'name',
            'designation',
            'role',
            'description',
            'image',
            'linkedin',
            'github',
            'twitter',
            'website',
            'order',
            'is_active',
            'created_at',
            'updated_at'
        ]

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = [
            'id',
            'title',
            'authors',
            'journal',
            'year',
            'link',
            'citation',
            'order',
            'is_active',
            'created_at',
            'updated_at'
        ]

class PatentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patent
        fields = [
            'id',
            'title',
            'patent_number',
            'inventors',
            'year',
            'link',
            'order',
            'is_active',
            'created_at',
            'updated_at'
        ]

class AboutStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutStat
        fields = [
            'id',
            'label',
            'value',
            'icon',
            'order',
            'is_active',
            'created_at',
            'updated_at'
        ]

class AboutSectionSerializer(serializers.ModelSerializer):
    team_members = TeamMemberSerializer(many=True, read_only=True)
    publications = PublicationSerializer(many=True, read_only=True)
    patents = PatentSerializer(many=True, read_only=True)
    stats = AboutStatSerializer(many=True, read_only=True)
    
    class Meta:
        model = AboutSection
        fields = [
            'id',
            'heading',
            'description',
            'is_active',
            'team_members',
            'publications',
            'patents',
            'stats',
            'created_at',
            'updated_at'
        ]