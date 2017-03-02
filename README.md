Example project to demonstrate how to build a simple app on Google App Engine, using a microservice architecture.

First install default service Python libraries
```
cd default
pip install -t lib -r requirements.txt
```

Deploy the services
```
gcloud app deploy default/app.yaml
gcloud app deploy dummy/app.yaml movie/app.yaml user/app.yaml
```

Deploying the first service by itself is on purpose, to give it another version name.
This is done so that the get_hostname function returns the default version for the other services.
You can read more about how it works [here](https://cloud.google.com/appengine/docs/standard/python/refdocs/google.appengine.api.modules.modules#google.appengine.api.modules.modules.get_hostname).


This app is available for demonstration on [http://poc-microservices.appspot.com](http://poc-microservices.appspot.com)