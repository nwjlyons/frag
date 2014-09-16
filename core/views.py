from urlparse import urljoin

from bs4 import BeautifulSoup
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.http import is_safe_url
import requests

from forms import FragForm

jquery = BeautifulSoup('<script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>')
script = BeautifulSoup("""
<script>
$(function(){

    $("[id]").click(function(event){
        event.stopPropagation();
        window.location.hash = $(this).attr("id");
    })

});
</script>""")
style = BeautifulSoup("""
<style>
[id]:hover {outline: 1px solid red;}
</style>""")


def home(request):

    if "url" in request.GET:
        form = FragForm(request.GET)
        if form.is_valid():
            url = form.cleaned_data["url"]
            response = requests.get(url)
            if response.ok:

                soup = BeautifulSoup(response.content)

                count = 0
                for element in soup.select("body *"):
                    if "id" not in element.attrs or element.attrs["id"] == "":
                        element["id"] = "frag-%s" % count
                    count += 1

                def absoulte_urls(attribute_key):
                    for element in soup.select("[%s]" % attribute_key):
                        path = element.attrs[attribute_key]
                        if not len([prefix for prefix in ["http", "https", "//"] if path.startswith(prefix)]):
                            element.attrs[attribute_key] = urljoin(url, path)

                absoulte_urls("src")
                absoulte_urls("href")

                if "HTTP_REFERER" in request.META and is_safe_url(request.META["HTTP_REFERER"], request.get_host()):
                    soup.head.insert(len(soup.head.contents), style)
                    soup.head.insert(len(soup.head.contents), jquery)
                    soup.head.insert(len(soup.head.contents), script)

                return HttpResponse(str(soup))
            else:
                messages.warning(request, "Error fetching page.")
    else:
        form = FragForm()

    return render(request, "home.html", {
        "form": form,
    })
