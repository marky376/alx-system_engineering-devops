#!/usr/bin/env bash
#Add a custom HTTP header with Puppet

exec {'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => present,
  content => "server_tokens off;\nmore_set_headers \"X-Served-By: ${::fqdn}\";",
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/conf.d/custom_headers.conf'],
}
