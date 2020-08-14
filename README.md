## FontAwesome
* **Determining which Package an Icon Belongs To**

    1. Solid Style - **fas**
    2. Regular Style - **far**
    3. Light Style - **fal**
    4. Duotone Style - **fad**


    ### Delete all data in a table
* ```./manage.py shell```
* ```from <APPNAME>.models import tableName```
* ```tableName.objects.all().delete()```


#### Querying
* ```./manage.py shell```
* ```from clients.models import Purchaser, paymentInvoice```
* ```queryset = paymentInvoice.objects.filter(invoiceOwner__name__contains="Becky").first()```
        + ``Returns 1st instance`` 
* ```queryset```

* ```queryset = paymentInvoice.objects.filter(invoiceOwner__name__contains="Becky").exists()```
        + ``Returns boolean``