import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "interview_project.settings")
django.setup()

import os
import glob
import subprocess
import pandas as pd
from django.core.management.base import BaseCommand
from interview_app.models import (
    School,
    Class,
    AssessmentArea,
    Student,
    Answers,
    Awards,
    Subject,
    Summary,
)

class Command(BaseCommand):
    help = "Import data from CSV files"

    def handle(self, *args, **options):
        # Define the path to the directory containing CSV files
        csv_directory = "interview_app/data/"

        # Discover all CSV files in the specified directory
        csv_files = glob.glob(os.path.join(csv_directory, "*.csv"))

        # Process data in batches for efficiency
        batch_size = 1000

        for csv_file in csv_files:
            self.stdout.write(self.style.SUCCESS(f"Processing data from {csv_file}"))

            try:
                chunk_size = None
                for chunk in pd.read_csv(csv_file, chunksize=batch_size):
                    chunk_size = len(chunk)
                    schools = []
                    classes = []
                    assessment_areas = []
                    students = []
                    awards = []
                    subjects = []
                    summaries = []

                    for _, row in chunk.iterrows():
                        # Create or retrieve a School object based on the school name
                        school, _ = School.objects.get_or_create(
                            name=row["school_name"]
                        )

                        # Create or retrieve a Class object based on the class name
                        class_name = row["Class"]
                        class_instance, _ = Class.objects.get_or_create(
                            class_name=class_name
                        )

                        # Create or retrieve an AssessmentArea object based on the Assessment Area name
                        assessment_area_name = row["Assessment Areas"]
                        assessment_area, _ = AssessmentArea.objects.get_or_create(
                            name=assessment_area_name
                        )

                        # Create a unique student identifier based on StudentID
                        student_identifier = row["StudentID"]
                        # Create or retrieve a Student object based on the unique identifier
                        student, _ = Student.objects.get_or_create(
                            id=student_identifier,
                            defaults={
                                "fullname": f"{row['First Name']} {row['Last Name']}",
                            },
                        )

                        # Use .filter() to get all matching Answers objects
                        answer_value = row["Answers"]
                        answers_instances = Answers.objects.filter(answer=answer_value)

                        if answers_instances.exists():
                            answers_instance = answers_instances.first()
                        else:
                            # If it doesn't exist, create a new Answers object
                            answers_instance = Answers.objects.create(
                                answer=answer_value
                            )

                        awards_name = row["award"] or row["awarDistinction"]
                        awards_instance, _ = Awards.objects.get_or_create(
                            name=awards_name
                        )

                        # Create or retrieve a Subject object based on the subject name
                        subject_name = row["Subject"]
                        subject_instance, _ = Subject.objects.get_or_create(
                            subject_name=subject_name,
                            defaults={"subject_score": row["student_score"]},
                        )

                        summaries.append(
                            Summary(
                                school=school,
                                syndey_participant=row["sydney_participants"],
                                syndey_percentile=row["sydney_percentile"],
                                assessment_area=assessment_area,
                                award=awards_instance,
                                class_name=class_instance,
                                correct_answer_percentage_per_class=row[
                                    "correct_answer_percentage_per_class"
                                ],
                                correct_answer=answers_instance,
                                student=student,
                                student_score=row["student_score"],
                                subject=subject_instance,
                                category_id=row["Question Number"],
                                year_level_name=row["Year Level"],
                            )
                        )

                    # Bulk create model instances for the current batch
                    School.objects.bulk_create(schools)
                    Class.objects.bulk_create(classes)
                    AssessmentArea.objects.bulk_create(assessment_areas)
                    Student.objects.bulk_create(students)
                    Awards.objects.bulk_create(awards)
                    Subject.objects.bulk_create(subjects)
                    Summary.objects.bulk_create(summaries)

                self.stdout.write(
                    self.style.SUCCESS(
                        f"Processed {chunk_size} records from {csv_file}"
                    )
                )

            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"Error processing data from {csv_file}: {e}")
                )
                continue

        self.stdout.write(
            self.style.SUCCESS("Successfully imported data from all datasets")
        )
