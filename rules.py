import re

SSH_FAILED_REGEX = re.compile(
    r"Failed password for (invalid user )?.* from (?P<ip>\d+\.\d+\.\d+\.\d+)"
)

SSH_ACCEPTED_REGEX = re.compile(
    r"Accepted password for .* from (?P<ip>\d+\.\d+\.\d+\.\d+)"
)
