Django Todo App in Docker with PyCharm
======================================

This is an example project for a 
[blog post on the PyCharm blog](http://blog.jetbrains.com/pycharm/2017/08/using-docker-compose-on-windows-in-pycharm).
Please read more about it there.

To run the project, set up a Django compatible database (I use PostgreSQL but you're welcome to use something else)
and configure it in `djangodocker/settings.py`. 

How to run project:


**_Use the Docker tool window:_**

When you have configured Docker, the Services tool window appears at the bottom of PyCharm's main window. 
You can click "docker-compose up" in the gutter next to the services group to launch db and web services.


**_Run the application:_**

1. Select Tools | Run 'manage.py' task from the main menu and enter migrate to run a migration and execute a Django application.
2. Create a Run/Debug configuration for the Django server. To do that, select Run | Edit Configurations from the main menu.
In the Run/Debug Configurations dialog, click Add Run/Debug configuration for a Django Server Add New Configuration and select Django Server.
3. Set the Host field to 0.0.0.0 to ensure that the Docker container is open to external requests. 
4. To run the newly created configuration, select Run | Run 'RunDjangoApp' from the main menu.

To see the output in your web browser, go to http://localhost:8000:


**_Debug the application:_**

With the Run/Debug configuration created, you can also debug your application.

1. Set a breakpoint (for a Django application, you can set it in a template).
2. Do one of the following:
   - Select Run | Debug 'RunDjangoApp' from the main menu. 
   - Click Start Debugger Debug next to the Run/Debug configuration drop-down with the RunDjangoApp configuration selected.

For more information about debugging application in a container, refer to Debugging in a Docker container.

------------------------------------------------------------------------------------------------------------

TODO: 
- [ ] migrate to latest Django version
- [ ] update Dockerfile to use latest Python version
- [ ] update Dockerfile to use latest PostgreSQL version