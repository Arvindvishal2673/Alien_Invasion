from cx_Freeze import setup, Executable

# Define the executables and their names
executables = [Executable("alien_invasion.py", base="Win32GUI", icon=None,)]

# Define the setup parameters
setup(
    name="ALIEN INVASION",
    version="1.0",
    description="alien invasion game",
    executables=executables,
)

