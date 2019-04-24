haproxy
========

Installs and configures [HAProxy 1.5](http://www.haproxy.org/).

Support for HAProxy >=1.8 will be done at a later date.

Versions
--------

The **current** release is [1.3.0](https://github.com/deveryware/ansible-haproxy/tree/v1.3.0).

The  **next** release is in development (Cf. [the projects tab](https://github.com/Deveryware/ansible-haproxy/projects)).

Features
--------

* Supports CentOS and Debian (Ubuntu should work)
* Installs HAProxy from official repositories on Debian.
* Installs HAProxy from EPEL repository on CentOS.
* Tests via Molecule and Docker

Role Variables
--------------

* `haproxy_global`

    Global HAProxy settings.
* `haproxy_defaults`

    Default settings for frontends, backends, and listen proxies.
* `haproxy_resolvers`

    A list of HAProxy resolvers.
* `haproxy_backends`

    A list of HAProxy backends.
* `haproxy_frontends`

    A list of HAProxy frontends.
* `haproxy_listen`

    A list of listen proxies.

See [`vars/main.yml`](vars/main.yml) for a complete list of configurable .

Example
-------

```yaml
- hosts: loadbalancers
  roles:
     - role: haproxy
       haproxy_frontends:
       - name: 'fe-mysupersite'
         ip: '123.123.123.120'
         port: '80'
         maxconn: '1000'
         default_backend: 'be-mysupersite'
       haproxy_backends:
       - name: 'be-mysupersite'
         description: 'mysupersite is really cool'
         servers:
           - name: 'be-mysupersite-01'
             ip: '192.168.1.100'
```

Testing
-------

To test the role you first need to install Molecule with :

```
$ pip install molecule docker
```

If you encounter a problem while installing with pip, install [python-dev](https://stackoverflow.com/a/21530768)

To run the tests, execute :

```
$ molecule test
```

License
------

Apache v2

Author Information
------------------

This role was created in 2014 by Pheromone - Pierre Paul Lefebvre (lefebvre@pheromone.ca).

This role was forked in 2019 by Deveryware.

[The contributors list](https://github.com/Deveryware/ansible-haproxy/blob/master/AUTHORS)
