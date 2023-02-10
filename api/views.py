from rest_framework.response import Response
from rest_framework.decorators import api_view
from classifier.recommender import api_call


@api_view(["post"])
def recommendation(request):

    return Response(api_call(request.body))
