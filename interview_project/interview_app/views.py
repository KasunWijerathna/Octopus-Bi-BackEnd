from django.shortcuts import render
from django.views.generic import ListView
from .models import School
from rest_framework import viewsets
from .models import Summary
from .serializers import SummarySerializer

from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage


def get_paginated_summaries(request):
    page = request.GET.get("page", 1)
    page_size = request.GET.get("page_size", 10)  # Number of summaries per page

    # Replace this with your actual query to retrieve summaries
    all_summaries = Summary.objects.all()

    paginator = Paginator(all_summaries, page_size)

    try:
        current_page = paginator.page(page)
    except EmptyPage:
        return JsonResponse({"error": "Page out of range"}, status=400)

    summaries = [
        {
            "school": summary.school.name,
            "student": summary.student.fullname,
            "subject": summary.subject.subject_name,
            "sydney_participant": summary.syndey_participant,
            "sydney_percentile": summary.syndey_percentile,
            "assessment_area": summary.assessment_area.name,
            "award": summary.award.name,
            "class_name": summary.class_name.class_name,
            "correct_answer_percentage_per_class": summary.correct_answer_percentage_per_class,
            "correct_answer": summary.correct_answer.answer,
            "student_score": summary.student_score,
            "category_id": summary.category_id,
            "year_level_name": summary.year_level_name,
            # Add more fields you want to include
        }
        for summary in current_page
    ]

    response_data = {
        "page": current_page.number,
        "page_size": page_size,
        "total_pages": paginator.num_pages,
        "total_items": paginator.count,
        "data": summaries,
    }

    return JsonResponse(response_data)


class SchoolListView(ListView):
    model = School
    template_name = "school_list.html"
    context_object_name = "schools"


class SummaryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer
