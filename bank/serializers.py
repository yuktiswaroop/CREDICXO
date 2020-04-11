from rest_framework import serializers
from .models import Bank, Branch

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = [
            'id', 'ifsc', 'bank_id', 'branch', 'address','city', 
            'district', 'state',
            'bank_name', 
            ]