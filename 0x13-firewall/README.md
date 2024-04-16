## What is ufw?

Uncomplicated Firewall (ufw) is a user-friendly front-end tool for managing iptables firewall rules on Linux systems. It provides a simplified interface for configuring firewall settings without needing to directly manipulate iptables rules.

## Installation

ufw is typically pre-installed on many Linux distributions. However, if it's not installed, you can install it using the package manager of your distribution. For example, on Ubuntu, you can install ufw using the following command:

```bash
sudo apt-get install ufw
```

## Basic Usage

### Enabling ufw

To enable ufw and activate the default set of rules (which usually deny all incoming and allow all outgoing connections), use the following command:

```bash
sudo ufw enable
```

### Allowing and Denying Connections

You can allow or deny specific types of connections by specifying rules. For example, to allow incoming SSH connections, use:

```bash
sudo ufw allow ssh
```

To deny incoming connections on a specific port, you can use:

```bash
sudo ufw deny <port_number>/<protocol>
```

Replace `<port_number>` with the port number you want to deny and `<protocol>` with the protocol (tcp/udp) you want to block.

### Checking Status

To check the status of ufw and view the current rules, use:

```bash
sudo ufw status
```

This will display a list of the active rules and their statuses.

### Disabling ufw

To disable ufw and deactivate the firewall, use:

```bash
sudo ufw disable
```
