from django.db.models import Q
from fuzzywuzzy import fuzz

from ..models import Car
from django.db import models
from django.db.models import Case, When


def search_cars(query):
    search_terms = query.split()

    # Build query for partial matching on 'name', 'model', 'year', 'price', and 'description'
    name = Q()
    name_query = Q()
    model_query = Q()
    year_query = Q()
    price_query = Q()
    description_query = Q()

    for term in search_terms:
        if len(term) >= 3:
            name |= Q(name=query)
            name_query |= Q(name__icontains=term)
            model_query |= Q(model__icontains=term)
            year_query |= Q(year__icontains=term)
            price_query |= Q(price__icontains=term)
            description_query |= Q(description__icontains=term)

    # Combine the queries for all fields
    all_fields_query = name | name_query | model_query | year_query | price_query | description_query

    # Perform the search query
    results = Car.objects.filter(all_fields_query, post=True).annotate(
        similarity=Case(
            When(name=query, then=1),
            default=0,
            output_field=models.IntegerField()
        )
    ).order_by('-similarity', 'name')

    return results
