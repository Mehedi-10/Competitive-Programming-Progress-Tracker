from django.shortcuts import HttpResponseRedirect
def is_allowed(get_response):
    def gaurd(request):
        try:
            if not request.session['user_type']:
                return HttpResponseRedirect('signin')
            response = get_response(request)
            return response
        except:
            return HttpResponseRedirect('signin')
    return gaurd