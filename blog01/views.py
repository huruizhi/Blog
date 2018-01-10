from django.shortcuts import render, get_object_or_404
from blog01 import models
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    post_list = models.Post.objects.all().order_by('id')
    post_list, contacts, page_range = page(request, post_list)
    return render(request, 'blog01/index.html', context={'post_list': post_list, 'contacts': contacts,
                                                         'page_range': page_range})


def detail(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    md = markdown.Markdown(extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      TocExtension(slugify=slugify), ])
    post.body = md.convert(post.body)
    post.toc = md.toc
    post.auto_add_views()
    return render(request, 'blog01/detail.html', context={'post': post})


def archives(request, year, month):
    post_list = models.Post.objects.filter(created_time__year=year).filter(created_time__month=month).order_by('id')
    post_list, contacts, page_range = page(request, post_list)
    return render(request, 'blog01/index.html', context={'post_list': post_list, 'contacts': contacts,
                                                         'page_range': page_range})


def category(request, pk):
    post_list = models.Post.objects.filter(category_id=pk).order_by('id')
    post_list, contacts, page_range = page(request, post_list)
    return render(request, 'blog01/index.html', context={'post_list': post_list, 'contacts': contacts,
                                                         'page_range': page_range})


def tag(request, pk):
    tag_id = get_object_or_404(models.Tag, pk=pk)
    post_list = models.Post.objects.filter(tags=tag_id).order_by('id')
    post_list, contacts, page_range = page(request, post_list)
    return render(request, 'blog01/index.html', context={'post_list': post_list, 'contacts': contacts,
                                                         'page_range': page_range})


def page(request, post_list):
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page_rows = Paginator(post_list, 5)
    try:
        rows_list = page_rows.page(page_num)
    except PageNotAnInteger:
        rows_list = page_rows.page(1)
    except EmptyPage:
        rows_list = page_rows.page(page_rows.num_pages)
    contacts = page_rows.get_page(page_num)
    page_range = page_rows.page_range
    print(page_num)
    return rows_list.object_list, contacts, page_range
