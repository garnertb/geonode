from celery.task import task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@task(name='geonode.tasks.email.send_queued_notifications', queue='email')
def send_queued_notifications(*args):
    """
    Sends queued notifications.

    settings.NOTIFICATION_QUEUE_ALL needs to be true in order to take advantage of this.
    """

    try:
        from notification.engine import send_all
    except ImportError:
        return

    logger.debug('Sending queued notifications.')
    send_all(*args)
