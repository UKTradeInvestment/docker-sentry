#!/usr/bin/env python

# Bootstrap the Sentry environment
import time
from sentry.utils.runner import configure
from django.db import IntegrityError
from django.db.utils import OperationalError
configure()

# Do something crazy
from sentry.models import (
    Team, Project, ProjectKey, User, Organization, OrganizationMember,
    OrganizationMemberTeam
)

DEFAULT_ORGANIZATION = 'Default'
DEFAULT_TEAM = 'Default'
DEFAULT_PROJECT = 'Default'


organizations = Organization.objects.filter(name=DEFAULT_ORGANIZATION)
if organizations.count():
    organization = organizations.first()
else:
    organization = Organization()
    organization.name = DEFAULT_ORGANIZATION
    organization.save()

teams = Team.objects.filter(name=DEFAULT_TEAM)
if teams.count():
    team = teams.first()
else:
    team = Team()
    team.name = DEFAULT_TEAM
    team.organization = organization
    team.save()

projects = Project.objects.filter(name=DEFAULT_PROJECT)
if projects.count():
    project = projects.first()
else:
    project = Project()
    project.team = team
    project.name = 'Default'
    project.organization = organization
    project.save()

user = User()
user.username = 'admin'
user.email = 'admin@localhost'
user.is_superuser = True
user.set_password('admin')
try:
    user.save()
except IntegrityError:
    user = User.objects.filter(username='admin').first()

try:
    member = OrganizationMember.objects.create(
        organization=organization,
        user=user,
        role='owner',
    )
except IntegrityError:
    member = OrganizationMember.objects.filter(organization=organization,user=user).first()

try:
    OrganizationMemberTeam.objects.create(
        organizationmember=member,
        team=team,
    )
except IntegrityError:
    pass

for key in ProjectKey.objects.all():
    print 'PROJECT={} SENTRY_DSN={}'.format(key.project.name, key.get_dsn())
