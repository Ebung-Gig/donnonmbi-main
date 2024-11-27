from django.core.management.base import BaseCommand
from website.models import Trustee  # Update with your app and model name


class Command(BaseCommand):
    help = "Populate the Trustee model with fake data."

    def handle(self, *args, **kwargs):
        # List of trustee data
        trustee_data = [
            {
                "name": "Dr. Emily Carter",
                "position": "Chairperson",
                "bio": "Dr. Emily Carter is a renowned philanthropist and health policy expert with over 20 years of experience in community development. She is passionate about creating equitable healthcare opportunities globally.",
                "picture": None,  # Replace with the path to the image if available
            },
            {
                "name": "Mr. Jonathan Brown",
                "position": "Vice Chairperson",
                "bio": "Jonathan Brown is a business strategist and entrepreneur who has spearheaded numerous initiatives to foster economic growth in underserved regions.",
                "picture": None,
            },
            {
                "name": "Ms. Sofia Ramirez",
                "position": "Secretary",
                "bio": "Sofia Ramirez is a legal advisor with expertise in non-profit compliance. She has supported several organizations in aligning their governance practices with international standards.",
                "picture": None,
            },
            {
                "name": "Prof. William Zhang",
                "position": "Treasurer",
                "bio": "Professor William Zhang is a finance professor with a passion for sustainable investments. He ensures that the foundation’s funds are managed responsibly to maximize impact.",
                "picture": None,
            },
            {
                "name": "Mrs. Priya Singh",
                "position": "Member",
                "bio": "Priya Singh is an advocate for women's empowerment and education. She has organized workshops to improve literacy and vocational training among rural populations.",
                "picture": None,
            },
            {
                "name": "Mr. Ahmed Ibrahim",
                "position": "Legal Advisor",
                "bio": "Ahmed Ibrahim is a seasoned lawyer specializing in international human rights. His expertise has been instrumental in shaping policies that promote justice and equity.",
                "picture": None,
            },
        ]

        # Populate the database
        for data in trustee_data:
            Trustee.objects.create(
                name=data["name"],
                position=data["position"],
                bio=data["bio"],
                picture=data["picture"],
            )

        self.stdout.write(self.style.SUCCESS("Trustee data populated successfully!"))
