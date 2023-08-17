from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext as _

class UserLoginLog(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('User'),
        related_name='login_logs',
        blank=True,
        null=True, on_delete=models.CASCADE
    )
    ip_address = models.GenericIPAddressField(
        verbose_name=_('IP Address')
    )
    user_agent = models.CharField(
        verbose_name=_('HTTP User Agent'),
        max_length=300,
    )

    class Meta:
        verbose_name = _('user login log')
        verbose_name_plural = _('user login logs')
        ordering = ('-created',)

    def __str__(self):
        return '%s %s' % (self.user, self.ip_address)

