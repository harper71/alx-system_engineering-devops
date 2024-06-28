# installs flasks using pip
package { 'python':
  ensure   => '3.8.10',
  provider => 'apt',
}
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
package { 'werkzeug':
  ensure   => '2.1.1'
  provider => 'pip3',
  require  => Package['python3-pip'],
}
