##from django.contrib import admin

# Register your models here.
#from . models import Invoice

##from .models import Owner,InvoiceSale,InvoiceType
 




##@admin.register(Owner)
##class OwnerAdmin(admin.ModelAdmin):
##    list_display = ("owner_id", "first_name", "last_name")
##    ordering = ("first_name", "last_name")
 

##@admin.register(InvoiceSale)
##class InvoiceSales(admin.ModelAdmin):
##    pass
 
##@admin.register(InvoiceType)
##class InvoiceType(admin.ModelAdmin):
##    list_display = ("make", "model", "year", "color", "price")
    ##list_filter = ("year",)
  ##  search_fields = ["make", "model"]
   ## ordering = ("make", "model")
    ##fieldsets = (
     ##   (
      ##      "Required Information", {
       ##         # Section Description
        ##        "description" : "Enter the vehicle information",
         ##       # Group Make and Model
          ##      "fields": (("make", "model"), "color", "price", "year")
           ## }
        ##),
       ## (
        ##    "Additional Information", {
                # Section Description
##                "description" : "Enter any additional information",
                #Enable a Collapsible Section
  ##              "classes": ("collapse",), 
    ##            "fields": ("description",)
      ##      }
        ##)
   ## )


#admin.site.register(Invoice,InvoiceAdmin)