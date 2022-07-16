"""

Spring time entrypoint.

"""


from spring_time.configuration.cl_configuration import CommandLineConfiguration as ClConfig

def main():

    """

    Main wrapper function for the clustering.

    This function is used to launch the clustering code. First it parses
    all the configuration (command line and optionally file) provided by the
    user. It then starts the clsutering based on the provided configuration
    and waits until either the process is killed or it errors out.

    """

    cl_config = ClConfig("command_line")
    cl_config.set()
    cl_config.parse()
    cl_config.print()

if __name__ == "__main__":
    main()
