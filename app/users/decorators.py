from django.shortcuts import redirect

def redirect_authenticated_user(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Redirige a la página de inicio o a donde desees
        return view_func(request, *args, **kwargs)
    return _wrapped_view_func
