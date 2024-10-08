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

def main():
    parser = argparse.ArgumentParser(description="SSH Port Forwarding Wrapper")
    parser.add_argument('-b', '--bind-port', type=str, required=True, help="Comma-separated list of binding ports")
    parser.add_argument('-p', '--port', type=int, default=22, help="SSH port (default: 22)")
    parser.add_argument('-u', '--user', type=str, default=os.environ.get("USER"), help="SSH user (default: $USER)")
    parser.add_argument('-H', '--host', type=str, default="127.0.0.1", help="SSH host (default: 127.0.0.1)")

    args = parser.parse_args()

    bind_ports = [port.strip() for port in args.bind_port.split(',')]
    port_forwarding = " ".join([f"-L {port}:localhost:{port}" for port in bind_ports])

    ssh_command = f"ssh {port_forwarding} -p {args.port} {args.user}@{args.host}"

    print(f"Executing: {ssh_command}", file=sys.stderr)

    run_ssh(ssh_command)

if __name__ == "__main__":
    main()
