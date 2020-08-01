from django.shortcuts import render
from .models import User, ActivityPeriod
import requests, json
from django.http import JsonResponse
# Create your views here.

# Since there wasn't a lot of informationa available about the assignment, I have made a few assumptions.
# 1. The request will a post request.
# 2. The request will be containing a json which will contain a list of id for which the data is to be returned
# 3. I date-time value in ActivityPeriods is string (I had little time so I used string to store them).

def send_json(request):
    if request.method == 'POST':
        content = json.loads(request.body)
        id_list = content['id_list']
        members_list = []
        for uid in id_list:
            user_obj = User.objects.filter(id = uid).values()
            user_list = list(user_obj)
            activity_period = ActivityPeriod.objects.filter(user = uid).values()
            activity_period_list = list(activity_period)
            member_dictionary =  user_list[0]
            actvity_dictionary_list = []
            for actvity_dictionary in activity_period_list:
                temp_dictionary = {"start_time" : actvity_dictionary["start_time"], "end_time" : actvity_dictionary["end_time"]}
                actvity_dictionary_list.append(temp_dictionary)
            member_dictionary["activity_periods"] = actvity_dictionary_list
            members_list.append(member_dictionary)
            final_dictionary = {"ok" : True, "members" : members_list}
        return JsonResponse(final_dictionary, safe=False)