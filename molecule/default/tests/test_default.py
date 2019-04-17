import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

conf_md5 = '87457a8be8e47b51d03da3154f4a1373'
conf_sha = '897215c11150201799b8c4d6e1605ab359904bfab85f39e2da2480752b55c3e8'


def test_haproxy_is_installed(host):
    haproxy = host.package('haproxy')
    assert haproxy.is_installed
    assert haproxy.version.startswith('1.5')


def test_haproxy_config_exist(host):
    config = host.file('/etc/haproxy/haproxy.cfg')
    assert config.exists


def test_haproxy_default_config_is_valid(host):
    config = host.file('/etc/haproxy/haproxy.cfg')
    assert config.md5sum == conf_md5
    assert config.sha256sum == conf_sha


def test_haproxy_is_running_and_enabled(host):
    haproxy = host.service('haproxy')
    assert haproxy.is_running
    assert haproxy.is_enabled
