from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
     person = {'Name':'Ramesh', 'Wing':'C', 'Room No': "504", 'start_time':"16:10", 'end_time':"16:45"}
     return Response(person)