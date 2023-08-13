from rest_framework import serializers
from .models import JobApplication, TypeA, TypeB

class TypeASerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeA
        fields = '__all__'

class TypeBSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeB
        fields = '__all__'

class JobApplicationSerializer(serializers.ModelSerializer):
    type_a = TypeASerializer(read_only=False, required=False, allow_null=True)
    type_b = TypeBSerializer(read_only=False, required=False, allow_null=True)

    class Meta:
        model = JobApplication
        fields = '__all__'

    def create(self, validated_data):
        type_a_data = validated_data.pop('type_a', None)
        type_b_data = validated_data.pop('type_b', None)
        job_application = JobApplication.objects.create(**validated_data)

        if type_a_data:
            TypeA.objects.create(job_application=job_application, **type_a_data)

        if type_b_data:
            TypeB.objects.create(job_application=job_application, **type_b_data)

        return job_application
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation['type_a'] = TypeASerializer(instance.typea_set.first()).data
        except TypeA.DoesNotExist:
            representation['type_a'] = None

        try:
            representation['type_b'] = TypeBSerializer(instance.typeb_set.first()).data
        except TypeB.DoesNotExist:
            representation['type_b'] = None

        return representation
    
    def update(self, instance, validated_data):
        type_a_data = validated_data.pop('type_a', None)
        type_b_data = validated_data.pop('type_b', None)

        new_application_type = validated_data.get('application_type', instance.application_type)

        # Check if the application type has changed
        if instance.application_type != new_application_type:
            if new_application_type == 'A':
                # Delete type B data if switching to type A
                instance.typeb_set.all().delete()
            elif new_application_type == 'B':
                # Delete type A data if switching to type B
                instance.typea_set.all().delete()

        instance.company_name = validated_data.get('company_name', instance.company_name)
        instance.role_position = validated_data.get('role_position', instance.role_position)
        instance.initial_application_submission_date = validated_data.get('initial_application_submission_date', instance.initial_application_submission_date)
        instance.application_type = new_application_type
        instance.result = validated_data.get('result', instance.result)
        instance.save()

        if type_a_data:
            type_a_instance = instance.typea_set.first()
            if type_a_instance:
                for attr, value in type_a_data.items():
                    setattr(type_a_instance, attr, value)
                type_a_instance.save()
            else:
                type_a_data.pop('job_application', None)  # Remove the job_application key if it exists
                TypeA.objects.create(job_application=instance, **type_a_data)

        if type_b_data:
            type_b_instance = instance.typeb_set.first()
            if type_b_instance:
                for attr, value in type_b_data.items():
                    setattr(type_b_instance, attr, value)
                type_b_instance.save()
            else:
                type_b_data.pop('job_application', None)  # Remove the job_application key if it exists
                TypeB.objects.create(job_application=instance, **type_b_data)


        return instance


