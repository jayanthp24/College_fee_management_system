from django.contrib import admin
from .models import Stud_PD,Adm_Types,Courses,Branches,Quota_List,Fee_Str,Stud_Admn,Stud_Fees,Fee_Record,F_Teach_Nonteach,Faculty

admin.site.register(Adm_Types)
admin.site.register(Courses)
admin.site.register(Quota_List)
admin.site.register(Branches)
admin.site.register(Stud_PD)
admin.site.register(Fee_Str)
admin.site.register(Stud_Admn)
admin.site.register(F_Teach_Nonteach)
admin.site.register(Faculty)
admin.site.register(Fee_Record)
admin.site.register(Stud_Fees)


