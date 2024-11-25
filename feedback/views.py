from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Feedback
from .forms import FeedbackForm
from django.db.models import Avg

def home(request):
    items = Item.objects.all()
    return render(request, 'feedback/home.html', {'items': items})

def item_detail(request, pk):
    # Fetch the item and its feedbacks
    item = get_object_or_404(Item, pk=pk)
    feedbacks = Feedback.objects.filter(item=item)

    # Calculate the average rating
    average_rating = feedbacks.aggregate(Avg('rating'))['rating__avg'] or 0

    # Handle the feedback form
    form = FeedbackForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        feedback = form.save(commit=False)
        feedback.item = item
        feedback.save()
        return redirect('item_detail', pk=item.pk)

    return render(request, 'feedback/item_detail.html', {
        'item': item,
        'feedbacks': feedbacks,
        'form': form,
        'average_rating': round(average_rating, 2),
    })
