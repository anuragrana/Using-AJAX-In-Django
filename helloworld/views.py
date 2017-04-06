from django.shortcuts import render
from django.http import HttpResponse
import logging
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

def index(request):
    #return HttpResponse("Hello World. First Django Project. ThePythonDjango.Com")
    return render(request,"helloworld/index.html",{})



def check_login(request):
    if request.method == "GET":
        raise Http404("URL doesn't exists")
    else:   
        response_data = {}
        login = request.POST["login"]
        user = None
        try:
            try:
                # we are matching the input again hardcoded value to avoid use of DB.
                # You can use DB and fetch value from table and proceed accordingly.
                if login == "rana" or login == "rana1":
                    user = True
            except ObjectDoesNotExist as e:
                pass
            except Exception as e:
                raise e
            if not user:
                response_data["is_success"] = True
            else:
                response_data["is_success"] = False
        except Exception as e:
            response_data["is_success"] = False
            response_data["msg"] = "Some error occurred. Please let Admin know."

        return JsonResponse(response_data)


