"""Engine for formatters."""

# !usr/bin/env/python3

import types

KEYWORDS_CONVERSION = types.MappingProxyType({
    'True': 'true',
    'False': 'false',
    'None': 'null',
})
