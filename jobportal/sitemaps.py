from django.contrib.sitemaps import Sitemap
from django.urls  import reverse
from .models import PostedJob
from django.utils.text import slugify


class StaticViewSitemap(Sitemap):

    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['aboutus', 'contactus']

    def location(self, item):
        return reverse(item)


class applyjobSitemap(Sitemap):

    def items(self):
        return PostedJob.objects.all()
    
    # def location(self, item):              
    #      return reverse('applyjob', args=[item.id])


    def location(self,obj):
         title=obj.jobtitle
         id=obj.id            
         return '/jobs-in-singapore/%s/%d' %(slugify(title),id)   

    def lastmod(self, obj):
	     return obj.date_posted
    
   