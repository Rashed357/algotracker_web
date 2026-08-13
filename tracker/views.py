from django.shortcuts import render, redirect
from .models import Solution

def solution_list(request):
    # 1. If the user clicked the "Save Solution" button (POST request)
    if request.method == 'POST':
        # Extract the data sent by the HTML form
        form_problem = request.POST.get('problem_name')
        form_language = request.POST.get('language')
        form_code = request.POST.get('code')
        
        # Tell the database to create and save a new entry
        Solution.objects.create(
            problem_name=form_problem,
            language=form_language,
            code=form_code
        )
        
        # Refresh the page so the form doesn't accidentally submit twice
        return redirect('solution_list')

    # 2. If the user is just visiting the page normally (GET request)
    all_solutions = Solution.objects.all()
    return render(request, 'tracker/solution_list.html', {'solutions': all_solutions})