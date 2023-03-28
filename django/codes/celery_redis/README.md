## Important Commands
install redis server
~~~
brew install redis
~~~
run redis server
~~~
redis-server
~~~
run celery worker
~~~
celery -A project_name_here worker -l INFO
~~~
run celery worker in background
~~~
celery multi start worker_name_here -A project_name_here -l INFO
~~~
restart worker 
~~~
celery multi restart worker_name_here -A project_name_here -l INFO
~~~

## Important Links
~~~
https://realpython.com/asynchronous-tasks-with-django-and-celery/
~~~
~~~
https://vedantsopinions.medium.com/how-we-scaled-celery-for-our-django-app-da2465a3a6be
~~~
### Redis
It is message broker in celery


### Celery Architecture
task -> message broker -> worker 
- task
any celery task e.g sending emails to users
- broker 
used to communicate messages between Django project (producer) and 
workers (consumers)
- worker
used to execute celery tasks

### Use cases
- Think of all the times you have had to run a certain task in the future. 
Perhaps you needed to access an API every hour. Or maybe you needed to send 
a batch of emails at the end of the day. Large or small, Celery makes 
scheduling such periodic tasks easy.

- You never want end users to have to wait unnecessarily for pages to load 
or actions to complete. If a long process is part of your application’s 
workflow, you can use Celery to execute that process in the background, 
as resources become available, so that your application can continue to 
respond to client requests. This keeps the task out of the application’s 
context.