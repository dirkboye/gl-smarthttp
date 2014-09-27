gl-smarthttp
============

Gitolite Smart HTTP Pull/Push on Uberspace

With this Python script you can enable Smart HTTP Pull/Push including Gitolite's user management.

### Installation:
Inside your html path create a directory "git" and chmod 755 on it:
```
mkdir ~/html/git
chmod 755 ~/html/git
```
Copy .htaccess and gl.py into that directory. Make gl.py executable:
```
chmod a+x ~/html/git/gl.py
```
Check .htaccess for path of __.htpasswd__ file. The usernames defined in that .htpasswd will be the usernames
gitolite will see for its permission checks. If a user has only R access in your gitolite.conf to one of the repositories he will only be able to checkout the repository without the right to push back.

Opening https://user.server.uberspace.de/git/gl.py in your browser will give you a list of repositories that
you have access to (depending on your permissions).

You can now checkout your repositories with following command:
```
git clone https://user.server.uberspace.de/git/gl.py/repo.git
```


### Anonymous access:
Anonymous access is also possible. Edit file __~/.gitolite.rc__ and uncomment following line:
```
$GL_HTTP_ANON_USER = "mob";
```
Do the same as above with another directory "gitmob":
```
mkdir ~/html/gitmob
chmod 755 ~/html/gitmob
```
Copy .htaccess and gl.py into that directory as well.
This time remove the user requirement from the .htaccess file. Now any user cloning repos with
```
git clone https://user.server.uberspace.de/gitmob/gl.py/repo.git
```
will be identified as user "mob" to gitolite (without any need for pw etc). In your gitolite.conf put R access for user __mob__ to the repositories that you'd like to allow anonymous access to.

### Drawbacks
When gitolite encounters an error (permission denied for example) the response header is missing following line:
```
Content-Type: application/x-git-service-advertisement
```
As a result of that, when trying to clone a repository without permissions, you'll get an error "this is not a git repository" instead of "access denied". 

This should be fixed in a newer version of gitolite.
