from django.shortcuts import render
# from .models import Letting, Profile


# General home page of the website.
def index(request):
    return render(request, 'index.html')


def page_not_found(request, exception):
    return render(request, '404.html', status=404)

# def page_not_found(request, exception):
#     response = render(request, "404.html", {})
#     response.status_code = 404
#     return response


def server_error(request):
    return render(request, '500.html', status=500)

# def server_error(request, exception=None):
#     response = render(request, "500.html", {
#         'exception': exception
#     })
#     response.status_code = 500
#     return response


def hello_world_error(request):
    raise Exception('This is a test error')


# # Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit. Sed non placerat
# massa. Integer est nunc, pulvinar a
# # tempor et, bibendum id arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices
# posuere cubilia curae; Cras eget scelerisque
# def lettings_index(request):
#     lettings_list = Letting.objects.all()
#     context = {'lettings_list': lettings_list}
#     return render(request, 'lettings_index.html', context)


# #Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl id
# eleifend. Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu, vitae
# efficitur
# #  lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas auctor, est ut
# luctus congue, dui enim mattis enim, ac condimentum velit libero in magna. Suspendisse potenti.
# In tempus a nisi sed laoreet.
# # Suspendisse porta dui eget sem accumsan interdum. Ut quis urna pellentesque justo mattis
# ullamcorper ac non tellus. In tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus. Mauris condimentum
# auctor elementum. Donec quis nisi ligula. Integer vehicula tincidunt enim, ac lacinia augue
# pulvinar sit amet.
# def letting(request, letting_id):
#     letting = Letting.objects.get(id=letting_id)
#     context = {
#         'title': letting.title,
#         'address': letting.address,
#     }
#     return render(request, 'letting.html', context)

# # Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc
# # faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d
# def profiles_index(request):
#     profiles_list = Profile.objects.all()
#     context = {'profiles_list': profiles_list}
#     return render(request, 'profiles_index.html', context)

# # Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# # laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt,
# dolor id facilisis fringilla, eros leo tristique lacus,
# # it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et netus et
# males
# def profile(request, username):
#     profile = Profile.objects.get(user__username=username)
#     context = {'profile': profile}
#     return render(request, 'profile.html', context)
