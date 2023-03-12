import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ItemFrom, CommentForm
from .models import Item, Vote, Comment

def frontpage(request):
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)

    items = Item.objects.filter(created_at__gte=date_from).order_by('-number_of_votes')[0:30]

    return render(request, 'item/frontpage.html', {
        'items': items
        })

def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0:
        items = Item.objects.filter(title__icontains=query)
    else:
        items = []

    return render(request, 'item/search.html', {'items': items, 'query': query})

def newest(request):
    items = Item.objects.all()[0:200]

    return render(request, 'item/frontpage.html', {
        'items': items
        })

@login_required
def submit(request):
    if request.method == 'POST':
        form = ItemFrom(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('frontpage')
    else:
        form = ItemFrom()

    return render(request, 'item/submit.html', {
        'form': form,
        })


def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.item = item
            comment.created_by = request.user
            comment.save()

            return redirect('item_detail', item_id=item_id)
    else:
        form = CommentForm()

    return render(request, 'item/detail.html', {'item': item, 'form': form})

@login_required
def vote(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    next_page = request.GET.get('next_page', '')

    if item.created_by != request.user and not Vote.objects.filter(created_by=request.user, item=item):
        vote = Vote.objects.create(item=item, created_by=request.user)

    if next_page == 'detailed':
        return redirect('item_detail', item_id=item_id)
    else:
        return redirect('frontpage')
