# Fixes "phpp" to "php" in "wp-settings.php"

exec { 'fix-php-sring':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
