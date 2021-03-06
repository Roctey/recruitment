from django.contrib import admin

# Register your models here.
from interview.models import Candidate


class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')
    list_display = (
        'username',
        'city',
        'bachelor_school',
        'first_score',
        'first_result',
        'first_interviewer_user',
        'second_score',
        'second_result',
        'second_interviewer_user',
        'hr_score',
        'hr_result',
        'hr_interviewer_user',
        'last_editor')
    fieldsets = (('基本信息',
                  {'fields': (("userid",
                               "username",
                               "city"),
                              ("phone",
                               "email",
                               "apply_position"),
                              ("born_address",
                               "gender",
                               "candidate_remark"),
                              "bachelor_school"
                              )}),
                 ('第一轮面试记录',
                  {'fields': (("first_score",
                               "first_learning_ability",
                               "first_professional_competency"),
                              ("first_advantage",
                               "first_disadvantage"),
                              "first_result",
                              "first_recommend_position",
                              "first_remark",
                              )}),
                 ('第二轮专业复试面试记录',
                  {'fields': (("second_score",
                               "second_learning_ability",
                               "second_professional_competency"),
                              ("second_pursue_of_excellence",
                               "second_communication_ability",
                               "second_pressure_score"),
                              "second_advantage",
                              "second_disadvantage",
                              "second_result",
                              "second_recommend_position",
                              "second_interviewer_user",
                              "second_remark",
                              )}),
                 ('HR复试记录',
                  {'fields': (("hr_score",
                               "hr_responsibility",
                               "hr_communication_ability"),
                              ("hr_logic_ability",
                               "hr_potential",
                               "hr_stability"),
                              "hr_advantage",
                              "hr_disadvantage",
                              "hr_result",
                              "hr_interviewer_user",
                              "last_editor",
                              )}))
    # 右侧筛选条件
    list_filter = ('city','first_result','second_result','hr_result','first_interviewer_user','second_interviewer_user','hr_interviewer_user')

    # 查询字段
    search_fields = ('username', 'phone', 'email', 'bachelor_school')


admin.site.register(Candidate, CandidateAdmin)
