from django.shortcuts import render
from .models import Solution

def solution_list(request):
    # 1. Fetch all solutions from the database
    all_solutions = Solution.objects.all()
    
    # 2. Package them up and send them to an HTML file
    return render(request, 'tracker/solution_list.html', {'solutions': all_solutions})