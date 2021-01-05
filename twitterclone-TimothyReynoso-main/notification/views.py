from django.shortcuts import render

from notification.models import Notification
# Create your views here.
def Notifications(request):
    html = 'notifications.html'
    notifications = Notification.objects.filter(user_to_notify=request.user)
    unviewed_notifications = []
    for notification in notifications:
        if notification.notified_flag == False:
            unviewed_notifications.append(notification.tweet_to_notify.tweet_post)
            notification.notified_flag = True
            notification.save()
    return render(request, html, {'notify': unviewed_notifications})
