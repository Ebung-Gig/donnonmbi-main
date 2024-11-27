from django.core.management.base import BaseCommand
from website.models import Team


class Command(BaseCommand):
    help = "Generate a list of team members"

    def handle(self, *args, **kwargs):
        team_members = [
            {"name": "John Doe", "role": "CEO"},
            {"name": "Jane Smith", "role": "CTO"},
            {"name": "Alice Johnson", "role": "Marketing Manager"},
            {"name": "Bob Brown", "role": "Lead Developer"},
            {"name": "Mary Green", "role": "HR Manager"},
            {"name": "Paul White", "role": "Finance Officer"},
        ]

        # Add team members to the database
        for member in team_members:
            team_member, created = Team.objects.get_or_create(
                name=member["name"], role=member["role"]
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added {team_member.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"{team_member.name} already exists")
                )
