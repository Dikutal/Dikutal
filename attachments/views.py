from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from attachments.forms import AttachmentForm

from attachments.models import Attachment

from datetime import datetime

def attachments_index(request):
    return render_to_response('attachments/index.html', RequestContext(request, {}))

def view(request, id):
    attachment = get_object_or_404(Attachment, pk=id)
    return render_to_response('attachments/view.html', RequestContext(request, {
        'attachment': attachment,
        'subtitle': 'Attachments'
    }))

@login_required
@csrf_protect
def attachments_create(request):
    if request.POST:
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            attachment = form.save(commit=False)
            attachment.save()
            return redirect(attachment)
    else:
        form = AttachmentForm()

    return render_to_response('attachments/create.html', RequestContext(request, {
        'form': form,
        'subtitle': 'Upload attachments'
    }))


@login_required
@csrf_protect
def attachments_edit(request, id):
    attachment = get_object_or_404(Attachment, pk=id)

    if not attachment.can_edit(request.user):
        return HttpResponseForbidden()

    if request.POST:
        form = AttachmentForm(request.POST, request.FILES, instance=attachment)
        if form.is_valid():
            attachment = form.save(commit=False)
            attachment.save()
            return redirect(attachment)
    else:
        form = AttachmentForm(instance=attachment)

    return render_to_response('attachments/edit.html', RequestContext(request, {
        'form': form,
        'subtitle': 'Edit attachments'
    }))

