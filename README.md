# ansible-role-irods-srv
Repository for ansible role installing and configuring irods (catalogue or resource) servers. The goal of this role is to provide a comprehensive way to install and manage iRODS grids with round-robin DNS loadbalancing of servers.

## Quick start with Vagrant
### Requirements
Obviously you need vagrant - the installation was tested on vagrant 2.4.4 with ```vagrant-libvirt``` provisioner, but the box used should work on other popular provisioners like virtualbox and vmware.

Vagrant file makes use of ```vagrant-hosts``` plugin, you can install it executing: ```vagrant plugin install vagrant-hosts```

You also need ansible to run the provisioner. The setup was tested on ansible 2.5.1.
### Commands to use
If you just want to give it a try, you can just clone the repository:
```
git clone https://github.com/cinek810/ansible-role-irods-srv.git
```
and start three VMs (one server and 2 resources):
```
cd ansible-role-irods-srv ; 
vagrant up
```

The blog post describing use of  this setup is [here](https://funinit.wordpress.com/2019/05/04/ansible-based-automated-deployment-of-irods-grid/)
