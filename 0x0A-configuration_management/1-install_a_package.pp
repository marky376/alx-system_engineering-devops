# Install a package

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Install Werkzeug package
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
