from django.conf.urls import include, url
from Admin import views

urlpatterns = [
				#Bus Ticket Reservation System Project
     url(r'^loader/', views.loader, name='admin_loader'),

	 url(r'^home/',views.home, name = 'admin_home'),

	 url(r'^logout/', views.logout, name='admin_logout'),

	 url(r'^register/', views.register, name='admin_register'),
	 url(r'^registerUser/', views.registerUser, name='admin_register_user'),

     url(r'^faqs/', views.faqs, name='admin_faqs'),

     url(r'^tellAFriend/', views.tellAFriend, name='admin_tell_friend'),
     url(r'^friendOptions/', views.friendOptions, name='admin_friend_options'),
     url(r'^friendApproval/', views.friendApproval, name='admin_friend_approval'),

     url(r'^feedback/', views.feedback, name='admin_feedback'),
     url(r'^feedbackOptions/', views.feedbackOptions, name='admin_feedback_options'),

     url(r'^users/', views.users, name='admin_users'),
     url(r'^usersOptions/', views.usersOptions, name='admin_users_options'),

     url(r'^buses/', views.buses, name='admin_buses'),
     url(r'^busesOptions/', views.busesOptions, name='admin_buses_options'),
     url(r'^newBus/', views.newBus, name='admin_buses_new'),
     url(r'^newBusForm/', views.newBusForm, name='admin_buses_new_form'),
     url(r'^editBus/', views.editBus, name='admin_buses_edit'),

     url(r'^fares/', views.fares, name='admin_fares'),
     url(r'^faresOptions/', views.faresOptions, name='admin_fares_options'),
     url(r'^editFare/', views.editFare, name='admin_fares_edit'),
     url(r'^newFare/', views.newFare, name='admin_fares_new'),
     url(r'^newFareForm/', views.newFareForm, name='admin_fares_new_form'),

     url(r'^changePassword/', views.changePassword, name='admin_change_password'),
     url(r'^changePasswordForm/', views.changePasswordForm, name='admin_change_password_form'),

     url(r'^reservations/', views.reservations, name='admin_reservations'),
     url(r'^reservationsOptions/', views.reservationsOptions, name='admin_reservations_options'),
]
