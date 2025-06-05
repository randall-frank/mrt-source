import argparse
import datetime
from http.server import SimpleHTTPRequestHandler, HTTPServer
import logging
import os
import platform
import shutil
import subprocess
try:
    import git
    repo = git.Repo(".")
    branch_name = repo.active_branch.name
    branch_sha = repo.active_branch.commit.hexsha
    __version_git__ = f"Source: {branch_name}:{branch_sha}"
except:
    __version_git__ = ""

    
# Get the current time/date
__version_date__ = datetime.datetime.now().isoformat(timespec='minutes', sep=" ") 
    
"""
Command line build tool:

python build.py [operation] [options]

Operations:

clean
build
serve [heresy|mrtrashcan] [--port port]

"""

def clean() -> None:
    """
    Clear out the "output" directories

    :return:
    """
    for target in ["heresy", "mrtrashcan"]:
        try:
            shutil.rmtree(os.path.join(target,"output"))
            os.mkdir(os.path.join(target,"output"))
        except OSError:
            pass


def build() -> None:
    """
    Rebuild the "build" directory from scratch.

    :return:
    """
    clean()
    orig_cwd = os.getcwd()
    for target in ["heresy", "mrtrashcan"]:
        try:
            log.info(f"Building: {target}")
            os.chdir(target)
            cmd = ["pelican"]
            ret = subprocess.run(cmd, capture_output=True, text=True)
            log.info(ret.stdout)
            log.info("-"*20)
        finally:
            os.chdir(orig_cwd)
        
def serve(port : int = 9000, target : str = "heresy") -> None:
    orig_cwd = os.getcwd()
    try:
        os.chdir(os.path.join(target, "output"))
        server_address = ('127.0.0.1', port)
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
        print(f"Serving story:  http://{server_address[0]}:{server_address[1]}")
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        os.chdir(orig_cwd)
    log.info("Server stopped.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", action="store_true", default=False, help="Run in verbose mode")
    parser.add_argument("--logfile", help="Log file for verbose output", default="")
    
    cmd_parsers = parser.add_subparsers(help="Command", dest="cmd")
    cmd_parsers.required = True
    
    build_parser = cmd_parsers.add_parser("build", help="Regenerate the story .json file in the build directory")

    clean_parser = cmd_parsers.add_parser("clean", help="Remove all build directory contents")

    serve_parser = cmd_parsers.add_parser("serve", help="Server the build via http")
    serve_parser.add_argument("target", choices=["heresy", "mrtrashcan"], help="Choose the target(s).")
    serve_parser.add_argument("--port", type=int, default=9000, help="The port to use. Default: 9000")

    args = parser.parse_args()

    # Set up logging
    level = logging.WARNING
    if args.verbose:
        level = logging.INFO
    log = logging.getLogger("mrt")
    logging.basicConfig(filename=args.logfile, level=level)
    log.info(f"Command line args: {args}")
    
    if args.cmd == "build":
        build()
    elif args.cmd == "clean":
        clean()
    elif args.cmd == "serve":
        serve(port=args.port, target=args.target)
    
    log.info(f"Operation: '{args.cmd}' complete")
    
    exit(0)
