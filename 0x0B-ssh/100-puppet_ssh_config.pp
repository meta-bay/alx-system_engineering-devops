file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
"
}

