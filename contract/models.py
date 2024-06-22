from django.db import models

class EmploymentAgreement(models.Model):
    employee_name = models.CharField(max_length=1000)
    role = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    terms = models.TextField()
    other_details = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee_name} - {self.role}"



