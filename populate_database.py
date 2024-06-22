import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employment_contracts.settings')
django.setup()

from contract.models import EmploymentAgreement


def dummyData():
     
   #dummy data gotten from AI
   dummy_data = [
    {
        "employee_name": "John Doe",
        "role": "Developer",
        "start_date": "2024-07-01",
        "end_date": "2025-06-30",
        "salary": 80000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Engineering", "manager": "Jane Smith"}
    },
    {
        "employee_name": "Alice Johnson",
        "role": "Designer",
        "start_date": "2024-08-15",
        "end_date": "2025-07-31",
        "salary": 75000,
        "terms": "Part-time, no benefits",
        "other_details": {"department": "Design", "manager": "David Brown"}
    },
    {
        "employee_name": "Emily Wilson",
        "role": "Marketing Specialist",
        "start_date": "2024-09-01",
        "end_date": "2025-08-31",
        "salary": 85000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Marketing", "manager": "Michael Johnson"}
    },
    {
        "employee_name": "Mark Davis",
        "role": "Sales Manager",
        "start_date": "2024-07-15",
        "end_date": "2025-07-14",
        "salary": 90000,
        "terms": "Full-time, commission-based",
        "other_details": {"department": "Sales", "manager": "Laura White"}
    },
    {
        "employee_name": "Sarah Miller",
        "role": "HR Coordinator",
        "start_date": "2024-08-01",
        "end_date": "2025-07-31",
        "salary": 70000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "HR", "manager": "Robert Green"}
    },
    {
        "employee_name": "Michael Lee",
        "role": "IT Specialist",
        "start_date": "2024-09-01",
        "end_date": "2025-08-31",
        "salary": 95000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "IT", "manager": "Jennifer Clark"}
    },
    {
        "employee_name": "Jessica Garcia",
        "role": "Financial Analyst",
        "start_date": "2024-07-01",
        "end_date": "2025-06-30",
        "salary": 85000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Finance", "manager": "Daniel Thomas"}
    },
    {
        "employee_name": "Brian Robinson",
        "role": "Operations Manager",
        "start_date": "2024-08-15",
        "end_date": "2025-07-31",
        "salary": 100000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Operations", "manager": "Olivia Martinez"}
    },
    {
        "employee_name": "Rachel Brown",
        "role": "Customer Support",
        "start_date": "2024-09-01",
        "end_date": "2025-08-31",
        "salary": 80000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Customer Support", "manager": "William Wilson"}
    },
    {
        "employee_name": "Eric Thompson",
        "role": "Quality Assurance",
        "start_date": "2024-07-15",
        "end_date": "2025-07-14",
        "salary": 90000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "QA", "manager": "Sophia Taylor"}
    },
    {
        "employee_name": "Oliver White",
        "role": "Data Analyst",
        "start_date": "2024-08-01",
        "end_date": "2025-07-31",
        "salary": 82000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Analytics", "manager": "Emma Moore"}
    },
    {
        "employee_name": "Grace Walker",
        "role": "Project Manager",
        "start_date": "2024-09-01",
        "end_date": "2025-08-31",
        "salary": 95000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Project Management", "manager": "Jack Harris"}
    },
    {
        "employee_name": "Lucas Green",
        "role": "Business Development",
        "start_date": "2024-07-15",
        "end_date": "2025-07-14",
        "salary": 88000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Business Development", "manager": "Lily Rogers"}
    },
    {
        "employee_name": "Sophie Hall",
        "role": "Legal Counsel",
        "start_date": "2024-08-01",
        "end_date": "2025-07-31",
        "salary": 105000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Legal", "manager": "Henry King"}
    },
    {
        "employee_name": "Daniel Scott",
        "role": "Research Scientist",
        "start_date": "2024-09-01",
        "end_date": "2025-08-31",
        "salary": 98000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Research", "manager": "Sarah Parker"}
    },
    {
        "employee_name": "Emma Brooks",
        "role": "Graphic Designer",
        "start_date": "2024-07-15",
        "end_date": "2025-07-14",
        "salary": 75000,
        "terms": "Part-time, no benefits",
        "other_details": {"department": "Design", "manager": "David Brown"}
    },
    {
        "employee_name": "Henry Cook",
        "role": "Accountant",
        "start_date": "2024-08-01",
        "end_date": "2025-07-31",
        "salary": 90000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Finance", "manager": "Jessica Turner"}
    },
    {
        "employee_name": "Liam King",
        "role": "Software Engineer",
        "start_date": "2024-09-01",
        "end_date": "2025-08-31",
        "salary": 87000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Engineering", "manager": "Jane Smith"}
    },
    {
        "employee_name": "Charlotte Reed",
        "role": "UX/UI Designer",
        "start_date": "2024-07-15",
        "end_date": "2025-07-14",
        "salary": 82000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Design", "manager": "David Brown"}
    },
    {
        "employee_name": "Thomas Taylor",
        "role": "Product Manager",
        "start_date": "2024-08-01",
        "end_date": "2025-07-31",
        "salary": 96000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Product Management", "manager": "Jack Harris"}
    },
    {
        "employee_name": "Victoria Evans",
        "role": "Customer Success Manager",
        "start_date": "2024-09-01",
        "end_date": "2025-08-31",
        "salary": 88000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Customer Success", "manager": "William Wilson"}
    },
    {
        "employee_name": "Max Murphy",
        "role": "Operations Coordinator",
        "start_date": "2024-07-15",
        "end_date": "2025-07-14",
        "salary": 78000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Operations", "manager": "Olivia Martinez"}
    },
    {
        "employee_name": "Julia Wright",
        "role": "Marketing Coordinator",
        "start_date": "2024-08-01",
        "end_date": "2025-07-31",
        "salary": 83000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Marketing", "manager": "Michael Johnson"}
    },

    {
        "employee_name": "Daniel Harris",
        "role": "Business Analyst",
        "start_date": "2024-07-10",
        "end_date": "2025-07-09",
        "salary": 85000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Business Analysis", "manager": "Megan Lee"}
    },
    {
        "employee_name": "Samantha Clark",
        "role": "Content Writer",
        "start_date": "2024-08-05",
        "end_date": "2025-08-04",
        "salary": 65000,
        "terms": "Part-time, flexible hours",
        "other_details": {"department": "Content", "manager": "Paul Wright"}
    },
    {
        "employee_name": "James Lewis",
        "role": "Data Scientist",
        "start_date": "2024-09-01",
        "end_date": "2025-08-31",
        "salary": 105000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Data Science", "manager": "Natalie Hall"}
    },
    {
        "employee_name": "Laura Scott",
        "role": "Executive Assistant",
        "start_date": "2024-07-20",
        "end_date": "2025-07-19",
        "salary": 60000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Administration", "manager": "Steven Adams"}
    },
    {
        "employee_name": "Kevin King",
        "role": "Logistics Coordinator",
        "start_date": "2024-08-25",
        "end_date": "2025-08-24",
        "salary": 70000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Logistics", "manager": "Teresa Parker"}
    },
    {
        "employee_name": "Stephanie Baker",
        "role": "Office Manager",
        "start_date": "2024-07-30",
        "end_date": "2025-07-29",
        "salary": 75000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Administration", "manager": "John Green"}
    },
    {
        "employee_name": "Christopher Carter",
        "role": "Product Owner",
        "start_date": "2024-09-05",
        "end_date": "2025-09-04",
        "salary": 110000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Product", "manager": "Lisa Nelson"}
    },
    {
        "employee_name": "Karen Mitchell",
        "role": "Project Coordinator",
        "start_date": "2024-07-15",
        "end_date": "2025-07-14",
        "salary": 80000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Project Management", "manager": "Frank Moore"}
    },
    {
        "employee_name": "Andrew Rodriguez",
        "role": "Research Analyst",
        "start_date": "2024-08-01",
        "end_date": "2025-07-31",
        "salary": 78000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Research", "manager": "Catherine Young"}
    },
    {
        "employee_name": "Nancy Perez",
        "role": "Software Architect",
        "start_date": "2024-09-10",
        "end_date": "2025-09-09",
        "salary": 120000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "IT", "manager": "Patrick Hernandez"}
    },
    {
        "employee_name": "Brian Roberts",
        "role": "Supply Chain Manager",
        "start_date": "2024-07-25",
        "end_date": "2025-07-24",
        "salary": 95000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Supply Chain", "manager": "Susan Martinez"}
    },
    {
        "employee_name": "Rebecca Lee",
        "role": "Talent Acquisition",
        "start_date": "2024-08-20",
        "end_date": "2025-08-19",
        "salary": 82000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "HR", "manager": "Nancy Turner"}
    },
    {
        "employee_name": "Joshua Walker",
        "role": "Technical Writer",
        "start_date": "2024-07-10",
        "end_date": "2025-07-09",
        "salary": 70000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Documentation", "manager": "Amy Phillips"}
    },
    {
        "employee_name": "Rachel Allen",
        "role": "UI/UX Designer",
        "start_date": "2024-08-01",
        "end_date": "2025-07-31",
        "salary": 85000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Design", "manager": "Kyle Johnson"}
    },
    {
        "employee_name": "Aaron Young",
        "role": "VP of Marketing",
        "start_date": "2024-09-15",
        "end_date": "2025-09-14",
        "salary": 150000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Marketing", "manager": "Brittany Roberts"}
    },
    {
        "employee_name": "Emily Gonzalez",
        "role": "Web Developer",
        "start_date": "2024-07-05",
        "end_date": "2025-07-04",
        "salary": 88000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Web Development", "manager": "Justin Collins"}
    },
    {
        "employee_name": "Matthew Perez",
        "role": "Systems Analyst",
        "start_date": "2024-08-10",
        "end_date": "2025-08-09",
        "salary": 92000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "IT", "manager": "Jason Edwards"}
    },
    {
        "employee_name": "Linda Thompson",
        "role": "Training Specialist",
        "start_date": "2024-07-20",
        "end_date": "2025-07-19",
        "salary": 78000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Training", "manager": "Julie White"}
    },
    {
        "employee_name": "William Rivera",
        "role": "Operations Specialist",
        "start_date": "2024-09-01",
        "end_date": "2025-08-31",
        "salary": 85000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Operations", "manager": "Kimberly Harris"}
    },
    {
        "employee_name": "Jessica Green",
        "role": "Accountant",
        "start_date": "2024-08-15",
        "end_date": "2025-08-14",
        "salary": 75000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Finance", "manager": "Gary Sanchez"}
    },
    {
        "employee_name": "Ryan Hall",
        "role": "HR Manager",
        "start_date": "2024-07-25",
        "end_date": "2025-07-24",
        "salary": 90000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "HR", "manager": "Donna Clark"}
    },
    {
        "employee_name": "Olivia Lewis",
        "role": "Customer Success Manager",
        "start_date": "2024-08-05",
        "end_date": "2025-08-04",
        "salary": 93000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Customer Success", "manager": "Mark Allen"}
    },
    {
        "employee_name": "Brandon Allen",
        "role": "Graphic Designer",
        "start_date": "2024-07-15",
        "end_date": "2025-07-14",
        "salary": 78000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Design", "manager": "Susan Walker"}
    },
    {
        "employee_name": "Madison Wright",
        "role": "SEO Specialist",
        "start_date": "2024-09-01",
        "end_date": "2025-08-31",
        "salary": 85000,
        "terms": "Full-time, benefits included",
        "other_details": {"department": "Design", "manager": "Susan Walker"}
    }
 ]


   
   
   #Populate dummy data to database
   populateData(dummy_data)




def populateData(dummy_data):
      #loop and save each item to database
      for data in dummy_data:
            employee = data['employee_name']

            #save employment agreement if employee does not already exist in database
            existing_employee = EmploymentAgreement.objects.filter(employee_name=employee).exists()

            if existing_employee:
                 pass
            else:
                create_data = EmploymentAgreement(
                        employee_name = data['employee_name'],
                        role = data['role'],
                        start_date = data['start_date'],
                        end_date = data['end_date'],
                        salary = data['salary'],
                        terms = data['terms'],
                        other_details = data['other_details']
                        
                )

                create_data.save()
                print(f"Data saved for {data['employee_name']}")

if __name__ == "__main__":
    dummyData()



      

      

        













