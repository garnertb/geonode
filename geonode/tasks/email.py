from celery.task import task
from geonode.people.models import Profile

@task(name='geonode.tasks.email.send_notification', queue='email')
def send_notification(recipients_ids, notice_type_label):
    try:
        from notification import models as notification
        from notification.models import NoticeSetting
    except ImportError:
        return

    recipients = Profile.objects.filter(id__in=recipients_ids)
    notification.send(recipients, notice_type_label, {"instance": instance})