import logging

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Seed database"

    def add_arguments(self, parser):
        parser.add_argument(
            "--create-super-user", action="store_true", dest="create_super_user"
        )

    def handle(self, *args, **options):
        if options["create_super_user"]:
            create_super_user()


def create_super_user():

    logger.info("Checking if it's necessary to create a super user")
    does_super_user_exist = User.objects.filter(username="admin").exists()

    if does_super_user_exist:
        logger.info("Super user already exists, there's no need to create another one")
        return

    logger.info("Creating super user")

    u = User(username="admin")
    u.set_password("test")
    u.is_superuser = True
    u.is_staff = True
    u.save()
