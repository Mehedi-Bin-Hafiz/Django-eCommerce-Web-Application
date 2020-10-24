**_The get_object_or_404()_** 

function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the model's manager. It raises Http404 if the object doesn't exist. ... It raises Http404 if the list is empty.