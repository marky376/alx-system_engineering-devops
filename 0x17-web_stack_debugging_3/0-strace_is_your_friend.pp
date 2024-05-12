exec { 'fix_apache_error':
  command  => '/bin/echo "Fixing Apache 500 error"',
  path     => '/usr/bin:/bin',
  require  => Package['apache2'], # Ensure Apache is installed first
  subscribe => File['/tmp/strace.log'], # Trigger the exec when strace.log is updated
}

