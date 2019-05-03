# ansible-role-irods-srv
Repository for ansible role installing and configuring irods (catalogue or resource) servers. The goal of this role is to provide a comprehensive way to install and manage iRODS grids with round-robin DNS loadbalancing of servers.

## Quick start with Vagrant
### Requirements
Vagrant file makes use of ```vagrant-hosts``` plugin, it's tested on ```vagrant-libvirt``` provisioner, but the box used should work on other popular provisioners like virtualbox or vmware.
### Commands to use
If you just want to give it a try, you can just clone the repository:
```
git clone https://github.com/cinek810/ansible-role-irods-srv.git
```
and start three VMs (one server and 2 resources):
```
vagrant up
```


