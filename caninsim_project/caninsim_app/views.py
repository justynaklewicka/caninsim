from django.shortcuts import render

def index(request):
    return render(
        request,
        'index.html',
        # context={'num_books': num_books, 'num_instances': num_instances,
        #          'num_instances_available': num_instances_available, 'num_authors': num_authors,
        #          'num_visits': num_visits},
    )
