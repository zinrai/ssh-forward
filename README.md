# SSH Port Forwarding Wrapper

This Python script provides a convenient wrapper for SSH port forwarding, allowing users to easily set up both local and remote port forwarding with customizable options.

## Features

- Simplified command-line interface for SSH port forwarding
- Support for both local and remote port forwarding
- Support for multiple ports in a single command
- Customizable SSH port, user, and host
- Automatic termination of the process when the SSH connection is closed

## Requirements

- Python 3.x

## Usage

```
./ssh-forward.py [-h] [-l LOCAL] [-r REMOTE] [-p PORT] [-u USER] -H HOST
```

### Arguments

- `-l`, `--local`: Local port forwarding: comma-separated list of ports
- `-r`, `--remote`: Remote port forwarding: comma-separated list of ports
- `-p`, `--port`: SSH port (default: 22)
- `-u`, `--user`: SSH user (default: current user)
- `-H`, `--host`: SSH host (required)

Note: At least one of `--local` or `--remote` must be specified.

### Examples

1. Local port forwarding (forwards local ports 11080 and 11090 to remote host):
   ```
   ./ssh-forward.py --local 11080,11090 --port 2222 --user zinrai --host 127.0.0.1
   ```

2. Remote port forwarding (forwards remote ports 8080 and 8090 to local host):
   ```
   ./ssh-forward.py --remote 8080,8090 --port 2222 --user zinrai --host 127.0.0.1
   ```

3. Both local and remote port forwarding:
   ```
   ./ssh-forward.py --local 11080 --remote 8080 --port 2222 --user zinrai --host 127.0.0.1
   ```

Or using short options:

```
./ssh-forward.py -l 11080,11090 -p 2222 -u zinrai -H 127.0.0.1
```

## How it works

1. The script parses the command-line arguments.
2. It constructs an SSH command with the specified local and/or remote port forwarding options.
3. The SSH connection is established as a subprocess.
4. The script monitors the SSH connection and terminates itself when the connection is closed.

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) for details.
