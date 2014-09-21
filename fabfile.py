import datetime

from fabric.api import *


env.roledefs.update({
    'webserver': ['nwjlyons@nwjlyons.webfactional.com'],
})
env.project_root = "/home/nwjlyons/webapps/frag"
env.forward_agent = True
env.warn_only=True


@task
@roles("webserver")
def deploy():
    """
    Deploy to web server.
    """
    # local("git checkout master")
    # local("git push")

    # utc_datetime = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")

    # local("git tag -a deploy-%s -m 'Deployed'" % utc_datetime)
    # local('git push --tags')

    with cd(env.project_root):

        with cd("frag"):
            o = run("git pull")
            if "package.json" in o:
                run("npm install")

            if "bower.json" in o:
                run("node_modules/bower/bin/bower install")

            if "requirements.txt" in o:
                run("workon frag && pip install -r requirements.txt")

            run("workon frag && ./manage.py collectstatic --noinput")
            run("workon frag && ./manage.py migrate")

        run("./apache2/bin/restart")
