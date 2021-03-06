#!/usr/bin/env python2.7
import cgi
import cgitb; cgitb.enable()
import pwd, sys, os, subprocess
from os.path import expanduser
home_dir = expanduser("~")
os.environ['HOME'] = home_dir
os.environ['GIT_PROJECT_ROOT'] = home_dir + '/repositories'
os.environ['GITOLITE_HTTP_HOME'] = home_dir
os.environ['GIT_HTTP_BACKEND'] = '/usr/libexec/git-core/git-http-backend'
os.environ['GIT_HTTP_EXPORT_ALL'] = ''
path = os.environ['PATH_INFO']
if (path == "/"):
        # Add additional content type header so the information is displayed in the browser
        # This only works for text output from gl-auth-command and cannot be user for git streams
        print "Content-Type: text-html"
        p = subprocess.Popen("/usr/bin/gl-auth-command", stdout=subprocess.PIPE)
        out, err = p.communicate()
        print out
else:
        subprocess.call("/usr/bin/gl-auth-command")
