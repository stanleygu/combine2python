# Sets up a container for the web based lab login
#
# VERSION               1.0.9

# At some point, more of this will be pushed into its own docker image

FROM        stanleygu/sysbio-workspace:1.0.9
MAINTAINER  Stanley Gu "stanleygu@gmail.com"

# zerorpc server
RUN         su user -c "source /usr/local/bin/virtualenvwrapper.sh; workon localpy; pip install click==3.3"
USER        user
RUN         mkdir /home/user/combine2python
ADD         ./combine2python /home/user/combine2python
ENV         PYTHONDIR /home/user/.ipython
ENV         MPLCONFIGDIR /home/user/ipynotebooks
ENV         HOME /home/user
