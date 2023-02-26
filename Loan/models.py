from django.db import models

# Create your models here.

class PersonalData(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    Surname = models.CharField(max_length=100)
    FirstName = models.TextField(max_length=999)
    OtherName = models.CharField(max_length=20)
    Gender = models.IntegerField(choices=GENDER_CHOICES)
    MaritalStatus = models.CharField(max_length=20)
    Profession = models.CharField(max_length=30)
    TotalChildren = models.IntegerField()
    ResidentialStatus = models.CharField(max_length=11)
    HouseNumber = models.CharField(max_length=20)
    DigitalAddress = models.TextField(max_length=11,default="cx-152-521 or Pt189/16")
    NearestLandMark = models.CharField(max_length=999, default="Kasoa Marketplace")
    MobileNumber = models.CharField(max_length=15,default= "+233000000000")
    Email = models.EmailField(default="joy@gmail.com", blank=True)
    Religion = models.CharField(max_length=100,default= "Christian Religion")
    ReligiousLeaderNameAndNumber = models.CharField(max_length=100, default= "Name +23300000000")
    DateTime = models.DateTimeField()

    #def_str_(self):
    #    return self.Surname

class SpouseDetail(models.Model):
    Name = models.CharField(max_length=100)
    SpouseName = models.CharField(max_length=11)
    Profession = models.CharField(max_length=11)
    Position = models.CharField(max_length=11)
    Mobile = models.CharField(max_length=11)
    Proffered_Repayment_Date = models.DateTimeField()


class LoanDetail(models.Model):
    Name = models.CharField(max_length=100)
    Loan_Amount = models.FloatField()
    Loan_Amount = models.FloatField()
    Purpose = models.TextField()
    Loan_Duration_Period = models.CharField(max_length=99, default= '3months, 4months, 5months, 6months, 24months, Others' )
    Mode_Of_Payment = models.TextField(default= 'post dated check, Ach direct Mandate, Cash, Momo')
    Proffered_Repayment_Date = models.DateTimeField()

class AccountDetail(models.Model):
    Name = models.CharField(max_length=100)
    ID_Image = models.ImageField(upload_to='uploads/')
    ID_Number = models.CharField(max_length=100,default= 'GHAXXXXXX')
    Signature = models.BooleanField(default=False)
    Guarantor_Name = models.CharField(max_length=100)
    Generator_ID = models.ImageField(upload_to='uploads/')
    Guarantor_ID_Number = models.CharField(max_length= 30,default= 'GHAXXXXXX')
    Pre_Contract_Agreement = models.TextField(max_length=100000,default='I,.............................................. agree that if my loan application is successful, the following will apply to a. Intrest shall be ____% per month/annum-flat/reducing /n b. Loan shall subject a full repayment on demand at any time /n c. I event of any default, a penal intrest Rate of 2% per month shall be applied above /n 1. Early payment of loan is permitted to subject replacement of outstanding principal amount defaults in making two installment repayment')
    Upload_Contract_agreement_Form = models.ImageField(upload_to='uploads/')
    Date = models.DateTimeField()

class GuarantorDetail(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    #Declaration1 = "I __________________ understand that by endorsing this application, I shall share full responsiblity with Applicant for the replacement of this loan as agreed"
    Relationship_with_Applicant = models.CharField(max_length=10, default='Co Worker, Emlpoyer, Friend, Relatives')
    Surname = models.CharField(max_length=100)
    FirstName = models.TextField(max_length=999)
    OtherName = models.CharField(max_length=20)
    Profession = models.CharField(max_length=30)
    Position = models.CharField(max_length=30)
    ResidentialStatus = models.CharField(max_length=11)
    HouseNumber = models.CharField(max_length=20)
    DigitalAddress = models.TextField(max_length=11,default="cx-152-521 or Pt189/16")
    NearestLandMark = models.CharField(max_length=999, default="Kasoa Marketplace")
    MobileNumber = models.CharField(max_length=15,default= "+233000000000")
    Email = models.EmailField(default="joy@gmail.com", blank=True)
    Gender = models.IntegerField(choices=GENDER_CHOICES)
    DateTime = models.DateTimeField()