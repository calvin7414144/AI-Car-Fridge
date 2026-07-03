from django.conf import settings
from django.http import HttpResponse
from django.utils import translation


def frontend_page(request, page='index'):
    allowed_pages = {'index', 'product', 'factory', 'custom', 'contact'}
    page_name = page if page in allowed_pages else 'index'
    index_path = settings.BASE_DIR / 'static' / 'frontend' / f'{page_name}.html'
    if index_path.exists():
        return HttpResponse(index_path.read_text(encoding='utf-8'), content_type='text/html; charset=utf-8')

    return HttpResponse('Vue frontend is not built yet. Run pnpm build in the frontend directory.', status=503)


def set_admin_language(request, language_code):
    language = language_code if language_code in dict(settings.LANGUAGES) else settings.LANGUAGE_CODE
    translation.activate(language)

    response = HttpResponse(
        """
        <!doctype html>
        <html>
        <head><meta charset="utf-8"></head>
        <body>
        <script>
            window.top.sessionStorage.clear();
            window.top.location.href = "/admin/";
        </script>
        </body>
        </html>
        """
    )
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response
