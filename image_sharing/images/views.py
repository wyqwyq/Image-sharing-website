from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from django.shortcuts import get_object_or_404
from .models import Image
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # 数据合法
            cd = form.cleaned_data
            # 先下载在本地存好图片
            new_item = form.save(commit=False)
            # 绑定登入的user
            new_item.user = request.user
            # Image对象存储
            new_item.save()
            messages.success(request, '图片成功添加！')
            # 重定向到image对象的详细情况的url
            return redirect(new_item.get_absolute_url())
    else:
        # js工具发出GET方法，会传入参数，构造出form
        form = ImageCreateForm(data=request.GET)
    return render(request,
                  'images/image/create.html',
                  {'section': 'images',
                  'form': form})
                  
                  

def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request,
                 'images/image/detail.html',
                 {'section': 'images',
                 'image': image})


@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'not-ok'})

@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # 如果不是整数，从第一页开始
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # s是ajax，越界，返回空页
            return HttpResponse('')
        # 非ajax，越界返回最后一页
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                     'images/image/list_ajax.html',
                     {'section': 'images', 'images': images})
    return render(request,
                  'images/image/list.html',
                  {'section': 'images', 'images': images})
