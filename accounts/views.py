from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import MemberCreationForm
from accounts.models import Member, Spouse, Family
from website.models import Package
# Auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Messages #
from django.contrib import messages
# Pagination stuff
from django.core.paginator import Paginator


# Register
def registerMember(request):

    form = MemberCreationForm()
    if request.method == 'POST':
        form = MemberCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='member')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')
        else:
            form = MemberCreationForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


# Login
def loginMember(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')

        else:
            messages.info(request, 'Username OR Password is incorrect!')

    context = {}
    return render(request, 'accounts/login.html', context)


# Logout
def logoutUser(request):
    logout(request)
    return redirect('login')


# Homepage
@login_required(login_url='login')
def homepage(request):
    # Getting request user Member
    member = request.user
    # members count
    members_no = Member.objects.all().count()
    spouse = Spouse.objects.all()
    family = Family.objects.all()
    pending = Member.objects.filter(status='pending').order_by('-created')
    active = Member.objects.filter(status='active')

    # ------- Admin homepage Views --------- #
    # burials = UpcomingBurials.objects.all()
    burials = Member.objects.filter(status='deceased').last()
    spouse_burials = Spouse.objects.filter(status='deceased').last()
    family_burials = Family.objects.filter(status='deceased').last()
    members = Member.objects.order_by('-created')

    # Pending member pagination
    p = Paginator(pending, 2)
    page = request.GET.get('page')
    pending_list = p.get_page(page)

    context = {
        'member': member,
        # members count
        'spouse': spouse,
        'family': family,
        'pending': pending,
        'active': active,
        'members_no': members_no,
        # burials
        'burials': burials,
        'spouse_burials': spouse_burials,
        'family_burials': family_burials,
        # pagination
        'pending_list': pending_list,
    }
    # return render(request, 'accounts/homepage.html', context)
    return render(request, 'accounts/homepage.html', context)


# Member profile view (using slug)
@login_required(login_url='login')
def memberDetails(request, slug_id):

    display = Member.objects.get(slug=slug_id)
    context = {'display': display}
    return render(request, 'accounts/member.html', context)


# Members Package
@login_required(login_url='login')
def memberPackage(request, slug_id):

    member = Member.objects.get(slug=slug_id)
    context = {'member': member}
    return render(request, 'accounts/member-package.html', context)


# Members Documents
@login_required(login_url='login')
def memberDocuments(request, slug_id):

    member = Member.objects.get(slug=slug_id)
    context = {'member': member}
    return render(request, 'accounts/documents.html', context)


# Payments
def memberPayments(request, slug_id):
    member = Member.objects.get(slug=slug_id)
    context = {'member': member}
    return render(request, 'accounts/member-payments.html', context)
