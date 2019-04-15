import os

import testinfra.utils.ansible_runner
import socket

addr=socket.gethostbyname(socket.gethostname())

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_sshd_service(host):
        with host.sudo():
                service = host.service('sshd')
                assert service.is_running
                assert service.is_enabled

def test_rsyslog_service(host):
        with host.sudo():
                service = host.service('rsyslog')
                assert service.is_running
                assert service.is_enabled

def test_ntpd(host):
	facts=host.ansible("setup")["ansible_facts"]
	if facts["ansible_os_family"] == "RedHat" and facts["ansible_distribution_major_version"] == "6":
		with host.sudo():
			service = host.service('ntpd')
			assert service.is_running
			assert service.is_enabled

def test_if_snow_deployed(host):
	cmd=host.run("getent passwd servicenow")
	assert cmd.rc == 0

def test_ssh_socket(host):
	assert host.socket("tcp://0.0.0.0:22").is_listening
