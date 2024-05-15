from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView # UpdateView, DeleteView

from .forms import ReviewForm
from .models import Review
## from .models import Review

# Create your views here.

class ReviewView(CreateView):
  model = Review
  form_class = ReviewForm
  template_name = 'reviews/review.html'
  success_url = '/thank-you'
  
  ## OK approach (NOTE: Using View, NOT CreateView)
  # def get(self, request):
  #   form = ReviewForm()
  #   return render(request, 'reviews/review.html', {
  #     'form': form
  #   })
  
  # def post(self, request):
  #   form = ReviewForm(request.POST)

  #   if form.is_valid():
  #     form.save()
  #     return HttpResponseRedirect('/thank-you')
  #   return render(request, 'reviews/review.html', {
  #     'form': form
  #   })

## OK approach
"""
def review(request):
  if request.method == 'POST':
    ## existing_data = Review.objects.get(pk=1)
    form = ReviewForm(request.POST) ## instance=existing_data

    if form.is_valid():
      form.save()
      # review = Review(user_name=form.cleaned_data['user_name'], review_text=form.cleaned_data['review_text'], rating=form.cleaned_data['rating'])
      # review.save()
      return HttpResponseRedirect('/thank-you')
  else:
    form = ReviewForm()

  return render(request, 'reviews/review.html', {
    'form': form
  })
"""

class ThankYouView(TemplateView):
  template_name = 'reviews/thank_you.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['message'] = 'This works!'
    return context

# OK approach
"""
def thank_you(request):
  return render(request, 'reviews/thank_you.html')
"""

class ReviewsListView(ListView):
  template_name = 'reviews/review_list.html'
  model = Review
  context_object_name = 'reviews'

  # def get_queryset(self):
  #   base_query = super().get_queryset()
  #   data = base_query.filter(rating__gt=3)
  #   return data

class SingleReviewView(DetailView):
  template_name = 'reviews/single_review.html'
  model = Review

class AddFavoriteView(View):
  def post(self, request):
    review_id = request.POST['review_id']
    fav_review = Review.objects.get(pk=review_id)
    request.session['favorite_review'] = fav_review
    return HttpResponseRedirect('/reviews/' + review_id)