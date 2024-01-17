# Find out why Apache is returning 500 error, then automate with Puppet

exec { 'fix_apache_500':
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  path    => ['/bin','/usr/bin'],
}
