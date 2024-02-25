#!/usr/bin/env bash
#Puppet to make changes to our configuration file

file { 'etc/ssh/ssh_cofig':
        ensure => present,
content =>"

         #SSH client configuration
         host*
         IdentityFile ~/.ssh/school
         PasswordAuthentication no
	 ",

}
