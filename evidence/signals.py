from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from evidence.models import Evidence, UserEvidenceLog
from django.conf import settings
import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from ipware.ip import get_client_ip
from user.models import UserLoginLog

@receiver( post_save, sender = Evidence )
def evidence_save( sender, user, request, **kwargs ):
    evidence = kwargs[ 'instance' ]
    evidence_log=UserEvidenceLog()
    evidence_log.title=evidence.title
    evidence_log.user=evidence.user
    evidence_log.created_at=evidence.created_at
    evidence_log.ip_address = get_client_ip(request)

    print('evidence 생성됨')
    evidence_log.save()

# def create_profile(sender, instance, created, **kwargs):
# 	print('시그널 실행')
# 	if created == True:
              

# post_save.connect(evidence_save, sender=Evidence)




@receiver(user_logged_in)
def sig_user_logged_in(sender, user, request, **kwargs):
    log = UserLoginLog()
    log.user = user
    client_ip, is_routable = get_client_ip(request)
    log.ip_address = client_ip
    log.user_agent = request.META['HTTP_USER_AGENT']
    log.save()


