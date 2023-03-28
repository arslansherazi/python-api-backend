from django.conf.urls import include, url
from User import views

urlpatterns = [
				#Bus Ticket Reservation System Project
	 url(r'^loader/', views.loader, name='user_loader'),

	 url(r'^home/',views.home, name = 'Home'),
	 url(r'^logout/', views.logout, name='user_logout'),

	 url(r'^reservations/', views.myReservations, name='user_reservations'),
	 url(r'^userReservations/', views.reservationsOptions, name='user_reservations_options'),

	 url(r'^faqs/', views.faqs, name='user_faqs'),
	 url(r'^friend/', views.friend, name='user_friend'),
	 url(r'^feedback/', views.feedback, name='user_feedback'),
	 url(r'^friendForm/', views.friendForm, name='user_friendForm'),
	 url(r'^feedbackForm/', views.feedbackForm, name='user_feedbackForm'),
	 url(r'^fareList/', views.fareList, name='user_fareList'),
	 url(r'^logout/', views.logout, name='user_logout'),
	 url(r'^changePassword/', views.changePassword, name='user_changePassword'),
	 url(r'^changePasswordForm/', views.changePasswordForm, name='user_change_password_form'),

	 url(r'^BookingsUrl/', views.ticketBookingURL, name='user_bookings_url'),
	 url(r'^Bookings/', views.ticketBooking, name='user_bookings'),
	 url(r'^BookingsForm/', views.ticketBookingForm, name='user_bookings_form'),

	 url(r'^Profile/', views.profileUpdate, name='user_profile_update'),
	 url(r'^profileData/', views.profileUpdateForm, name='user_profile_update_form'),
]
