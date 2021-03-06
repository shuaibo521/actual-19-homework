from django.shortcuts import render
from .models import Assets
# Create your views here.


def assetsView(request):
    objs = Assets.objects.all()
    return render(request, "assets.html", context= {'objs' : objs})



def deleteAssetsView(request):
    pk = request.GET.get("pk")
    obj = Assets.objects.get(pk=pk)
    obj.delete()
    return HttpResponse("Delete {} ok".format(obj.hostname))

def addAssetsView(request):
    hostname = request.GET.get("hostname")
    private_ip = request.GET.get("private_ip")
    public_ip = request.GET.get("public_ip")
    cpu_num = request.GET.get("cpu_num")
    cpu_model = request.GET.get("cpu_model")
    mem_total = request.GET.get("mem_total")
    disk = request.GET.get("disk")
    os_system = request.GET.get("os_system")
    status = request.GET.get("status")
    frame = request.GET.get("frame")
    create_time = request.GET.get("create_time")
    update_time = request.GET.get("update_time")
    remark = request.GET.get("remark")
    op = request.GET.get("op")
    remote_ip = request.GET.get("remote_ip")
    service_line = request.GET.get("service_line")

    data = {'hostname': hostname,
            'private_ip': private_ip,
            'public_ip': public_ip,
            'cpu_num': cpu_num,
            'cpu_model': cpu_model,
            'mem_total': mem_total,
            'disk': disk,
            'os_system': os_system,
            'status': status,
            'frame': frame,
            'create_time': create_time,
            'update_time': update_time,
            'remark': remark,
            'op': op,
            'remote_ip': remote_ip,
            'service_line': service_line,
            }
    Assets.objects.create(**data)
    return HttpResponse("Insert {} ok".format(data['hostname']))


#
def addPageAssetsView(request):
# def addAssetsView(request):
    return render(request, "assets_add_page.html")
