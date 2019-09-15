import logging
import argparse

from rtsparchiver.app import RSTPServer

if __name__ == "__main__":

    # Initialise logging module
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG,
    )

    # Define parser
    parser = argparse.ArgumentParser(description='RTSP Archiver')

    # Add positional arguments
    parser.add_argument('host', type=str, help='host of the RTSP server')
    parser.add_argument('port', type=str, help='port of the RTSP server')
    parser.add_argument('username', type=str, help='username used for authenticating with the RTSP server')
    parser.add_argument('password', type=str, help='password used for authenticating with the RTSP server')

    # Add optional argument
    parser.add_argument('--channel', type=str, action='append', help='channels to stream from')
    parser.add_argument('--width', type=str, help='width of video stream, defaults to 1920')
    parser.add_argument('--height', type=str, help='height of video stream, defaults to 1080')
    parser.add_argument('--fps', type=str, help='fps of video stream, defaults to 30')
    parser.add_argument('--chunk', type=str, help='chunk interval (in seconds) between each data file, defaults to 3600')
    parser.add_argument('--prefix', type=str, help='prefix for data output')

    # Parse args
    args = parser.parse_args()
    logging.debug(f"Parsed arguments: {args}")

    # Sieve args
    args_dict = {k: v for k, v in vars(args).items() if v is not None}
    del args_dict["channel"]  # Channel will be managed externally
    logging.debug(f"Sieved arguments: {args_dict}")

    # Start stream
    server = RSTPServer(**args_dict)
    for channel in args.channel:
        server.stream(channel)
