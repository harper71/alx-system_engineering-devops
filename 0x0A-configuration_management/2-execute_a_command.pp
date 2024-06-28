# kills a process
exec { 'kilmenow':
command => '/usr/bin/pkill killmenow',
path    => ['/bin', 'usr/bin'],
}
