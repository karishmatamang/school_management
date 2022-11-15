from django.http import HttpResponse

def role_required(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			if request.user.role in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to do the given action')
		return wrapper_func
	return decorator


