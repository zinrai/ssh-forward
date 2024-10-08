# SSH Port Forwarding Wrapper

This Python script provides a convenient wrapper for SSH port forwarding, allowing users to easily set up port forwarding with customizable options.

## Features

- Simplified command-line interface for SSH port forwarding
- Support for multiple binding ports
- Customizable SSH port, user, and host
- Automatic termination of the process when the SSH connection is closed

## Requirements

- Python 3.x

## Usage

```
./ssh_forward.py [-h] -b BIND_PORT [-p PORT] [-u USER] [-H HOST]
```

### Example

To forward ports 11080 and 11090 to a remote server:

```
./ssh_forward.py --bind-port 11080,11090 --port 2222 --user zinrai --host 127.0.0.1
```

Or using short options:

```
./ssh_forward.py -b 11080,11090 -p 2222 -u zinrai -H 127.0.0.1
```

## How it works

1. The script parses the command-line arguments.
2. It constructs an SSH command with the specified port forwarding options.
3. The SSH connection is established as a subprocess.
4. The script monitors the SSH connection and terminates itself when the connection is closed.

## Notes

- The script requires the `ssh` command to be available in your system's PATH.
- Make sure you have the necessary permissions to establish SSH connections to the specified host.

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) for details.
