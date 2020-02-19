# from django.shortcuts import render
# from django.http import HttpResponse, Http404, HttpResponseRedirect
# # from django.template import loader

# from django.shortcuts import render, get_object_or_404
# from django.urls import reverse
# from django.views import generic
# from rest_framework.views import APIView
# from rest_framework.generics import ListCreateAPIView
# from rest_framework.response import Response

# from .models import Question, Choice, Chat, Post
# from .serializers import PostSerializer, ChatSerializer

from django.shortcuts import render

def index(request):
    return render(request, 'chats/index.html', {})

# class PostListView(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class ChatListView(ListCreateAPIView):
#     queryset = Chat.objects.all()
#     serializer_class = ChatSerializer

# class PostView(APIView):
#     def post(self, request):
#         entry = request.data
#         print(entry)
#         proxy = PostSerializer(data=entry)
#         if proxy.is_valid():
#             return Response(entry, status=201)
#         return Response(proxy.errors, status=422)
    


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('chats/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
#     # output = ','.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'chats/detail.html',

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))