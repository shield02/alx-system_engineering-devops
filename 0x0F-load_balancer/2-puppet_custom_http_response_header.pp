# automate the task of creating a custom HTTP header response

exec { 'apt-get update':
  command  => 'apt-get update',
  provider => shell,
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get update'],
}

file_line { 'Header response':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
