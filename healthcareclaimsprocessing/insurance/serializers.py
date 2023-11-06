from rest_framework import serializers
from .models import Patient, Provider, InsuranceClaim



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('name', 'policy_number')

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('id', 'name', 'speciality')

class InsuranceClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceClaim
        fields = ('id', 'Patient', 'provider', 'claim_amount', 'submitted_at', 'is_approved')