import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/derrickrose/ws02_tools/install/py04_tf_listener'
