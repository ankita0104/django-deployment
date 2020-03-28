from django.urls import path
from the_chatbot import views as the_chatbot_views

#TEMPLATE TAGGING
app_name='the_chatbot'

urlpatterns =[
   
   path('register/', the_chatbot_views.register,name='register'), 
   path('user_login/',the_chatbot_views.user_login, name='user_login')
   
   ]