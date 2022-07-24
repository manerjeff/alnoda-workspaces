"""
Basic example of a Mkdocs-macros module.
Include this  {{ macros_info() }} in any page to get complete macro info
"""
import os

port_increments = {
    "DOCS_URL": 0,
    "FILEBROWSER_URL": 1,
    "UNGIT_URL": 4,
    "IDE_URL": 5,
    "TERMINAL_URL": 6,
    "STREAMLIT_URL": 9,
    "PORT_8038": 18,
    "PORT_8039": 19,
    "PORT_8040": 20
    }

# this function name should not be changed
def define_env(env):
    """
    This is the hook for defining variables, macros and filters
    - variables: the dictionary that contains the environment variables
    - macro: a decorator function, to declare a macro.
    - filter: a function with one of more arguments,
        used to perform a transformation
    """
    @env.macro
    def get_tool_url(env):
        try:
            return os.environ[env]
        except:
            # Get host
            host = "localhost"
            try:
                host = os.environ["WRK_HOST"]
            except:
                pass
            proto = "http"
            try:
                proto = os.environ["WRK_PROTO"]
            except:
                pass
            # Entry port - port relative to which other ports will be calculated 
            entry_port = 8020
            try:
                entry_port = int(os.environ["ENTRY_PORT"])
            except:
                pass
            # Assign port
            try:
                port = port_increments[env] + entry_port
            except:
                port = 80
            return f"{proto}://{host}:{port}"

            