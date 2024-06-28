# installs flask using pip
package { 'python3-pip':
  ensure   => 'installed',
  provider => 'apt',
}
# Install Flask version 2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
# Install Werkzeug version 2.1.1
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
