#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
import signal

def run_ssh(ssh_command):
    try:
        signal.signal(signal.SIGCHLD, signal.SIG_IGN)
        process = subprocess.Popen(ssh_command, shell=True)
        process.wait()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received. Terminating SSH connection.", file=sys.stderr)
    finally:
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
        print("SSH connection closed. Exiting wrapper.", file=sys.stderr)
        sys.exit(0)

def parse_ports(ports):
    return [port.strip() for port in ports.split(',') if port.strip()]

def main():
    parser = argparse.ArgumentParser(description="Simple SSH Port Forwarding Wrapper")
    parser.add_argument('-l', '--local', type=str, help="Local port forwarding: comma-separated list of ports")
    parser.add_argument('-r', '--remote', type=str, help="Remote port forwarding: comma-separated list of ports")
    parser.add_argument('-p', '--port', type=int, default=22, help="SSH port (default: 22)")
    parser.add_argument('-u', '--user', type=str, default=os.environ.get("USER"), help="SSH user (default: $USER)")
    parser.add_argument('-H', '--host', type=str, default="127.0.0.1", help="SSH host (default: 127.0.0.1)")

    args = parser.parse_args()

    if not args.local and not args.remote:
        parser.error("At least one of --local or --remote must be specified")

    forwarding = []
    if args.local:
        local_ports = parse_ports(args.local)
        forwarding.extend([f"-L {port}:localhost:{port}" for port in local_ports])
    if args.remote:
        remote_ports = parse_ports(args.remote)
        forwarding.extend([f"-R {port}:localhost:{port}" for port in remote_ports])

    port_forwarding = " ".join(forwarding)

    ssh_command = f"ssh {port_forwarding} -p {args.port} {args.user}@{args.host}"

    print(f"Executing: {ssh_command}", file=sys.stderr)

    run_ssh(ssh_command)

if __name__ == "__main__":
    main()
