from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Bank, Branch
from .serializers import BranchSerializer
import csv
from django.views import View
from django.http import JsonResponse

class DetailView(View):
    def get(self, request, ifsc):
        branch = Branch.objects.filter(ifsc__iexact=ifsc).first()
        serializer = BranchSerializer(branch)
        return JsonResponse(serializer.data, safe=False)

class ListView(View):
    def get(self, request, city, bank_name):
        branch_qset = Branch.objects.filter(
            city__iexact=city, bank_name__name__icontains=bank_name)
        serializer = BranchSerializer(branch_qset, many=True)
        return JsonResponse(serializer.data, safe=False)

def home(request):
	branch = Branch.objects.all()
	print(branch)
	return HttpResponse ("done")
    