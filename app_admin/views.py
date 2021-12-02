from django.shortcuts import render, redirect
from accounts.models import Member, Spouse, Family
from .filters import MemberFlilter
# Pagination stuff
from django.core.paginator import Paginator
# forms
from .forms import AddMemberPayment, UpdateMemberForm, UpdatePendingMemberForm, AdminMemberCreationForm
from django.contrib.auth.models import Group
# Messages
from django.contrib import messages
# Admin Authentication Stuff
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only


# Register
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def registerNewMember(request):

    form = AdminMemberCreationForm()
    if request.method == 'POST':
        form = AdminMemberCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='member')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

        else:
            form = AdminMemberCreationForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


# Admin List Members
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def allMembers(request):
    member = Member.objects.all().order_by('-created')

    # Filter
    myFilter = MemberFlilter(request.GET, queryset=member)
    member = myFilter.qs

    # Pagination with Search Filter
    p = Paginator(myFilter.qs, 4)
    page = request.GET.get('page')
    members = p.get_page(page)

    context = {'myFilter': myFilter, 'member': member, 'members': members}
    return render(request, 'app-admin/all-members.html', context)


# Admin Members Detail View
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def showprofiledetails(request, profile_id):
    display_profile = Member.objects.get(id=profile_id)
    member = Member.objects.get(id=profile_id)

    return render(request, 'app-admin/ShowProfileDetails.html', {
        'display': display_profile,
        'member': member
    })


# Admin Update Member
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def UpdateMemberAdmin(request, slug_id):

    # Getting data from the form id=pk ,instance=form
    member = Member.objects.get(slug=slug_id)
    form = UpdateMemberForm(instance=member)

    # Saving updated form to database
    if request.method == 'POST':
        form = UpdateMemberForm(request.POST or None,
                                request.FILES or None,
                                instance=member)
        if form.is_valid():
            form.save()
            return redirect('all-members')

    context = {'form': form, 'member': member}
    return render(request, 'app-admin/update_member.html', context)


# Admin Member Search
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def search_member(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        # membership_no = foregnkey field + id_number = foregnkey value
        # members = MembershipNumber.objects.filter(id_number__contains=searched)
        members = Member.objects.filter(id_number__contains=searched)

        context = {'searched': searched, 'members': members}

        return render(request, 'app-admin/results.html', context)
    else:
        context = {}
        return render(request, 'app-admin/results.html', context)


# Payments
def payments(request, slug_id):
    member = Member.objects.get(slug=slug_id)

    form = AddMemberPayment

    context = {'member': member, 'form': form}

    return render(request, 'app-admin/payments.html', context)


# Admin Member Burials
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def burials(request, slug_id):
    display = Member.objects.filter(slug=slug_id)
    spouse_display = Spouse.objects.filter(slug=slug_id)
    family_display = Family.objects.filter(slug=slug_id)

    context = {
        'display': display,
        'spouse_display': spouse_display,
        'family_display': family_display
    }

    return render(request, 'app-admin/burials.html', context)


# Admin List Member Burials
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def allburials(request):
    x_member = Member.objects.filter(status='deceased').order_by('-created')
    x_spouse = Spouse.objects.filter(status='deceased').order_by('-created')
    x_family = Family.objects.filter(status='deceased').order_by('-created')
    context = {
        'x_member': x_member,
        'x_spouse': x_spouse,
        'x_family': x_family
    }

    return render(request, 'app-admin/all-burials.html', context)


####------------------------------------------- PENDING MEMBER VIEWS ------------------------------------####


# Admin Update Pending Member
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def UpdatePendingMember(request, slug_id):

    # Getting data from the form id=pk ,instance=form
    pending = Member.objects.get(status='pending', slug=slug_id)

    # member = Member.objects.get(id=slug_id)
    form = UpdatePendingMemberForm(instance=pending)

    # Saving updated form to database
    if request.method == 'POST':
        #print('Printing:', request.POST)
        form = UpdatePendingMemberForm(request.POST or None,
                                       request.FILES or None,
                                       instance=pending)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context = {'form': form, 'pending': pending}
    return render(request, 'app-admin/pending-member/pending-member-form.html',
                  context)


# Pending Member Detail View
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def PendingMemberDetail(request, slug_id):
    pending = Member.objects.get(status='pending', slug=slug_id)

    context = {
        'pending': pending,
    }
    return render(request, 'app-admin/pending-member/pending-member-view.html',
                  context)
