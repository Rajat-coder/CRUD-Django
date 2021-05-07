from rest_framework import serializers
from authentication.models import *

class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = "__all__"

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields ="__all__"

    def validate_participant(self, data):
        parti_data = data
        parti_list = parti_data.split(',')
        parti_data2 = []
        if len(parti_list) < 11:
            for i in parti_list:
                if len(i) <101:
                    parti_data2.append(i)
                else:
                    raise serializers.ValidationError({"participant": "string cannot be larger than 100 characters"})
        else:
            raise serializers.ValidationError({"participant": "maximum of 10 participants possible"})

        return data
    