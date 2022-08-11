from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage, name='main_page'),
    path('register_page/', views.registerPage, name='register_page'),
    path('logout_user/', views.logoutUser, name='logout_user'),

    path('explore/', views.explorePage, name='explore'),

    path('post_action/<int:pk>/', views.postAction, name='post_action'),
    path('delete_post/<int:pk>/', views.deletePost, name='delete_post'),
    path('delete_comment/<int:pk>/', views.deleteComment, name='delete_comment'),

    path('<str:user>/', views.userProfile, name='user_profile'),
    path('<str:user>/saved/', views.userProfileSaved, name='user_profile_saved'),


    path('accounts/edit/', views.accountsEdit, name="accounts_edit"),
    path('remove_logo', views.removeLogo, name='remove_logo'),
    path('accounts/password/change/', views.accountsPasswordChange, name='accounts_password_change'),
]
