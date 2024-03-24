# create a Puppet manifest that kills a process named "killmenow" using the exec resource and pkill

exec { 'kill_killmenow_process':
  command     => '/usr/bin/pkill killmenow',
  path        => '/usr/bin:/bin',
  refreshonly => true,
  onlyif      => '/usr/bin/pgrep killmenow',
}
