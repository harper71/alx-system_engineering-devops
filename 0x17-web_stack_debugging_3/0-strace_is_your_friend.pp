# Fixes bad `phpp` extensions to `php` in a WordPress file `wp-settings.php`

$fileto_change = '/var/www/html/wp-settings.php'

#replace line containing "phpp" with "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${fileto_change}",
  path    => ['/bin','/usr/bin']
}
