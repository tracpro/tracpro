from django.contrib.auth import models as auth_models

from dash.orgs.models import Org


class AbstractDashUser(auth_models.AbstractUser):

    class Meta(auth_models.AbstractUser.Meta):
        abstract = True
        db_table = "auth_user"

    def get_org(self):
        return getattr(self, '_org', None)

    def get_org_group(self):
        org_group = None
        org = self.get_org()
        if org:
            org_group = org.get_user_org_group(self)
        return org_group

    def get_user_orgs(self):
        if self.is_superuser:
            return Org.objects.all()
        user_orgs = self.org_admins.all() | self.org_editors.all() | self.org_viewers.all()
        return user_orgs.distinct()

    def set_org(self, org):
        self._org = org


class User(AbstractDashUser):

    class Meta(AbstractDashUser.Meta):
        swappable = "AUTH_USER_MODEL"
