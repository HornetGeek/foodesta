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
    path('InitSession/', views.init_session, name='InitSession'),
    path('AcceptTermsOfUse/', views.accept_terms_of_use, name='AcceptTermsOfUse'),
    path('GetUseDefaultValues/<str:sessionid>', views.get_use_default_values, name='GetUseDefaultValues'),
    path('GetOutcomes/', views.get_out_comes, name='GetOutcomes'),
    path('GetFeatures/', views.get_features, name='GetFeatures'),
    path('SetUseDefaultValues/<str:sessionId>/<str:boolean>', views.set_use_default_values, name='SetUseDefaultValues'),
    path('UpdateFeature/<str:sessionId>/<str:feature>/<str:boolean>', views.update_feature, name='UpdateFeature'),
    path('DeleteFeature/<str:sessionId>/<str:feature>', views.delete_feature, name='DeleteFeature'),

]
