# Script to install nginx using puppet

package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,

}

exec {'Hello':
  command  => '/usr/bin/echo "Hello World!" | sudo /usr/bin/tee /var/www/html/index.html',
  provider => shell,
}

# Define the Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('your_module/nginx_config.erb'),
  notify  => Exec['configure_nginx'],
}

# Define the exec to configure Nginx using sed
exec { 'configure_nginx':
  command     => '/bin/sed -i "s|server_name _|server_name _;\n\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}|" /etc/nginx/sites-available/default',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}

# Restart Nginx after configuration changes
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Exec['configure_nginx'],
}
