def create_commands_table(commands):
    """Print this help text"""
    return '\n'.join(['{:<30}: {}'.format(name, func.__doc__)
                      for name, func in sorted(commands.items())])
