from django.urls import path
from . import views

urlpatterns = [
    path('TopItemsToConsume/', views.top_items_to_consume, name='TopItemsToConsume'),
    path('suggest/<str:fg2>', views.suggest, name='suggest'),
    path('TopItemsToAvoid/', views.top_items_to_avoid, name='TopItemsToAvoid'),
    path('DetailedHelpfulList/<str:fg1>', views.detailed_helpful_list, name='DetailedHelpfulList'),
    path('DetailedHarmfulList/<str:fg1>', views.detailed_harmful_list, name='DetailedHarmfulList'),
    path('DetailedNeutralList/<str:fg1>', views.detailed_neutral_list, name='DetailedNeutralList'),
    path('GoodFor/<int:b>', views.good_for, name='GoodFor'),
    path('FoodGroups', views.food_groups, name='FoodGroups'),
    path('HealthConditions', views.health_conditions, name='HealthConditions'),
    path('FoodItems/<str:fg>/<str:condition>/<str:value>', views.food_items, name='FoodItems'),

]
