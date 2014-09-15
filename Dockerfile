# Sets up a container for the web based lab login
#
# VERSION               1.0.9

# At some point, more of this will be pushed into its own docker image

FROM        stanleygu/sysbio-workspace:1.0.9
MAINTAINER  Stanley Gu "stanleygu@gmail.com"

# zerorpc server
USER        user
RUN         /home/user/.virtualenvs/localpy/bin/python -c "import SedmlToRr"
