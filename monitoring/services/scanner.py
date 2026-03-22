from monitoring.models import Keyword,Flag

from monitoring.models import ContentItem
from django.utils.dateparse import parse_datetime

def calculate_score(keyword, content_item):
    keyword = keyword.lower()
    title=content_item.title.lower()
    body = content_item.body.lower()

    if keyword in title.split():
        return 100
    elif keyword in title:
        return 70
    elif keyword in body:
        return 40
    return 0

def run_scan(content_items):
    keywords = Keyword.objects.all()

    for content in content_items:
        for keyword in keywords:

            score = calculate_score(keyword.name, content)

            if score == 0:
                continue

            existing_flag = Flag.objects.filter(
                keyword=keyword,
                content_item=content
            ).first()

            if existing_flag:

                
                if existing_flag.status == 'irrelevant':
                    if existing_flag.reviewed_at and content.last_updated <= existing_flag.reviewed_at:
                        continue

                continue

            Flag.objects.create(
                keyword=keyword,
                content_item=content,
                score=score
            )

# Mock Data

def load_mock_data():
    data = [
        {
            "title": "Learn Django Fast",
            "body": "Django is a powerful Python framework",
            "source": "Blog A",
            "last_updated": "2026-03-20T10:00:00Z"
        },
        {
            "title": "Cooking Tips",
            "body": "Best recipes for beginners",
            "source": "Blog B",
            "last_updated": "2026-03-20T10:00:00Z"
        }
    ]

    content_items = []

    for item in data:
        obj, created = ContentItem.objects.update_or_create(
            title=item["title"],  
            defaults={
                "body": item["body"],
                "source": item["source"],
                "last_updated": parse_datetime(item["last_updated"])
            }
        )

        content_items.append(obj)

    return content_items