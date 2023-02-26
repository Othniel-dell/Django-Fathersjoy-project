from django.contrib import admin

# Register your models here.

from .models import PersonalData,LoanDetail,SpouseDetail,AccountDetail,GuarantorDetail


class PersonalAdmin(admin.ModelAdmin):
    list_display = ('FirstName','Profession','DigitalAddress','ResidentialStatus','DateTime')

admin.site.register(PersonalData,PersonalAdmin)


class LoanAdmin(admin.ModelAdmin):
    list_display = ('Name','Loan_Amount','Purpose','Loan_Duration_Period','Mode_Of_Payment','Proffered_Repayment_Date')


admin.site.register(LoanDetail,LoanAdmin)


class SpouseAdmin(admin.ModelAdmin):
    list_display = ('SpouseName','Profession','Position','Mobile')


admin.site.register(SpouseDetail,SpouseAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display = ('Name','ID_Number','Guarantor_Name','Guarantor_ID_Number')


admin.site.register(AccountDetail,AccountAdmin)


class GuarantorAdmin(admin.ModelAdmin):
    list_display = ('FirstName','Surname','HouseNumber','ResidentialStatus','MobileNumber')


admin.site.register(GuarantorDetail,GuarantorAdmin)