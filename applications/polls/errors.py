from django.shortcuts import render


def page_forbidden(request, exception):
    return render(
        request,
        'misc/403.html',
        {'path': request.path},
        status=403
    )


def page_not_found(request, exception):
    return render(
        request,
        'misc/404.html',
        {'path': request.path},
        status=404
    )


def server_error(request):
    return render(
        request,
        'misc/500.html',
        status=500)
