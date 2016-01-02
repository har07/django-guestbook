# django-guestbook
Sample Django project created using Visual Studio 2015 and Google App Engine SDK. 
Specifically, this is Guestbook sample application based on the official Python Google App Engine [documentation](https://cloud.google.com/appengine/docs/python/gettingstartedpython27/introduction). 
In fact, this project is sooo simple that you can (and I plan to) use it as template for new Django App Engine project.


- Feel the convinience of coding Python with Visual Studio *Intellisense* and debugging features
- Deploy your application to the Google App Engine cloud platform and see it up and running online. Straightforward deployment and free hosting* *#yaaay!* 

Created on Windows 10 using :
-------
- Visual Studio 2015 Update 1 Community Edition ([Visual Studio Community page](https://www.visualstudio.com/en-us/products/visual-studio-community-vs.aspx))
- PTVS 2.2.2 ([releases page](https://github.com/microsoft/ptvs/releases))
- Anaconda2 2.4.0 64-bit ([download page](https://www.continuum.io/downloads#_windows))
- Google App Engine SDK 1.9.30 ([download page](https://cloud.google.com/appengine/downloads))
- Django 1.9 (run command: `pip install django`. See Django [documentation](https://docs.djangoproject.com/en/1.9/howto/windows/) for more details)

Step by step for debugging this project using Visual Studio 2015 :
------------
- Fork or download this Django Guestbook project source code
- Open DjangoGAE.sln and Run (Debug) the project
- When a new browser tab/window opened, press CTRL+ALT+P on the Visual Studio. That will open 'Attach to Process' dialog.
- On the 'Attach to Process' dialog, select 'Python remote (ptvsd)' for Transport and 'tcp://har07@localhost:5678' for Qualifier, and then click 'Attach'.
- Qualifier argument is configurable as 'secret' key in pydevd_startup.py file

[![enter image description here][1]][1]

References :
- StackOverflow. [Debugging GAE in Python Tools for Visual Studio](http://stackoverflow.com/questions/17633045/debugging-gae-in-python-tools-for-visual-studio)
- [Django on Google App Engine series](http://django-appengine.com/) (with some modifications to make it work with the newer Django version 1.9)


  [1]: http://i.stack.imgur.com/8Bouw.png


