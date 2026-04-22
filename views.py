from django.shortcuts import render
from django.http import HttpResponse
# from mtapp.models import Student, Scorelist
from myapp.models import *
from django.forms.models import model_to_dict

def test(request):
    #     return HttpResponse("Hello")







# datas = Student.objects.all() #querySet內是Student物件
    # # print(type(datas))
    # for data in datas:
    #     # print(type(data))
    #     print(model_to_dict(data)) #物件轉成字典格式
    ############################################
    # datas = Student.objects.values('cSex').distinct()
    # for data in datas:
    #     # print(type(data))#dict
    #     print(data)
    ############################################
# datas = Student.objects.values('cSex').distinct()
# for data in datas:
#         # print(type(data))#dict
#         print(data)
    ############################################
    # 想要由 students 資料表中找出座號大於 5 的男生
    #__get #greater
    #
    # datas = Student.objects.filter(cID__gt=5,cSex='F')
    # for data in datas:
    #     # print(data)
    #     print(model_to_dict(data))
    ############################################
    from django.db.models import Q
    # datas = Student.objects.filter(
    #     ~Q(cID__gt=5) & Q(cSex='M')
    # )
    # for data in datas:
    #     #print(data)
    #     print(model_to_dict(data))

    # datas = Student.objects.filter(
    #     Q(cID=1) | Q(cID__gte=8)
    # )
    # for data in datas:
    #     # print(data)
    #     print(model_to_dict(data))
    ############################################
    # 由 students 資料表中找出座號大於等於 4 且小於等於 6 的學生資料
    # datas = Student.objects.filter(cID__range=[4,6])

    # for data in datas:
    #     #print(data)
    #     print(model_to_dict(data))
    ############################################
    # 想要由 students 資料表中找出座號為 1,3,5,7,9 的學生資料
    # datas = Student.objects.filter(cID__in=[1,3,5,7,9])
    # for data in datas:
    #     #print(data)
    #     print(model_to_dict(data))
    ############################################
    #想要由 students 資料表中，出電話號碼是「0918」開頭的學生資料
    # datas = Student.objects.filter(cAddr__contains='建國')
    # for dat



    ############################################
    #想要由 students 資料表中，找出學生的地址中有「建國」這個字的資料
    # datas = Student.objects.filter(cAddr__contains='建國')
    # for data in datas:
        # print
        # print(model_to_dict(data))
    ############################################
    # 想要由 students 資料表所有同學的資料依生日遞減排序
    # datas = Student.objects.all().order_by('-cBirthday')
    # for data in datas:
    #     print(data)
    #     print(model_to_dict(data))
    ############################################
    # 前5筆資料
    # datas = Student.objects.all()[:5] #前5筆資料
    # datas = Student.objects.all()[0:5] #第0筆到第4筆之間
    # datas = Student.objects.all()[3:7] #第3筆到第6筆資料
    # for data in datas:
        # print(data)
    #    print(model_to_dict(data))
    ############################################
    # 想要算出全班國文、英文及數學總分
    # from django.db.models import Sum,Count,Max,Min,Avg
    # data = Scorelist.objects.aggregate(Sum('score'))
    # print(data)
    ############################################
    # 想要算出全班國文總分
    # data = Scorelist.objects.filter(course='國文').aggregate(Sum('score'))
    # data = Scorelist.objects.filter(course='國文').aggregate(Avg('score'))
    # print
    ############################################
    # 由 students 資料表統計全班人數
    # data = Student.objects.aggregate(Count('cID'))
    # print(data)
    ############################################
    # 找出全班國文最高分
    # data = Scorelist.objects.filter(course='國文').aggregate(Max('score'))
    # print(data)
    ############################################
    # 想要顯示每個學生的總分
    # datas = Scorelist.objects.values_list('cID').annotate(Sum('score'))
    # for data in datas:
    #     print(data) #tuple
    ############################################
    # 想要顯示座號 1 到 5 同學的分數總計
    # datas = Scorelist.objects.filter(cID__lte=5).values_list('cID').annotate(Sum('score'))
    # for data in data in datas:
    #     print(data) #tuple
    ############################################
    # add
    # 第一種
    # student_exists = Student.objects.filter(cName="bill1").exists()
    # if not student_exists:
    #     add = Student(cName='bill1',cSex='M',cBirthday='2021-08-08',
    #                   cEmail='bill1@gmail.com',cPhone='09111111',
    #                   cAddr = '新竹', cHeight=180, cWeight=70
    #                   )
    #     add.save()
    #     print("新增成功")
    # else:
    #     print("已存在")
    # 第二種
    # student_exists = Student.objects.filter(cName="bill2").exists()
    # if not student_exists:
    #     Student.objects.create(cName='bill1',cSex='M',cBirthday='2021-08-08',
    #                   cEmail='bill1@gmail.com',cPhone='09111111',
    #                   cAddr = '新竹', cHeight=180, cWeight=70
    #                   )
    #     print("新增成功")
    # else:
    #     print("已存在")
    ############################################
    # update
    # try:
    #     update = Student.objects.get(cID=11)
    #     update.cHeight = 160
    #     update.cHeight = 71
    #     update.save()
    #     print("修改成功")
    # except:
    #     print("沒有此學員")
    ############################################
    # delete
    # delete_students = Student.objects.filter(cID__lte=2)
    # if delete_students.exists():
    #     delete_students.delete()
    #     print("刪除成功")
    # else:
    #     print("沒有此學員")
    ############################################
    # 若學生已建立，直接建立成績資料
    # try:
    #     Student_data = Student.objects.get(cName='bill1')
    #     geography_score = Scorelist(cID=Student_data, course='國文').exists()
    #     if not geography_exists:
    #         Scorelist.objects.create(cID=Student_data, course='國文', score=0)
    #         print("國文成績新增成功")
    #     else:
    #         print("國文成績已存在")
    # except:
    #     print("沒有此學員")
    ############################################
    # try:
    #     Student_data = Student.objects.get(cID=3)
    #     course_exists = Scorelist.objects.filter(cID=Student_data, course='英文').exists()
    ############################################
    try:
        student_data = Student.objects.get(cName='簡奉君')
        course_exists = Scorelist.objects.filter(cID=student_data, course='國文').exists()
        if course_exists:
            Scorelist.objects.filter(cID=student_data, course='國文').delete()
            print("國文成績修改成功")



    return HttpResponse("Hello world!")




                                                                                            