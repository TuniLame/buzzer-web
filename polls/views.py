# Create your views here.
from django.template import RequestContext, Context, loader # t et c
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Poll, Party
from django.http import HttpResponse

def index(request):
	# return HttpResponse("Hello, world. You're at the poll index.")
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	party = Party.objects.all()[:1]
	#output = ', '.join([p.question for p in latest_poll_list])
	#return HttpResponse (output)
	t = loader.get_template('polls/index.html')
	c = Context ({
		'latest_poll_list': latest_poll_list,
	})
	# return HttpResponse(t.render(c))
	return render_to_response ('polls/index.html',{'latest_poll_list': latest_poll_list,'party':party})
	
def detail (request,poll_id,party_id):
#	try:
#		p = Poll.objects.get(pk=poll_id)
#	except Poll.DoesNotExist:
#		raise Http404
	p = get_object_or_404(Poll,pk=poll_id)
	party = get_object_or_404(Party,pk=party_id)
	return render_to_response('polls/detail.html',{'poll':p,'party':party},context_instance=RequestContext(request))
	
	# return HttpResponse("You're looking at poll %s"% poll_id)
	
def results (request, poll_id):
	return HttpResponse("You're looking at the results of poll %s" % poll_id)
def vote(request,poll_id):
	# return HttpResponse("You're voting in poll %s"% poll_id)
	p = get_object_or_404(Poll,pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render_to_response('polls/detail.html', {
		'poll': p,
		'error_message': "You didn't select a choice.",
		}, context_instance=RequestContext(request))
	else:
		selected_choice.votes +=  1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
      # with POST data. This prevents data from being posted twice if a
      # user hits the Back button.
		return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
