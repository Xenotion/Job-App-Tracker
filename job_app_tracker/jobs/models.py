from django.db import models

class JobApplication(models.Model):
    RESULT_CHOICES = (
        ('Waiting', 'Waiting'),
        ('Offer', 'Offer'),
        ('Rejected', 'Rejected'),
    )
        
    TYPE_CHOICES = (
        ('A', 'Type A Process'),
        ('B', 'Type B Process'),
    )

    company_name = models.CharField(max_length=255)
    role_position = models.CharField(max_length=255)
    initial_application_submission_date = models.DateField()
    application_type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    result = models.CharField(max_length=10, choices=RESULT_CHOICES, null=True, blank=True)

    def __str__(self):
        return f'{self.company_name} - {self.role_position}'

class TypeA(models.Model):
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, null=True)

    online_assessment_date = models.DateField(null=True, blank=True)
    online_assessment_completed = models.BooleanField(default=False)

    digital_interview_date = models.DateField(null=True, blank=True)
    digital_interview_completed = models.BooleanField(default=False)

    assessment_centre_date = models.DateField(null=True, blank=True)
    assessment_centre_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Type A - {self.job_application.company_name}'

class TypeB(models.Model):
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE, null=True)

    recruiter_interview_date = models.DateField(null=True, blank=True)
    recruiter_interview_completed = models.BooleanField(default=False)

    technical_interview_date = models.DateField(null=True, blank=True)
    technical_interview_completed = models.BooleanField(default=False)

    behavioural_interview_date = models.DateField(null=True, blank=True)
    behavioural_interview_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Type B - {self.job_application.company_name}'
