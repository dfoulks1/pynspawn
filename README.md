# pynspawn
systemd-nspawn wrapper for daemonizing / passing commands to a machine image

## Functions

### Daemonize

will start the chroot environment with a separate systemd instance as PID 1
Requires: machineID

### Order

Spawn a systemd instance in the chroot environment and send it a command.
requires: machineID, command
