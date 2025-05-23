import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codebin.settings')
django.setup()

from django.contrib.auth.models import User
from snippets.models import Language
from django.utils.text import slugify

def initialize_languages():
    languages = [
        {'name': 'Python', 'syntax_highlight_key': 'python'},
        {'name': 'JavaScript', 'syntax_highlight_key': 'javascript'},
        {'name': 'HTML', 'syntax_highlight_key': 'html'},
        {'name': 'CSS', 'syntax_highlight_key': 'css'},
        {'name': 'Java', 'syntax_highlight_key': 'java'},
        {'name': 'C++', 'syntax_highlight_key': 'cpp'},
        {'name': 'C#', 'syntax_highlight_key': 'csharp', 'slug': 'csharp'},  # Slug personnalisé pour C#
        {'name': 'PHP', 'syntax_highlight_key': 'php'},
        {'name': 'Ruby', 'syntax_highlight_key': 'ruby'},
        {'name': 'Swift', 'syntax_highlight_key': 'swift'},
        {'name': 'Go', 'syntax_highlight_key': 'go'},
        {'name': 'TypeScript', 'syntax_highlight_key': 'typescript'},
        {'name': 'Rust', 'syntax_highlight_key': 'rust'},
        {'name': 'Kotlin', 'syntax_highlight_key': 'kotlin'},
        {'name': 'SQL', 'syntax_highlight_key': 'sql'},
        {'name': 'Bash', 'syntax_highlight_key': 'bash'},
        {'name': 'JSON', 'syntax_highlight_key': 'json'},
        {'name': 'XML', 'syntax_highlight_key': 'xml'},
        {'name': 'Markdown', 'syntax_highlight_key': 'markdown'},
        {'name': 'YAML', 'syntax_highlight_key': 'yaml'},
    ]
    
    for lang_data in languages:
        try:
            # Utiliser le slug personnalisé s'il existe, sinon le générer
            defaults = {
                'syntax_highlight_key': lang_data['syntax_highlight_key'],
                'slug': lang_data.get('slug') or slugify(lang_data['name'])
            }
            
            Language.objects.get_or_create(
                name=lang_data['name'],
                defaults=defaults
            )
        except Exception as e:
            print(f"Error creating {lang_data['name']}: {str(e)}")
            continue
    
    print(f"Added {len(languages)} programming languages")


def create_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        print("Superuser created: admin / admin")


if __name__ == '__main__':
    print("Initializing database...")
    initialize_languages()
    create_superuser()
    print("Database initialization complete!")