* **Get** product data

    + ``./manage.py dumpdata products.Product --indent 2 > backup_data/products.json``

`` **GET ALL** data 

* **Restore** data for a specific app

    + ``python manage.py loaddata --app Product products.json``
