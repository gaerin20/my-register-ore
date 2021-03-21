from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils import timezone
from .models import Post

# Create your views here.
@login_required
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})
@login_required
def listing(request):
        data = {
                "blogs" : Post.objects.all(),
        }
        return render(request, "blog/listing.html" , data)
@login_required
def view_blog(request, blog_id):
        blog = get_object_or_404(Post, id=blog_id)
        data = {
                "blog":blog,
        }
        return render(request, "blog/view_blog.html" , data)

def see_request(request):
        text=f"""
                Alcuni attributi dell'oggetto HttpRequest:
                scheme: {request.scheme}
                path: {request.path}
                method: {request.method}
                GET: {request.path}
                user: {request.user}
                Seguono attributi del Httprequest.user
                username: {request.user.username}
                is_anonymous: {request.user.is_anonymous}
                is_staff: {request.user.is_staff}
                is_superuser: {request.user.is_superuser}
                is_active: {request.user.is_active}
        """
        return HttpResponse(text, content_type="text/plain")

@login_required
def spazio_privato(request):
        return HttpResponse("Shhh! Questo spazio è riservato ai soli autorizzati", content_type="text/plain")
                
@user_passes_test(lambda user: user.is_staff)
def staff_place(request):
        return HttpResponse("I dipendendi devono lavarsi le mani", content_type="text/plain")
@login_required
def add_messages(request):
        username = request.user.username
        messages.add_message(request, messages.INFO, f"Ciao {username}")
        messages.add_messsage(request, messages.WARNING, "DANGER WILL ROBINSON")
        return HttpResponse("Messages added", content_type="text/plain")
